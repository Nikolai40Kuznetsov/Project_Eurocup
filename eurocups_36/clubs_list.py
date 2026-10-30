import pandas as pd
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
leagues = pd.DataFrame()
league_1 = albanian_league.df[['Клубы', "Евроочки"]]
league_2 = armenian_league.df[['Клубы', "Евроочки"]]
league_3 = austrian_league.df[['Клубы', "Евроочки"]]
league_4 = azerbaijanian_league.df[['Клубы', "Евроочки"]]
league_5 = belarussian_league.df[['Клубы', "Евроочки"]]
league_6 = belgian_league.df[['Клубы', "Евроочки"]]
league_7 = bosnian_league.df[['Клубы', "Евроочки"]]
league_8 = bulgarian_league.df[['Клубы', "Евроочки"]]
league_9 = croatian_league.df[['Клубы', "Евроочки"]]
league_10 = cypriot_league.df[['Клубы', "Евроочки"]]
league_11 = czech_league.df[['Клубы', "Евроочки"]]
league_12 = danish_league.df[['Клубы', "Евроочки"]]
league_13 = deutch_league.df[['Клубы', "Евроочки"]]
league_14 = dutch_league.df[['Клубы', "Евроочки"]]
league_15 = english_league.df[['Клубы', "Евроочки"]]
league_16 = estonian_league.df[['Клубы', "Евроочки"]]
league_17 = faroe_league.df[['Клубы', "Евроочки"]]
league_18 = finnish_league.df[['Клубы', "Евроочки"]]
league_19 = french_league.df[['Клубы', "Евроочки"]]
league_20 = georgian_league.df[['Клубы', "Евроочки"]]
league_21 = greek_league.df[['Клубы', "Евроочки"]]
league_22 = hungarian_league.df[['Клубы', "Евроочки"]]
league_23 = irish_league.df[['Клубы', "Евроочки"]]
league_24 = islandian_league.df[['Клубы', "Евроочки"]]
league_25 = italian_league.df[['Клубы', "Евроочки"]]
league_26 = jewish_league.df[['Клубы', "Евроочки"]]
league_27 = kazakh_league.df[['Клубы', "Евроочки"]]
league_28 = kosovar_league.df[['Клубы', "Евроочки"]]
league_29 = makedonian_league.df[['Клубы', "Евроочки"]]
league_30 = moldovan_league.df[['Клубы', "Евроочки"]]
league_31 = montenegrin_league.df[['Клубы', "Евроочки"]]
league_32 = norwegian_league.df[['Клубы', "Евроочки"]]
league_33 = polish_league.df[['Клубы', "Евроочки"]]
league_34 = portugese_league.df[['Клубы', "Евроочки"]]
league_35 = romanian_league.df[['Клубы', "Евроочки"]]
league_36 = russian_league.df[['Клубы', "Евроочки"]]
league_37 = scottish_league.df[['Клубы', "Евроочки"]]
league_38 = serbian_league.df[['Клубы', "Евроочки"]]
league_39 = slovakian_league.df[['Клубы', "Евроочки"]]
league_40 = slovenian_league.df[['Клубы', "Евроочки"]]
league_41 = spanish_league.df[['Клубы', "Евроочки"]]
league_42 = sweden_league.df[['Клубы', "Евроочки"]]
league_43 = swiss_league.df[['Клубы', "Евроочки"]]
league_44 = turkish_league.df[['Клубы', "Евроочки"]]
league_45 = ukrainian_league.df[['Клубы', "Евроочки"]]
bonus_clubs = {
    'Клубы': ["Вадуц", "Жальгирис", "Ларн",
               "Линкольн Ред Импс", "Ауда", "Виртус", 
               "Интер Эскальдес", "Расинг Юнион", "Хамрун Спартанс"],
    "Евроочки": ["8500", "12000", "9000", 
                 "13500", "4500", "4000", 
                 "7500", "3500", "8000"],
}
bonus_league = pd.DataFrame(bonus_clubs)
leagues = pd.concat([leagues, league_1], ignore_index=True)
leagues = pd.concat([leagues, league_2], ignore_index=True)
leagues = pd.concat([leagues, league_3], ignore_index=True)
leagues = pd.concat([leagues, league_4], ignore_index=True)
leagues = pd.concat([leagues, league_5], ignore_index=True)
leagues = pd.concat([leagues, league_6], ignore_index=True)
leagues = pd.concat([leagues, league_7], ignore_index=True)
leagues = pd.concat([leagues, league_8], ignore_index=True)
leagues = pd.concat([leagues, league_9], ignore_index=True)
leagues = pd.concat([leagues, league_10], ignore_index=True)
leagues = pd.concat([leagues, league_11], ignore_index=True)
leagues = pd.concat([leagues, league_12], ignore_index=True)
leagues = pd.concat([leagues, league_13], ignore_index=True)
leagues = pd.concat([leagues, league_14], ignore_index=True)
leagues = pd.concat([leagues, league_15], ignore_index=True)
leagues = pd.concat([leagues, league_16], ignore_index=True)
leagues = pd.concat([leagues, league_17], ignore_index=True)
leagues = pd.concat([leagues, league_18], ignore_index=True)
leagues = pd.concat([leagues, league_19], ignore_index=True)
leagues = pd.concat([leagues, league_20], ignore_index=True)
leagues = pd.concat([leagues, league_21], ignore_index=True)
leagues = pd.concat([leagues, league_22], ignore_index=True)
leagues = pd.concat([leagues, league_23], ignore_index=True)
leagues = pd.concat([leagues, league_24], ignore_index=True)
leagues = pd.concat([leagues, league_25], ignore_index=True)
leagues = pd.concat([leagues, league_26], ignore_index=True)
leagues = pd.concat([leagues, league_27], ignore_index=True)
leagues = pd.concat([leagues, league_28], ignore_index=True)
leagues = pd.concat([leagues, league_29], ignore_index=True)
leagues = pd.concat([leagues, league_30], ignore_index=True)
leagues = pd.concat([leagues, league_31], ignore_index=True)
leagues = pd.concat([leagues, league_32], ignore_index=True)
leagues = pd.concat([leagues, league_33], ignore_index=True)
leagues = pd.concat([leagues, league_34], ignore_index=True)
leagues = pd.concat([leagues, league_35], ignore_index=True)
leagues = pd.concat([leagues, league_36], ignore_index=True)
leagues = pd.concat([leagues, league_37], ignore_index=True)
leagues = pd.concat([leagues, league_38], ignore_index=True)
leagues = pd.concat([leagues, league_39], ignore_index=True)
leagues = pd.concat([leagues, league_40], ignore_index=True)
leagues = pd.concat([leagues, league_41], ignore_index=True)
leagues = pd.concat([leagues, league_42], ignore_index=True)
leagues = pd.concat([leagues, league_43], ignore_index=True)
leagues = pd.concat([leagues, league_44], ignore_index=True)
leagues = pd.concat([leagues, league_45], ignore_index=True)
leagues = pd.concat([leagues, bonus_league], ignore_index=True)
leagues["Евроочки"] = leagues["Евроочки"].astype(int)
leagues = leagues.sort_values(by=['Евроочки', 'Клубы'], ascending=False)
sorted_leagues = pd.DataFrame()
sorted_leagues = pd.concat([sorted_leagues, leagues], ignore_index=True)
print(sorted_leagues.to_string())