import games
import pandas as pd
finnish_league = {
    'Клубы': ["ХИК", "КуПС", "Интер Турку", "КТП",
              "ВПС", "Оулу", "Мариехамн", "Лахти",
              "СЙК", "Хака", "Ильвес", "Хонка"],
    'Евроочки': ["14000", "14000", "2000", "0",
                 "0", "0", "0", "0", 
                 "2500", "1000", "3500", "2500"], 
    'Очки силы': [10, 9, 7, 2,
                  5, 4, 3, 4,
                  8, 5, 7, 6],
    'Игры': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Победы': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Ничьи': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Поражения': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Очки': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Голов забито': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Голов пропущено': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Разница мячей': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}
games.play_league(4, 12, finnish_league)
df = pd.DataFrame(finnish_league)
df = df.sort_values(
    by=['Очки', 'Голов забито', 'Разница мячей'], 
    ascending=[False, False, False]
)
df = df.reset_index(drop=True)
df['Место'] = df.index + 1
# print(df)
cup_winner = games.play_cup(12, finnish_league)
def champions_qual():
    return df['Клубы'][0], df["Евроочки"][0]
def europe_qual():
    global cup_winner
    if cup_winner == (df['Клубы'][0], df["Евроочки"][0]) or cup_winner == (df['Клубы'][1], df["Евроочки"][1]):
        cup_winner = df['Клубы'][1], df["Евроочки"][1] 
    return cup_winner
def conference_qual():
    if cup_winner == (df['Клубы'][1], df["Евроочки"][1]):
        return df['Клубы'][2], df["Евроочки"][2]
    else:
        return df['Клубы'][1], df["Евроочки"][1]