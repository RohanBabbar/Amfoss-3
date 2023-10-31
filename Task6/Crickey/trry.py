from bs4 import BeautifulSoup
import requests
import json
import csv

csv_file = "cricket_scores.csv"
url = 'https://www.espncricinfo.com/live-cricket-score'
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, 'html.parser')
score_card = soup.find('div', class_ = 'ds-flex ds-flex-wrap')
score_card = score_card.find_all(recursive=False)

res = []
for i in score_card:
    D = json.loads(i.find('script').get_text())
    Arr = [j.get_text() for j in (i.find_all('span'))] + [j.get_text() for j in (i.find_all('strong'))]
    res.append({"Match": D['name'], "Description": D['description'], "Score": f"{Arr[-2]} / {Arr[-1]}"})

with open(csv_file, mode="w", newline="") as file:
    fieldnames = ["Match", "Description", "Score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()

    for match in res:
        if match["Description"] == 'Live':
            print(f"{match['Match']}\n{match['Description']}\n{match['Score']}")
        writer.writerow(match)
