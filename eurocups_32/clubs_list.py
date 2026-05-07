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
leagues = pd.concat([leagues, league_1], ignore_index=True)
leagues = pd.concat([leagues, league_2], ignore_index=True)
leagues = leagues.sort_values(by='Евроочки', ascending=False)
sorted_leagues = pd.DataFrame()
sorted_leagues = pd.concat([sorted_leagues, leagues], ignore_index=True)
print(sorted_leagues)