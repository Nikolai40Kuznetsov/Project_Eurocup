import games
import pandas as pd
croatian_league = {
    'Клубы': ["Динамо Загреб", "Горица", "Хайдук Сплит", "Риека", "Истра",
              "Осиек", "Славен Белупо", "Шибеник", "Вараждин", "Локомотива Загреб"],
    'Евроочки': ["44000", "0", "10000", "15000", "0",
                 "7500", "0", "0", "1500", "0"], 
    'Очки силы': [10, 4, 9, 9, 5,
                  5, 6, 3, 6, 5],
    'Игры': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Победы': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Ничьи': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Поражения': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Очки': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Голов забито': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Голов пропущено': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Разница мячей': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}
games.play_league(4, 10, croatian_league)
df = pd.DataFrame(croatian_league)
df = df.sort_values(
    by=['Очки', 'Голов забито', 'Разница мячей'], 
    ascending=[False, False, False]
)
df = df.reset_index(drop=True)
df['Место'] = df.index + 1
# print(df)
cup_winner = games.play_cup(10, croatian_league)
def champions_qual():
    return df['Клубы'][0], df["Евроочки"][0]
def europe_qual():
    global cup_winner
    if cup_winner == (df['Клубы'][0], df["Евроочки"][0]) or cup_winner == (df['Клубы'][1], df["Евроочки"][1]):
        cup_winner = df['Клубы'][1], df["Евроочки"][1] 
    return cup_winner
def conference_qual_1():
    if cup_winner == (df['Клубы'][1], df["Евроочки"][1]):
        return df['Клубы'][2], df["Евроочки"][2]
    else:
        return df['Клубы'][1], df["Евроочки"][1]
def conference_qual_2():
    if conference_qual_1() == (df['Клубы'][2], df["Евроочки"][2]):
        return df['Клубы'][3], df["Евроочки"][3]
    else:
        return df['Клубы'][2], df["Евроочки"][2]
