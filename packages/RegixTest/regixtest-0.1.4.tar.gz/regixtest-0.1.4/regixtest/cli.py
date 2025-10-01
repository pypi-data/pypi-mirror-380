# regixtest/cli.py
import argparse
import sys
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse, urljoin
from .data_extensions import DEFAULT_EXTENSIONS

__version__ = "0.1.0"

def normalize_target(target):
    if not target.startswith(("http://", "https://")):
        return "http://" + target
    return target

def check_url(url, timeout=8, method="HEAD"):
    try:
        # HEAD first, fallback to GET if server doesn't support
        resp = requests.request(method, url, allow_redirects=True, timeout=timeout)
        return resp.status_code, len(resp.content) if resp.content is not None else 0
    except requests.RequestException as e:
        return None, str(e)

def run_scan(base_target, exts=None, workers=20, timeout=8, show_success=True):
    base = normalize_target(base_target).rstrip('/')
    # if user passed a path-like target we preserve it
    parsed = urlparse(base)
    base_root = f"{parsed.scheme}://{parsed.netloc}"
    to_check = []
    for ext in (exts or DEFAULT_EXTENSIONS):
        # If target already has a trailing path segment, append ext to that.
        to_check.append(base + ext)
        # Also check at root with filename-like additions
        to_check.append(urljoin(base_root + '/', parsed.path.lstrip('/') + ext))

    # dedupe and keep order
    seen = set()
    uniq = []
    for u in to_check:
        if u not in seen:
            seen.add(u); uniq.append(u)

    results = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(check_url, u, timeout): u for u in uniq}
        for fut in as_completed(futures):
            url = futures[fut]
            try:
                status, info = fut.result()
                results.append((url, status, info))
            except Exception as e:
                results.append((url, None, str(e)))

    # print nicely
    for url, status, info in results:
        if status is None:
            print(f"[ERROR] {url} -> {info}")
        else:
            # optionally only show non-200s or show all based on show_success
            if show_success or status >= 400:
                print(f"[{status}] {url} (len={info})")

    return results

def main(argv=None):
    parser = argparse.ArgumentParser(prog="regixtest", description="Check common file extensions on a target site and print status codes.")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g. example.com or http://example.com/path)")
    parser.add_argument("-e", "--extensions", help="Comma-separated list of extensions to check (overrides default)")
    parser.add_argument("-w", "--workers", type=int, default=20, help="Concurrent worker threads (default 20)")
    parser.add_argument("-t", "--timeout", type=int, default=8, help="Request timeout seconds (default 8)")
    parser.add_argument("--show-success", action="store_true", help="Show successful responses (2xx/3xx). Default is to show all; use this to ensure successes display.")
    parser.add_argument("--version", action="version", version=__version__)
    args = parser.parse_args(argv)

    exts = None
    if args.extensions:
        # parse csv like ".php,.txt"
        exts = [x.strip() if x.strip().startswith('.') else '.' + x.strip() for x in args.extensions.split(',') if x.strip()]
    try:
        run_scan(args.domain, exts=exts, workers=args.workers, timeout=args.timeout, show_success=args.show_success)
    except KeyboardInterrupt:
        print("Interrupted by user", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
