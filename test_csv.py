import csv
with open("/Users/shaikmohammadusman/Desktop/Work_Project/Linkedin_Scraping/assets/inputs/harvested_urls.csv", "r", encoding="utf-8") as f:
    queue_records = list(csv.DictReader(f))
print(queue_records[0].keys())
print(queue_records[0]["candidate_name"])
