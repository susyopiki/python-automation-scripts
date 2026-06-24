import requests
from bs4 import BeautifulSoup
import csv
import json
from datetime import datetime

# --- Configure this ---
URL = "https://www.nytimes.com/international/"  # Change to any website
OUTPUT_FORMAT = "csv"               # "csv" or "json"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def scrape(url):
    print(f"Scraping: {url}")
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to reach site: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    results = []

    # --- Scrape all links ---
    print("\n🔗 Links found:")
    for link in soup.find_all("a", href=True):
        text = link.get_text(strip=True)
        href = link["href"]
        if text:
            results.append({"type": "link", "text": text, "url": href})
            print(f"  {text} → {href}")

    # --- Scrape all headings ---
    print("\n📰 Headings found:")
    for tag in ["h1", "h2", "h3"]:
        for heading in soup.find_all(tag):
            text = heading.get_text(strip=True)
            if text:
                results.append({"type": tag, "text": text, "url": ""})
                print(f"  [{tag.upper()}] {text}")

    # --- Scrape all paragraphs ---
    print("\n📄 Paragraphs found:")
    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        if text:
            results.append({"type": "paragraph", "text": text, "url": ""})
            print(f"  {text[:80]}...")

    return results

def save_results(results, fmt):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if fmt == "csv":
        filename = f"scrape_results_{timestamp}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["type", "text", "url"])
            writer.writeheader()
            writer.writerows(results)
        print(f"\n✅ Saved {len(results)} items to {filename}")

    elif fmt == "json":
        filename = f"scrape_results_{timestamp}.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        print(f"\n✅ Saved {len(results)} items to {filename}")

# --- Run ---
data = scrape(URL)
if data:
    save_results(data, OUTPUT_FORMAT)
else:
    print("No data collected.")