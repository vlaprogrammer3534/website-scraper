import requests
from bs4 import BeautifulSoup
import json

BASE_URL = " "  # website ulr with  specific page that you scrape
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

def scrape_chapter(chapter_num):
    url = f"{BASE_URL}{chapter_num}/"
    print(f"🔍 Scraping Chapter {chapter_num}...")

    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"❌ Failed to load Chapter {chapter_num}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    hadith_blocks = soup.select("div.hadit_box")
    
    hadiths = []
    for block in hadith_blocks:
        title = block.find("a", class_="title").text.strip().replace('\n', '')
        number = ''.join(filter(str.isdigit, title))
        short_text = block.find("p").text.strip()
        link = block.find("a", class_="view_more_link")["href"]
        full_link = "https://example.com" + link # full link website 

        hadiths.append({
            "number": number,
            "short_text": short_text,
            "full_link": full_link
        })

    return hadiths

def main():
    all_hadiths = []
    for chapter in range(1, 99):  # Or however many chapters you want
        chapter_hadiths = scrape_chapter(chapter)
        all_hadiths.extend(chapter_hadiths)

    print(f"\n✅ Done! Total hadiths scraped: {len(all_hadiths)}")

    with open("your file name .json", "w", encoding="utf-8") as f:
        json.dump(all_hadiths, f, ensure_ascii=False, indent=2)
        print("📁 File saved as: file name .json")

if __name__ == "__main__":
    main()
