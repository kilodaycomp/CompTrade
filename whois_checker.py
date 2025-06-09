#!/usr/bin/env python3
import sys
import whois

def check_domain(domain):
    try:
        w = whois.whois(domain)
        if w.status is None:
            print(f"✅ {domain} appears to be available.")
        else:
            print(f"❌ {domain} is already registered.")
    except Exception as e:
        print(f"⚠️ Could not check {domain}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <domain>")
        sys.exit(1)
    check_domain(sys.argv[1])
