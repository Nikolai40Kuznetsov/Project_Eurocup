from shuffle import champions_qual, europe_qual, conference_qual
from games import group_shuffle, eurocup_league_games, playoffs_draft

champions_playoffs_list = [] 
champions_clashes_list = [] 
europe_playoffs_list = [] 
europe_clashes_list = []      
conference_playoffs_list = [] 
conference_clashes_list = []  
dropped = [] 

champions_groups = champions_qual()
print("Лига Чемпионов — общий этап:")
champions_teams, champions_tours = group_shuffle(champions_groups, 4)
eurocup_league_games(champions_teams, champions_tours, champions_playoffs_list, champions_clashes_list)
europe_groups = europe_qual()
print("Лига Европы — общий этап:")
europe_teams, europe_tours = group_shuffle(europe_groups, 4)
eurocup_league_games(europe_teams, europe_tours, europe_playoffs_list, europe_clashes_list)
conference_groups = conference_qual()
print("Лига Конференций — общий этап:")
conference_teams, conference_tours = group_shuffle(conference_groups, 6)
eurocup_league_games(conference_teams, conference_tours, conference_playoffs_list, conference_clashes_list)
