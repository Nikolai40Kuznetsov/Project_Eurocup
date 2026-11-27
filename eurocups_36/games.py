import random as ran
import leagues_list as l_l
# 10 + 5x
nowice_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
               0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
               0, 0, 1, 1, 1, 1, 1, 1, 2, 2] 
first_round_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    1, 1, 1, 1, 1, 1, 2, 2, 2, 3] 
second_round_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                     0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                     1, 1, 1, 1, 2, 2, 2, 2, 3, 3]
third_round_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                    0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
                    1, 1, 2, 2, 2, 2, 2, 3, 3, 3]
playoff_round_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                      0, 0, 1, 1, 1, 1, 1, 1, 1, 1,
                      1, 1, 2, 2, 2, 2, 2, 3, 3, 4]
group_stage_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
                    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                    1, 2, 2, 2, 2, 2, 3, 3, 3, 4]
clashes_list = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 
                1, 1, 1, 1, 1, 1, 1, 1, 1, 2,
                2, 2, 2, 2, 2, 3, 3, 3, 4, 4]
warriors_list = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 
                 1, 1, 1, 1, 1, 1, 1, 1, 2, 2,
                 2, 2, 2, 3, 3, 3, 3, 4, 4, 5]
pretenders_list = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 
                   1, 1, 1, 1, 1, 1, 1, 2, 2, 2,
                   2, 2, 3, 3, 3, 3, 4, 4, 4, 5]
tops_list = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 
             1, 1, 1, 1, 1, 2, 2, 2, 2, 2,
             2, 3, 3, 3, 3, 4, 4, 4, 5, 5]
grands_list = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 
               1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
               3, 3, 3, 3, 4, 4, 4, 5, 5, 6]
legends_list = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 
                1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
                3, 3, 3, 4, 4, 4, 5, 5, 6, 7]

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
        return ran.choice(nowice_list)
    if power_number > 0 and power_number < 1000: # первый раунд 1000
        return ran.choice(first_round_list)
    if power_number >= 1000 and power_number < 3000: # второй раунд 2000
        return ran.choice(second_round_list)
    if power_number >= 3000 and power_number < 6000: # третий раунд 3000
        return ran.choice(third_round_list)
    if power_number >= 6000 and power_number < 10000: # раунд плей-офф 4000
        return ran.choice(playoff_round_list)
    if power_number >= 10000 and power_number < 16000: # групповая стадия 6000
        return ran.choice(group_stage_list)
    if power_number >= 16000 and power_number < 22000: # стыки 8000
        return ran.choice(clashes_list)
    if power_number >= 22000 and power_number < 32000: # боец 10000
        return ran.choice(warriors_list)
    if power_number >= 32000 and power_number < 45000: # претендент 13000
        return ran.choice(pretenders_list)
    if power_number >= 45000 and power_number < 61000: # топ 16000
        return ran.choice(tops_list)
    if power_number >= 61000 and power_number < 81000: # гранд 20000
        return ran.choice(grands_list)
    if power_number >= 81000: # легенда 20000-40000
        return ran.choice(legends_list)

def _make_round(team_count, pot_of, quota, played):
    for _ in range(400):
        order = list(range(team_count))
        ran.shuffle(order)
        used = set()
        pairs = []
        ok = True
        for t in order:
            if t in used:
                continue
            cands = [u for u in range(team_count)
                     if u != t and u not in used
                     and quota[t][pot_of[u]] > 0
                     and quota[u][pot_of[t]] > 0
                     and frozenset((t, u)) not in played]
            if not cands:
                ok = False
                break
            u = ran.choice(cands)
            pairs.append((t, u))
            used.add(t)
            used.add(u)
        if ok:
            return pairs
    return None

def _balance_homes(matches, teams_total, need):
    home = []
    for a, b in matches:
        home.append(a if ran.randint(0, 1) == 0 else b)
    while True:
        homes = {}
        for i in range(len(matches)):
            homes.setdefault(home[i], []).append(i)
        surplus = deficit = None
        for t in range(teams_total):
            cnt = len(homes.get(t, []))
            if cnt > need:
                surplus = t
            if cnt < need:
                deficit = t
        if surplus is None:
            return home
        parent = {surplus: None}
        queue = [surplus]
        found = False
        qi = 0
        while qi < len(queue) and not found:
            u = queue[qi]
            qi += 1
            for i in range(len(matches)):
                if home[i] == u:
                    a, b = matches[i]
                    v = b if a == u else a
                    if v not in parent:
                        parent[v] = (u, i)
                        if v == deficit:
                            found = True
                            break
                        queue.append(v)
        if not found:
            return None
        v = deficit
        while parent[v] is not None:
            u, i = parent[v]
            home[i] = v
            v = u

def group_shuffle(array, pots_count):
    teams = sorted(array[:36], key=lambda x: int(x[1]), reverse=True)
    pot_size = 36 // pots_count
    pot_of = [i // pot_size for i in range(36)]
    rounds_count = 8 if pots_count == 4 else 6
    opp_per_pot = 2 if pots_count == 4 else 1
    while True:
        quota = {t: {p: opp_per_pot for p in range(pots_count)} for t in range(36)}
        played = set()
        tours = []
        complete = True
        for r in range(rounds_count):
            pairs = _make_round(36, pot_of, quota, played)
            if pairs is None:
                complete = False
                break
            for t, u in pairs:
                quota[t][pot_of[u]] -= 1
                quota[u][pot_of[t]] -= 1
                played.add(frozenset((t, u)))
            tours.append(pairs)
        if complete:
            break
    flat = []
    for r, pairs in enumerate(tours):
        for h, a in pairs:
            flat.append((h, a, r))
    pairs_only = [(h, a) for h, a, r in flat]
    homes = _balance_homes(pairs_only, 36, len(pairs_only) // 36)
    result = [[] for _ in range(rounds_count)]
    for (h, a, r), home in zip(flat, homes):
        if h == home:
            result[r].append((h, a))
        else:
            result[r].append((a, h))
    for p in range(pots_count):
        pot_teams = [teams[i][0] for i in range(36) if pot_of[i] == p]
        print(f"Корзина {p + 1}: " + ", ".join(pot_teams))
    return teams, result


def eurocup_league_games(teams, tours, direct_list=None, clashes_list=None):
    break_nations(teams)
    n = len(teams)
    points = [0] * n
    wins = [0] * n
    draws = [0] * n
    losses = [0] * n
    gf = [0] * n
    ga = [0] * n
    for num, tour in enumerate(tours, 1):
        print(f"Тур {num}:")
        for h, a in tour:
            hs = bonus_power(teams[h])
            a_s = bonus_power(teams[a])
            print(f"{teams[h][0]} - {teams[a][0]} {hs}:{a_s}")
            gf[h] += hs
            ga[h] += a_s
            gf[a] += a_s
            ga[a] += hs
            if hs > a_s:
                points[h] += 3
                wins[h] += 1
                losses[a] += 1
            elif hs < a_s:
                points[a] += 3
                wins[a] += 1
                losses[h] += 1
            else:
                points[h] += 1
                points[a] += 1
                draws[h] += 1
                draws[a] += 1
    order = sorted(range(n), key=lambda t: (points[t], gf[t] - ga[t], gf[t]), reverse=True)
    print("Общая таблица:")
    for place, t in enumerate(order, 1):
        print(f"{place}. {teams[t][0]} — {points[t]} очк. "
              f"({wins[t]}-{draws[t]}-{losses[t]}, мячи {gf[t]}:{ga[t]})")
    if direct_list is not None:
        for t in order[:8]: 
            direct_list.append(teams[t])
    if clashes_list is not None:
        for k in range(8): 
            clashes_list.append(teams[order[8 + k]])
            clashes_list.append(teams[order[23 - k]])
    return order


def playoffs_draft(array, positions, path_1, path_2, path_3):
    places_positions = sorted(positions)
    winner = places_positions[3]
    runner_up = places_positions[2]
    dropped = places_positions[1]
    i = 0
    while i < 4:
        if positions[i] == dropped:
            dropped = i
            positions[i] = 999
        if positions[i] == runner_up:
            runner_up = i
            positions[i] = 999
        if positions[i] == winner:
            winner = i
            positions[i] = 999
        i += 1
    path_1.append(array[winner])
    path_2.append(array[runner_up])
    path_3.append(array[dropped])
    
def qual_game(club_1, club_2, win_array, lose_array):
    club_1_score = bonus_power(club_1) + bonus_power(club_1)
    club_2_score = bonus_power(club_2) + bonus_power(club_2)
    while club_1_score == club_2_score:
        club_1_score = bonus_power(club_1) + bonus_power(club_1)
        club_2_score = bonus_power(club_2) + bonus_power(club_2)
    if club_1_score > club_2_score:
        win_array.append(club_1)
        lose_array.append(club_2)
    else:
        win_array.append(club_2)
        lose_array.append(club_1)
    return f"{club_1_score}:{club_2_score}"

def break_nations(array):
    pairs = len(array) / 2
    i = 0
    while i < pairs:
        while array[i][2] == array[i+1][2]:
            ran.shuffle(array)
        i += 2

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
