from shuffle import champions_qual, europe_qual, conference_qual
from games import group_shuffle, eurocup_group_games
print("Группы Лиги Чемпионов:")
champions_group = group_shuffle(champions_qual())
# print("Группы Лиги Европы:")
# group_shuffle(europe_qual())
# print("Группы Лиги Конференций:")
# group_shuffle(conference_qual())
eurocup_group_games(champions_group[0])
# eurocup_group_games(champions_group[1])
# eurocup_group_games(champions_group[2])
# eurocup_group_games(champions_group[3])
