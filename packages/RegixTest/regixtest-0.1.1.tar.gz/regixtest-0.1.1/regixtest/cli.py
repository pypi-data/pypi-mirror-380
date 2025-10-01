import requests
import argparse
from .data_extensions import DEFAULT_EXTENSIONS

def check_extensions(domain, extensions, timeout=5):
    print(f"Checking {domain} for {len(extensions)} extensions...")
    for ext in extensions:
        url = f"https://{domain}/{ext}"
        try:
            r = requests.get(url, timeout=timeout)
            print(f"{url} -> {r.status_code}")
        except requests.RequestException as e:
            print(f"{url} -> ERROR ({e})")

def main():
    parser = argparse.ArgumentParser(description="RegixTest: Check common file extensions on a website")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (without https://)")
    parser.add_argument("-e", "--extensions", help="Comma-separated list of extensions to check")
    parser.add_argument("-t", "--timeout", type=int, default=5, help="Request timeout in seconds")

    args = parser.parse_args()

    domain = args.domain
    if args.extensions:
        extensions = [ext.strip() for ext in args.extensions.split(",")]
    else:
        extensions = DEFAULT_EXTENSIONS

    check_extensions(domain, extensions, timeout=args.timeout)

if __name__ == "__main__":
    main()
