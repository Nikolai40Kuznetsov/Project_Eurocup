import random as ran
from games import qual_tour
from group_shuffle import champions_playoffs_list, europe_playoffs_list, europe_clashes_list, conference_playoffs_list, conference_clashes_list
champions_quarterfinals = []
champions_semifinals = []
champions_final = []
champions_winner = []
europe_quarterfinals = []
europe_semifinals = []
europe_final = []
europe_winner = []
conference_quarterfinals = []
conference_semifinals = []
conference_final = []
conference_winner = []
dropped = []
print("1/8 Лиги Чемпионов")
ran.shuffle(champions_playoffs_list)
qual_tour(champions_playoffs_list, champions_quarterfinals, dropped)
print("1/4 Лиги Чемпионов")
ran.shuffle(champions_quarterfinals)
qual_tour(champions_quarterfinals, champions_semifinals, dropped)
print("1/2 Лиги Чемпионов")
ran.shuffle(champions_semifinals)
qual_tour(champions_semifinals, champions_final, dropped)
print("Финал Лиги Чемпионов")
qual_tour(champions_final, champions_winner, dropped)
print("Победитель Лиги Чемпионов:", champions_winner[0][0])
print("Стыки Лиги Европы")
ran.shuffle(europe_clashes_list)
qual_tour(europe_clashes_list, europe_playoffs_list, dropped)
print("1/8 Лиги Европы")
ran.shuffle(europe_playoffs_list)
qual_tour(europe_playoffs_list, europe_quarterfinals, dropped)
print("1/4 Лиги Европы")
ran.shuffle(europe_quarterfinals)
qual_tour(europe_quarterfinals, europe_semifinals, dropped)
print("1/2 Лиги Европы")
ran.shuffle(europe_semifinals)
qual_tour(europe_semifinals, europe_final, dropped)
print("Финал Лиги Европы")
qual_tour(europe_final, europe_winner, dropped)
print("Победитель Лиги Европы:", europe_winner[0][0])
print("Стыки Лиги Конференций")
ran.shuffle(conference_clashes_list)
qual_tour(conference_clashes_list, conference_playoffs_list, dropped)
print("1/8 Лиги Конференций")
ran.shuffle(conference_playoffs_list)
qual_tour(conference_playoffs_list, conference_quarterfinals, dropped)
print("1/4 Лиги Конференций")
ran.shuffle(conference_quarterfinals)
qual_tour(conference_quarterfinals, conference_semifinals, dropped)
print("1/2 Лиги Конференций")
ran.shuffle(conference_semifinals)
qual_tour(conference_semifinals, conference_final, dropped)
print("Финал Лиги Конференций")
qual_tour(conference_final, conference_winner, dropped)
print("Победитель Лиги Конференций:", conference_winner[0][0])