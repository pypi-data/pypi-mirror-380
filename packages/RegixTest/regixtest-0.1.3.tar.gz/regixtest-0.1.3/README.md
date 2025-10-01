# RegixTest

Python CLI tool যা ওয়েবসাইটে সাধারণ ফাইল এক্সটেনশন চেক করে এবং HTTP status code দেখায়।

## ব্যবহার

```bash
# ডিফল্ট 30+ এক্সটেনশন চেক
regixtest -d example.com

# কাস্টম এক্সটেনশন ব্যবহার
regixtest -d example.com -e .php,.git,.env -w 10
