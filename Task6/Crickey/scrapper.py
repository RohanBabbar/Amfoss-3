
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

# print(score_card)
# score = score_card.get_text().strip()
res = []
for i in score_card:
    D =  json.loads(i.find('script').get_text())
    # print(D)
    Arr =[j.get_text() for j in (i.find_all('span'))] + [j.get_text() for j in (i.find_all('strong'))]
    # print(Arr)
    res.append([D,Arr])
# print(res)
for k in res:
    if k[1][0]=='Live':
        print(f'''{k[0]['name']}
{k[0]['description']}
{k[1][-2]}   /   {k[1][-1]}''')
for k in res:
    if k[1][0]=='RESULT':
        print(f'''{k[0]['name']}
{k[0]['description']}
{k[1][-2]}   /   {k[1][-1]}''')
        
with open(csv_file, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Match", "Team 1", "Team 2", "Score1", "Score2"])
    writer.writeheader()
    for match in res:
        # match_name = match[0]['name']
        # team1, team2 = match_name.split(' vs ')
        teams = match[0]['name'].split(" vs ")

        team1 = teams[0]
        team2 = teams[1]
        team2_parts = team2.split()[:-2]

        team2 = " ".join(team2_parts)
        if match[1][0]=='Live':
            print(f'''{match[0]['name']}
                {match[0]['description']}
                {match[1][-2]}   /   {match[1][-1]}''')
        writer.writerow({"Match": match[1][3], "Team 1":  team1, "Score1" : (match[1][-2])+"_", "Team 2" : team2, "Score2" : (match[1][-1])+"_"})
# url = 'https://www.espncricinfo.com/live-cricket-score'
# response = requests.get(url)
# content = response.text
# soup = BeautifulSoup(content, 'lxml')
# score_card = soup.find('div', class_ = 'ds-flex ds-flex-wrap')
# score_card = score_card.find_all(recursive=False)

# # print(score_card)
# # score = score_card.get_text().strip()

# # dict_list = []
# # arr_list = []
# # # strong_list = []
# # # for i in score_card:
    
#     # # script_tag = i.find('script')
#     # # if script_tag:
#     #     # script_text = script_tag.get_text()
#         # # data_dict = json.loads(script_text)
#         # # dict_list.append(data_dict)

#     # # span_tags = i.find_all('span')
#     # # arr_data = [span.get_text() for span in span_tags]
#     # # arr_list.append(arr_data)

#     # # strong_tag = i.find('strong')
#     # # if strong_tag:
#     #     # strong_data = strong_tag.get_text()
#         # # strong_list.append(strong_data)
#         # break
# # 

# # # print(dict_list)
# # # # print(arr_list)
# # # first_names = []
# # # descriptions = []

# # # for data_dict in dict_list:
# #     # found_first_name = False
#     # # found_first_description = False
#     # # found_location = False

#     # # for key, value in data_dict.items():
#     #     # if key == "name" and not found_first_name:
#         #     # first_names.append(value)
#         #     # found_first_name = True
#         # # if key == "description" and not found_first_description:
#         #     # descriptions.append(value)
#             # # found_first_description = True

#     # # if found_first_name and found_first_description:
#     #     # break
# # 

# # # print(first_names[0])
# # # print(strong_list)
# # print(descriptions[0])