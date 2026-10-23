import random as ran
import leagues_list as l_l

def bonus_power(club):
    power_number = int(club[1])
    nation_power = l_l.return_nation_power(club)
    if int(club[1]) < nation_power:
        power_number = nation_power
    if club[2] == "Беларусь":
        power_number += 7500 
    if club[0] == "Комо" or club[0] == "Болонья" or club[0] == "Хоффенхайм":
        power_number = 30000     
    if club[0] == "Кайрат":
        power_number = 20000   
    if power_number == 0: # новичок
        return 0
    if power_number > 0 and power_number < 1000: # первый раунд 1000
        return ran.randint(0, 1)
    if power_number >= 1000 and power_number < 3000: # второй раунд 2000
        return ran.randint(0, 2)
    if power_number >= 3000 and power_number < 6000: # третий раунд 3000
        return ran.randint(0, 3)
    if power_number >= 6000 and power_number < 10000: # раунд плей-офф 4000
        return 1 + ran.randint(0, 2) 
    if power_number >= 10000 and power_number < 16000: # групповая стадия 6000
        return 1 + ran.randint(0, 3)
    if power_number >= 16000 and power_number < 22000: # стыки 8000
        return 1 + ran.randint(0, 4)
    if power_number >= 22000 and power_number < 32000: # боец 10000
        return 2 + ran.randint(0, 2) 
    if power_number >= 32000 and power_number < 45000: # претендент 13000
        return 2 + ran.randint(0, 3)
    if power_number >= 45000 and power_number < 61000: # топ 16000
        return 2 + ran.randint(0, 4)
    if power_number >= 61000 and power_number < 81000: # гранд 20000
        return 3 + ran.randint(0, 2)
    if power_number >= 81000: # легенда 20000-40000
        return 3 + ran.randint(0, 3)

def group_shuffle(array):
    sorted_teams = sorted(array[:32], key=lambda x: int(x[1]), reverse=True)
    pots = [sorted_teams[i*8:(i+1)*8] for i in range(4)]
    def draw_team(pot):
        return pot.pop(ran.randint(0, len(pot) - 1))
    groups = [[] for _ in range(8)]
    for i in range(8): 
        for pot in pots:
            groups[i].append(draw_team(pot))
    print(f"Группа А: {groups[0][0][0]}, {groups[0][1][0]}, {groups[0][2][0]}, {groups[0][3][0]}")
    print(f"Группа B: {groups[1][0][0]}, {groups[1][1][0]}, {groups[1][2][0]}, {groups[1][3][0]}")
    print(f"Группа C: {groups[2][0][0]}, {groups[2][1][0]}, {groups[2][2][0]}, {groups[2][3][0]}")
    print(f"Группа D: {groups[3][0][0]}, {groups[3][1][0]}, {groups[3][2][0]}, {groups[3][3][0]}")
    print(f"Группа E: {groups[4][0][0]}, {groups[4][1][0]}, {groups[4][2][0]}, {groups[4][3][0]}")
    print(f"Группа F: {groups[5][0][0]}, {groups[5][1][0]}, {groups[5][2][0]}, {groups[5][3][0]}")
    print(f"Группа G: {groups[6][0][0]}, {groups[6][1][0]}, {groups[6][2][0]}, {groups[6][3][0]}")
    print(f"Группа H: {groups[7][0][0]}, {groups[7][1][0]}, {groups[7][2][0]}, {groups[7][3][0]}")
    return groups

def eurocup_group_games(array):
    array_1_1 = [0, 2, 0, 3, 0, 1]
    array_1_2 = [1, 0, 3, 0, 2, 0]
    array_2_1 = [2, 3, 1, 2, 1, 3]
    array_2_2 = [3, 1, 2, 1, 3, 2]
    group_data = [0, 0, 0, 0]
    for i in range(0, 6):
        club_1 = array[array_1_1[i]]
        club_2 = array[array_1_2[i]]
        club_3 = array[array_2_1[i]]
        club_4 = array[array_2_2[i]]
        club_1_score = ran.randint(0, 3) + bonus_power(club_1)
        club_2_score = ran.randint(0, 3) + bonus_power(club_2) 
        if club_1_score > club_2_score:
            group_data[array_1_1[i]] += 3
        if club_1_score == club_2_score:
            group_data[array_1_1[i]] += 1
            group_data[array_1_2[i]] += 1
        if club_1_score < club_2_score:
            group_data[array_1_2[i]] += 3
        print(f"{club_1} - {club_2} {club_1_score}:{club_2_score}")
        club_3_score = ran.randint(0, 3) + bonus_power(club_3)
        club_4_score = ran.randint(0, 3) + bonus_power(club_4) 
        if club_3_score > club_4_score:
            group_data[array_2_1[i]] += 3
        if club_3_score == club_4_score:
            group_data[array_2_1[i]] += 1
            group_data[array_2_2[i]] += 1
        if club_3_score < club_4_score:
            group_data[array_2_2[i]] += 3
        print(f"{club_3} - {club_4} {club_3_score}:{club_4_score}")
        i += 1
    print(group_data)
    
def qual_game(club_1, club_2, win_array, lose_array):
    club_1_score = ran.randint(0, 3) + ran.randint(0, 3) + bonus_power(club_1) + bonus_power(club_1)
    club_2_score = ran.randint(0, 3) + ran.randint(0, 3) + bonus_power(club_2) + bonus_power(club_2)
    while club_1_score == club_2_score:
        club_1_score = ran.randint(0, 3) + ran.randint(0, 3) + bonus_power(club_1) + bonus_power(club_1)
        club_2_score = ran.randint(0, 3) + ran.randint(0, 3) + bonus_power(club_2) + bonus_power(club_2)
    if club_1_score > club_2_score:
        win_array.append(club_1)
        lose_array.append(club_2)
    else:
        win_array.append(club_2)
        lose_array.append(club_1)
    return f"{club_1_score}:{club_2_score}"

def qual_tour(array, win_array, lose_array):
    games = 0
    while games < len(array):
        club_1 = array[games]
        club_2 = array[games + 1]
        result = qual_game(club_1, club_2, win_array, lose_array)
        print(f"{array[games]} - {array[games + 1]} {result}")
        games += 2

    
def play_game(club_1, club_2, clubs_data):
    club_1_power = clubs_data['Очки силы'][club_1]
    club_2_power = clubs_data['Очки силы'][club_2]
    diff = club_1_power - club_2_power
    club_1_score = ran.randint(0, 3) 
    club_2_score = ran.randint(0, 3) 
    if diff >= 0:
        club_1_score += diff
    else:
        club_2_score -= diff
    clubs_data["Игры"][club_1] += 1
    clubs_data["Игры"][club_2] += 1
    if club_1_score > club_2_score:
        clubs_data['Победы'][club_1] += 1
        clubs_data['Очки'][club_1] += 3
        clubs_data["Поражения"][club_2] += 1 
        clubs_data['Голов забито'][club_1] += club_1_score
        clubs_data['Голов пропущено'][club_1] += club_2_score
        clubs_data['Голов забито'][club_2] += club_2_score
        clubs_data['Голов пропущено'][club_2] += club_1_score
        clubs_data['Разница мячей'][club_1] += club_1_score - club_2_score
        clubs_data['Разница мячей'][club_2] += club_2_score - club_1_score
    if club_1_score == club_2_score:
        clubs_data['Ничьи'][club_1] += 1
        clubs_data['Очки'][club_1] += 1
        clubs_data['Ничьи'][club_2] += 1
        clubs_data['Очки'][club_2] += 1 
        clubs_data['Голов забито'][club_1] += club_1_score
        clubs_data['Голов пропущено'][club_1] += club_2_score
        clubs_data['Голов забито'][club_2] += club_2_score
        clubs_data['Голов пропущено'][club_2] += club_1_score
        clubs_data['Разница мячей'][club_1] += club_1_score - club_2_score
        clubs_data['Разница мячей'][club_2] += club_2_score - club_1_score
    if club_1_score < club_2_score:
        clubs_data['Победы'][club_2] += 1
        clubs_data['Очки'][club_2] += 3
        clubs_data["Поражения"][club_1] += 1 
        clubs_data['Голов забито'][club_1] += club_1_score
        clubs_data['Голов пропущено'][club_1] += club_2_score
        clubs_data['Голов забито'][club_2] += club_2_score
        clubs_data['Голов пропущено'][club_2] += club_1_score
        clubs_data['Разница мячей'][club_1] += club_1_score - club_2_score
        clubs_data['Разница мячей'][club_2] += club_2_score - club_1_score

def play_league(circles, league_size, clubs_data):
    club = 0
    enemy = 1
    circle = 0
    while circle < circles:
        while club < league_size:
            while enemy < league_size:
                play_game(club, enemy, clubs_data)
                enemy += 1
            club += 1
            enemy = club + 1
        circle += 1
        club = 0
        enemy = 1

def play_cup(league_size, clubs_data, league_name):
    results = []
    pulls = 0
    while pulls < league_size:
        result = ran.randint(0, 10) + clubs_data["Очки силы"][pulls]
        results.append(result)
        pulls += 1
    searcher = 0
    cup_winner = 0
    while searcher < league_size:
        if results[searcher] >= results[cup_winner]:
            cup_winner = searcher
        searcher += 1
    cup_winner_name = clubs_data["Клубы"][cup_winner], clubs_data["Евроочки"][cup_winner], league_name
    return cup_winner_name    