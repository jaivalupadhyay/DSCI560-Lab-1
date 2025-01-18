import requests
from bs4 import BeautifulSoup
import csv

# File paths for input HTML and output CSVs
source_file_path = "../data/raw_data/web_data.html"
market_data_csv_path = '../data/processed_data/market_data.csv'
news_data_csv_path = "../data/processed_data/news_data.csv"

# Opening and parsing the HTML file
with open(source_file_path, "r", encoding="utf-8") as file:
    html_lines = file.readlines()

html_combined = "".join(html_lines)
parsed_html = BeautifulSoup(html_combined, 'html.parser')
print("HTML content successfully parsed.")

# Extracting market data
banner_section = parsed_html.select_one('div.MarketsBanner-main')
market_data_section = banner_section.select_one("div.MarketsBanner-marketData")
market_entries = market_data_section.select('a')

symbols = [entry.select_one('span.MarketCard-symbol').get_text(strip=True) for entry in market_entries]
positions = [entry.select_one('span.MarketCard-stockPosition').get_text(strip=True) for entry in market_entries]
percentage_changes = [entry.select_one('span.MarketCard-changesPct').get_text(strip=True) for entry in market_entries]

market_data = {
    "symbol": symbols,
    "position": positions,
    "percentage_change": percentage_changes
}
print("Market data has been extracted.")

print("Filtering fields....")
# Extracting news data
news_list_section = parsed_html.select_one('ul.LatestNews-list')
news_items = news_list_section.select('li.LatestNews-item')

timestamps = [item.select_one('time.LatestNews-timestamp').get_text(strip=True) for item in news_items]
headlines = [item.select_one('a.LatestNews-headline').get('title') for item in news_items]
urls = [item.select_one('a.LatestNews-headline').get('href') for item in news_items]

news_data = {
    "timestamp": timestamps,
    "headline": headlines,
    "url": urls
}
print("News data has been extracted.")

# Saving market data to CSV
with open(market_data_csv_path, mode='w', newline='', encoding='utf-8') as market_file:
    csv_writer = csv.writer(market_file)
    csv_writer.writerow(['Symbol', 'Position', 'Percentage Change'])
    csv_writer.writerows(zip(symbols, positions, percentage_changes))

# Saving news data to CSV
with open(news_data_csv_path, mode='w', newline='', encoding='utf-8') as news_file:
    csv_writer = csv.writer(news_file)
    csv_writer.writerow(['Timestamp', 'Headline', 'URL'])
    csv_writer.writerows(zip(timestamps, headlines, urls))

print("CSV files have been created and data saved.")

