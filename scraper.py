import requests
from bs4 import BeautifulSoup
import csv

# URL to scrape (example: BBC News homepage)
url = "https://www.bbc.com/news"

# Send HTTP request
response = requests.get(url)
response.raise_for_status()  # Raise error if request fails

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract specific data (e.g., news headlines)
headlines = []
for h in soup.find_all("h3"):  # BBC uses <h3> for many headlines
    text = h.get_text(strip=True)
    if text:  # avoid empty strings
        headlines.append(text)

# Save to CSV
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Headline"])  # column header
    for headline in headlines:
        writer.writerow([headline])

print("✅ Data scraped and saved to scraped_data.csv")
