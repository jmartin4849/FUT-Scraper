import bs4
import requests
import lxml
import csv
import os
import sqlite3
import math
from sqlite3 import Error
from populatorHelper import *

path = os.getcwd()
db_file = "\Player-SQL-Database.db"
print(path + db_file)
conn = create_connection(path + db_file)
create_player_table = """ CREATE TABLE IF NOT EXISTS players (
                                        pid integer PRIMARY KEY,
                                        name text NOT NULL,
                                        value real,
                                        rating integer,
                                        card_type text,
                                        club text,
                                        nation text,
                                        league text
                                    ); """
if conn is not None:
        # create projects table
    create_table(conn, create_player_table)
else:
    print("Error! cannot create the database connection.")

with open('FUT-player-database.csv', mode='w', encoding="utf-8", newline='') as player_file:
    player_writer = csv.writer(player_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    player_id = 0
    for page in range(500):
        print(page)
        response = requests.get('https://www.futbin.com/players?page=' + str(page))

        soup = bs4.BeautifulSoup(response.text, 'lxml')
        numbers = [1,2]
        for number in numbers:
            players = soup.findAll('tr', 'player_tr_'+str(number))
            for p in players:
                tds = p.findAll('td')
                name = tds[0].text.strip()
                card_type = ""
                value = p.find('span', "ps4_color font-weight-bold").get_text()
                rating = p.find('span', "form rating ut22 gold rare")
                for _ in range(1):
                    if rating == None:
                        rating = p.find('span', "form rating ut22 gold non-rare")
                    else:
                        card_type = "gold rare"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 icon gold rare")
                    else: 
                        card_type = "gold non-rare"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 otw gold rare")
                    else:
                        card_type = "Icon"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 vip gold rare")
                    else:
                        card_type = "otw gold"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 potm_laliga gold rare")#Goes here
                    else:
                        card_type = "otw vip"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 potm_epl gold rare")#Goes here
                    else:
                        card_type = "POTM Laliga"#ABOVE GOES HERE
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 potm_seriea gold rare")#Goes here
                    else:
                        card_type = "POTM prem"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 heroes gold rare")#Goes here
                    else:
                        card_type = "POTM seriea"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 if gold rare")#Goes here
                    else:
                        card_type = "hero"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 sbc_flashback gold rare")#Goes here
                    else:
                        card_type = "IF gold"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 objective_reward gold rare")#Goes here
                    else:
                        card_type = "SBC Flashback"#ABOVE GOES HERE
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 potm_eredivisie gold rare")#Goes here
                    else:
                        card_type = "obj gold"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 libertadores_b gold rare")#Goes here
                    else:
                        card_type = "POTM eridiv"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 sudamericana gold rare")#Goes here
                    else:
                        card_type = "liber gold rare"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 silver rare")#Goes here
                    else:
                        card_type = "sudamericana gold rare"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 silver non-rare")#Goes here
                    else:
                        card_type = "silver rare"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 libertadores_b silver rare")#Goes here
                    else:
                        card_type = "silver non-rare"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 sudamericana silver rare")#Goes here
                    else:
                        card_type = "liber silver rare"#ABOVE GOES HERE
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 if silver rare")#Goes here
                    else:
                        card_type = "sudamericana silver rare"#ABOVE GOES HERE
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 bronze rare")#Goes here
                    else:
                        card_type = "IF silver"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 bronze non-rare")#Goes here
                    else:
                        card_type = "bronze rare"#ABOVE GOES HERE
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 sudamericana bronze rare")#Goes here
                    else:
                        card_type = "bronze non-rare"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 libertadores_b bronze rare")#Goes here
                        pass
                    else:
                        card_type = "sudamericana bronze rare"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 potm_bundesliga gold rare")#Goes here
                        pass
                    else:
                        card_type = "liber bronze rare"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 conference gold rare")#Goes here
                        pass
                    else:
                        card_type = "POTM bundisliga"
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 ucl_live gold rare")#Goes here
                        pass
                    else:
                        card_type = "conference gold rare"#ABOVE GOES HERE
                        break
                    if rating == None:
                        rating = p.find('span', 'form rating ut22 europa_live gold rare')#Goes here
                        pass
                    else:
                        card_type = "ucl live gold rare"#ABOVE GOES HERE
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 fgs_swaps_1 bronze rare")#Goes here
                        pass
                    else:
                        card_type = "europa live gold rare"#ABOVE GOES HERE
                        break
                    if rating == None:
                        rating = p.find('span', "form rating ut22 bluered gold rare")#Goes here
                        pass
                    else:
                        card_type = "bronze rare fgs_swap"#ABOVE GOES HERE
                        break
                    if rating == None:
                        #rating = p.find('span', )#Goes here
                        pass
                    else:
                        card_type = "bluered gold rare"#ABOVE GOES HERE
                        break
                    '''
                    if rating == None:
                        #rating = p.find('span', )#Goes here
                        pass
                    else:
                        card_type = #ABOVE GOES HERE
                        break
                    '''

                if rating != None:
                    rating = rating.get_text()
                else:
                    print(tds)
                clubs = p.find('span', 'players_club_nation').findAll('a')
                club = clubs[0]['data-original-title'].replace('Icons', 'unknown').strip()
                nation = clubs[1]['data-original-title'].replace('Icons', 'unknown').strip()
                league = clubs[2]['data-original-title'].replace('Icons', 'unknown').strip()
                value.rstrip()
                if 'M' in value:
                    idx = value.find('M')
                    value = float(value[:idx]) * 1e6
                elif 'K' in value:
                    idx = value.find('K')
                    value = float(value[:idx]) * 1e3
                else:
                    value = float(value)
                rating = int(rating)
                print('Name     : ',name)
                print('Value    : ', value)
                print('rating   : ', rating)
                print('Type     : ', card_type)
                print('Club     : ', club)
                print('Nation   : ',nation)
                print('League   : ',league,'\n')
                player_params = [player_id, name, value, rating, card_type, club, nation, league]
                player_writer.writerow([player_id, name, value, rating, card_type, club, nation, league])
                create_player(conn, player_params)
                player_id += 1





#<td><span class="xb1_color font-weight-bold">0 <img alt="c" class="small-coins-icon" src="./players page_files/coins_bin.png"></span></td>
#<div id="pslowest3" class="hide">6230000</div>

#<td><span class="ps4_color font-weight-bold">550 <img alt="c" class="small-coins-icon" src="/design/img/coins_bin.png"/></span> </td>