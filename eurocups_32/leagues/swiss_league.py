import games
import random as ran
import pandas as pd
swiss_league = {
    'Клубы': ["Базель", "Серветт", "Янг Бойз", "Люцерн",
              "Лугано", "Лозанна-Спорт", "Санкт-Галлен", "Сьон",
              "Грассхоппер", "Цюрих", "Ивердон", "Винтертур"],
    'Евроочки': ["34500", "12500", "29500", "4000",
                 "21250", "10000", "4000", "0", 
                 "0", "5000", "0", "0"], 
    'Очки силы': [8, 7, 10, 6,
                  6, 5, 6, 4,
                  4, 5, 4, 4],
    'Игры': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Победы': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Ничьи': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Поражения': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Очки': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Голов забито': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Голов пропущено': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Разница мячей': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}
games.play_league(4, 12, swiss_league)
df = pd.DataFrame(swiss_league)
df = df.sort_values(
    by=['Очки', 'Голов забито', 'Разница мячей'], 
    ascending=[False, False, False]
)
df = df.reset_index(drop=True)
df['Место'] = df.index + 1
# print(df)
cup_winner = games.play_cup(12, swiss_league)
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