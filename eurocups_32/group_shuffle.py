from shuffle import champions_qual, europe_qual, conference_qual
from games import group_shuffle
print("Группы Лиги Чемпионов:")
group_shuffle(champions_qual())
print("Группы Лиги Европы:")
group_shuffle(europe_qual())
print("Группы Лиги Конференций:")
group_shuffle(conference_qual())
