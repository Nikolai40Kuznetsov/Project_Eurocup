import random as ran
from games import qual_tour
import leagues.albanian_league as albanian_league
import leagues.armenian_league as armenian_league
import leagues.austrian_league as austrian_league
import leagues.azerbaijanian_league as azerbaijanian_league
import leagues.belarussian_league as belarussian_league
import leagues.belgian_league as belgian_league
import leagues.bosnian_league as bosnian_league
import leagues.bulgarian_league as bulgarian_league
import leagues.croatian_league as croatian_league
import leagues.cypriot_league as cypriot_league
import leagues.czech_league as czech_league
import leagues.danish_league as danish_league
import leagues.deutch_league as deutch_league
import leagues.dutch_league as dutch_league
import leagues.english_league as english_league
import leagues.estonian_league as estonian_league
import leagues.faroe_league as faroe_league
import leagues.finnish_league as finnish_league
import leagues.french_league as french_league
import leagues.georgian_league as georgian_league
import leagues.greek_league as greek_league
import leagues.hungarian_league as hungarian_league
import leagues.irish_league as irish_league 
import leagues.islandian_league as islandian_league
import leagues.italian_league as italian_league
import leagues.jewish_league as jewish_league
import leagues.kazakh_league as kazakh_league
import leagues.kosovar_league as kosovar_league
import leagues.makedonian_league as makedonian_league
import leagues.moldovan_league as moldovan_league
import leagues.montenegrin_league as montenegrin_league
import leagues.norwegian_league as norwegian_league
import leagues.polish_league as polish_league
import leagues.portugese_league as portugese_league
import leagues.romanian_league as romanian_league
import leagues.russian_league as russian_league
import leagues.scottish_league as scottish_league
import leagues.serbian_league as serbian_league
import leagues.slovakian_league as slovakian_league
import leagues.slovenian_league as slovenian_league
import leagues.spanish_league as spanish_league
import leagues.sweden_league as sweden_league
import leagues.swiss_league as swiss_league
import leagues.turkish_league as turkish_league
import leagues.ukrainian_league as ukrainian_league
champions_first_round = []
champions_second_round = []
champions_third_round = []
champions_fourth_round = []
champions_main_round = []
europe_first_round = []
europe_second_round = []
europe_third_round = []
europe_fourth_round = []
europe_main_round = []
conference_first_round = []
conference_second_round = []
conference_third_round = []
conference_fourth_round = []
conference_main_round = []
pretenders_first_round = []
pretenders_second_round = []
pretenders_third_round = []
pretenders_fourth_round = []
pretenders_main_round = []
off_pull = []
# Участники первого раунда ЛЧ
champions_first_round.append(bosnian_league.champions_qual()) 
champions_first_round.append(faroe_league.champions_qual())
champions_first_round.append(kazakh_league.champions_qual()) 
champions_first_round.append(kosovar_league.champions_qual()) 
champions_first_round.append(azerbaijanian_league.champions_qual())
champions_first_round.append(belarussian_league.champions_qual())
champions_first_round.append(bulgarian_league.champions_qual())
champions_first_round.append(finnish_league.champions_qual())
champions_first_round.append(irish_league.champions_qual())
champions_first_round.append(islandian_league.champions_qual())
champions_first_round.append(jewish_league.champions_qual())
champions_first_round.append(moldovan_league.champions_qual())
champions_first_round.append(serbian_league.champions_qual())
champions_first_round.append(slovakian_league.champions_qual())
champions_first_round.append(slovenian_league.champions_qual())
champions_first_round.append(ukrainian_league.champions_qual())
# Участники второго раунда ЛЧ
champions_second_round.append(croatian_league.champions_qual())
champions_second_round.append(cypriot_league.champions_qual())
champions_second_round.append(greek_league.champions_qual())
champions_second_round.append(hungarian_league.champions_qual())
champions_second_round.append(polish_league.champions_qual())
champions_second_round.append(romanian_league.champions_qual())
champions_second_round.append(russian_league.champions_qual())
champions_second_round.append(sweden_league.champions_qual())
# Участники третьего раунда ЛЧ
champions_third_round.append(austrian_league.champions_qual())
champions_third_round.append(czech_league.champions_qual())
champions_third_round.append(norwegian_league.champions_qual())
champions_third_round.append(scottish_league.champions_qual())
# Участники отборочного раунда плей-офф ЛЧ
champions_fourth_round.append(belgian_league.champions_qual())
champions_fourth_round.append(danish_league.champions_qual())
champions_fourth_round.append(swiss_league.champions_qual())
champions_fourth_round.append(turkish_league.champions_qual())
# Участники группового этапа ЛЧ
champions_main_round.append(deutch_league.champions_qual_1())
champions_main_round.append(deutch_league.champions_qual_2())
champions_main_round.append(dutch_league.champions_qual())
champions_main_round.append(english_league.champions_qual_1())
champions_main_round.append(english_league.champions_qual_2())
champions_main_round.append(french_league.champions_qual())
champions_main_round.append(italian_league.champions_qual_1())
champions_main_round.append(italian_league.champions_qual_2())
champions_main_round.append(portugese_league.champions_qual())
champions_main_round.append(spanish_league.champions_qual_1())
champions_main_round.append(spanish_league.champions_qual_2())
# Участники первого раунда ЛЕ
europe_first_round.append(austrian_league.europe_qual())
europe_first_round.append(cypriot_league.europe_qual())
europe_first_round.append(danish_league.europe_qual())
europe_first_round.append(greek_league.europe_qual())
europe_first_round.append(norwegian_league.europe_qual())
europe_first_round.append(polish_league.europe_qual())
europe_first_round.append(romanian_league.europe_qual())
europe_first_round.append(swiss_league.europe_qual())
# Участники второго раунда ЛЕ
europe_second_round.append(belgian_league.europe_qual())
europe_second_round.append(croatian_league.europe_qual())
europe_second_round.append(czech_league.europe_qual())
europe_second_round.append(russian_league.europe_qual())
europe_second_round.append(scottish_league.europe_qual())
europe_second_round.append(turkish_league.europe_qual())
# Участники третьего раунда ЛЕ
europe_third_round.append(dutch_league.europe_qual())
europe_third_round.append(french_league.europe_qual())
europe_third_round.append(portugese_league.europe_qual())
# Участники группового этапа ЛЕ
europe_main_round.append(deutch_league.europe_qual())
europe_main_round.append(english_league.europe_qual())
europe_main_round.append(italian_league.europe_qual())
europe_main_round.append(spanish_league.europe_qual())
# Участники первого раунда ЛК
conference_first_round.append(austrian_league.conference_qual())
conference_first_round.append(belarussian_league.conference_qual())
conference_first_round.append(belgian_league.conference_qual())
conference_first_round.append(bulgarian_league.conference_qual())
conference_first_round.append(croatian_league.conference_qual())
conference_first_round.append(cypriot_league.conference_qual())
conference_first_round.append(czech_league.conference_qual())
conference_first_round.append(danish_league.conference_qual())
conference_first_round.append(finnish_league.conference_qual())
conference_first_round.append(greek_league.conference_qual())
conference_first_round.append(hungarian_league.conference_qual())
conference_first_round.append(jewish_league.conference_qual())
conference_first_round.append(norwegian_league.conference_qual())
conference_first_round.append(polish_league.conference_qual())
conference_first_round.append(romanian_league.conference_qual())
conference_first_round.append(russian_league.conference_qual())
conference_first_round.append(scottish_league.conference_qual())
conference_first_round.append(serbian_league.conference_qual())
conference_first_round.append(sweden_league.conference_qual())
conference_first_round.append(swiss_league.conference_qual())
conference_first_round.append(turkish_league.conference_qual())
conference_first_round.append(ukrainian_league.conference_qual())
# Участники второго раунда ЛК
conference_second_round.append(deutch_league.conference_qual())
conference_second_round.append(dutch_league.conference_qual())
conference_second_round.append(english_league.conference_qual())
conference_second_round.append(french_league.conference_qual())
conference_second_round.append(italian_league.conference_qual())
conference_second_round.append(portugese_league.conference_qual())
conference_second_round.append(spanish_league.conference_qual())
# Участники первого раунда ЛП
pretenders_first_round.append(("Линкольн Ред Импс", "13500"))
# Участники второго раунда ЛП
pretenders_second_round.append(kazakh_league.pretenders_qual())
pretenders_second_round.append(bosnian_league.pretenders_qual())
# Участники третьего раунда ЛП
pretenders_third_round.append(armenian_league.pretenders_qual_1())
pretenders_third_round.append(estonian_league.pretenders_qual())
pretenders_third_round.append(makedonian_league.pretenders_qual())
# Участники отборочного раунда плей-офф ЛП
pretenders_fourth_round.append(moldovan_league.pretenders_qual())
pretenders_fourth_round.append(faroe_league.pretenders_qual())
pretenders_fourth_round.append(albanian_league.pretenders_qual())
pretenders_fourth_round.append(armenian_league.pretenders_qual_2())
# Участники группового этапа ЛП
pretenders_main_round.append(islandian_league.pretenders_qual())
pretenders_main_round.append(belarussian_league.pretenders_qual())
pretenders_main_round.append(georgian_league.pretenders_qual())
pretenders_main_round.append(kosovar_league.pretenders_qual())
pretenders_main_round.append(montenegrin_league.pretenders_qual())
pretenders_main_round.append(("Хамрун Спартанс", "8000"))
pretenders_main_round.append(("Расинг Юнион", "3500"))
pretenders_main_round.append(("Виртус", "4000"))
pretenders_main_round.append(("Интер Эскальдес", "7500"))
pretenders_main_round.append(("Вадуц", "8500"))
def champions_qual():
    ran.shuffle(champions_first_round)
    print("Результаты первого квалификационного раунда Лиги Чемпионов:")
    qual_tour(champions_first_round, champions_second_round, conference_second_round)
    ran.shuffle(champions_second_round)
    print("Результаты второго квалификационного раунда Лиги Чемпионов:")
    qual_tour(champions_second_round, champions_third_round, europe_third_round)
    ran.shuffle(champions_third_round)
    print("Результаты третьего квалификационного раунда Лиги Чемпионов:")
    qual_tour(champions_third_round, champions_fourth_round, europe_fourth_round)
    ran.shuffle(champions_fourth_round)
    print("Результаты квалификационного раунда плей-офф Лиги Чемпионов:")
    qual_tour(champions_fourth_round, champions_main_round, europe_main_round)
    print("Состав группового раунда Лиги Чемпионов:")
    print(champions_main_round)
    return champions_main_round
def europe_qual():
    ran.shuffle(europe_first_round)
    print("Результаты первого квалификационного раунда Лиги Европы:")
    qual_tour(europe_first_round, europe_second_round, conference_second_round)
    ran.shuffle(europe_second_round)
    print("Результаты второго квалификационного раунда Лиги Европы:")
    qual_tour(europe_second_round, europe_third_round, conference_third_round)
    ran.shuffle(europe_third_round)
    print("Результаты третьего квалификационного раунда Лиги Европы:")
    qual_tour(europe_third_round, europe_fourth_round, conference_fourth_round)
    ran.shuffle(europe_fourth_round)
    print("Результаты квалификационного раунда плей-офф Лиги Европы:")
    qual_tour(europe_fourth_round, europe_main_round, conference_main_round)
    print("Состав группового раунда Лиги Европы:")
    print(europe_main_round)
    return europe_main_round
def conference_qual():
    ran.shuffle(conference_first_round)
    print("Результаты первого квалификационного раунда Лиги Конференций:")
    qual_tour(conference_first_round, conference_second_round, pretenders_second_round)
    ran.shuffle(conference_second_round)
    print("Результаты второго квалификационного раунда Лиги Конференций:")
    qual_tour(conference_second_round, conference_third_round, pretenders_first_round)
    ran.shuffle(conference_third_round)
    print("Результаты третьего квалификационного раунда Лиги Конференций:")
    qual_tour(conference_third_round, conference_fourth_round, pretenders_first_round)
    ran.shuffle(conference_fourth_round)
    print("Результаты квалификационного раунда плей-офф Лиги Конференций:")
    qual_tour(conference_fourth_round, conference_main_round, off_pull)
    print("Состав группового раунда Лиги Конференций:")
    print(conference_main_round)
    return conference_main_round
def pretenders_qual():
    ran.shuffle(pretenders_first_round)
    print("Результаты первого квалификационного раунда Лиги Претендентов:")
    qual_tour(pretenders_first_round, off_pull, pretenders_second_round)
    ran.shuffle(pretenders_second_round)
    print("Результаты второго квалификационного раунда Лиги Претендентов:")
    qual_tour(pretenders_second_round, off_pull, pretenders_third_round)
    ran.shuffle(pretenders_third_round)
    print("Результаты третьего квалификационного раунда Лиги Претендентов:")
    qual_tour(pretenders_third_round, off_pull, pretenders_fourth_round)
    ran.shuffle(pretenders_fourth_round)
    print("Результаты квалификационного раунда плей-офф Лиги Претендентов:")
    qual_tour(pretenders_fourth_round, off_pull, pretenders_main_round)
    print("Состав группового раунда Лиги Претендентов:")
    print(pretenders_main_round)
    return pretenders_main_round