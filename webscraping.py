import requests
from bs4 import BeautifulSoup
import csv
date = input("please enter a date in the follwing format MM/DD/YYYY:")
page = requests.get(
    f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}")


def main(page):
    src = page.content
    soup = BeautifulSoup(src, "lxml")
    matches_details = []
    championships = soup.find_all("div", {'class': 'matchCard'})

    def get_match_info(championships):
        championship_title = championships.contents[1].find('h2').text.strip()
        all_matches = championships.contents[3].find_all('li')
        number_of_matches = len(all_matches)
        for i in range(number_of_matches):
            team_A = all_matches[i].find(
                'div', {'class': 'team_A'}).text.strip()
            team_B = all_matches[i].find(
                'div', {'class': 'team_B'}).text.strip()
            match_result = all_matches[i].find(
                'div', {'class': 'MResult'}).find_all('span', {'class': 'score'})
            score = f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
            match_time = all_matches[i].find('div', {'class': 'MResult'}).find(
                'span', {'class': 'time'}).text.stip()
            # add match info to matches details
            matches_details.append({"نوع البطوله": championship_title, "الفريق الاول": team_A,
                                   "الفريق الثاني": team_B, "ميعاد المباراه": match_time, "النتيجه": score})

    for i in range(len(championships)):

        get_match_info(championships[i])
    keys = matches_details[0].keys()
    with open('Documents/yallakora/matches-details.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(matches_details)
        print("file created")
        
main(page)

