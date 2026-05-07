import games
import pandas as pd
slovenian_league = {
    'Клубы': ["Олимпия Любляна", "Мура", "Нафта", "Марибор", "Целе",
              "Приморье", "Домжале", "Радомлье", "НК Браво", "Копер"],
    'Евроочки': ["18375", "4000", "0", "10000", "20500",
                 "0", "3000", "0", "1500", "3000"], 
    'Очки силы': [10, 7, 3, 8, 9,
                  2, 5, 5, 6, 4],
    'Игры': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Победы': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Ничьи': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Поражения': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Очки': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Голов забито': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Голов пропущено': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Разница мячей': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
}
games.play_league(4, 10, slovenian_league)
df = pd.DataFrame(slovenian_league)
df = df.sort_values(
    by=['Очки', 'Голов забито', 'Разница мячей'], 
    ascending=[False, False, False]
)
df = df.reset_index(drop=True)
df['Место'] = df.index + 1
# print(df)
cup_winner = games.play_cup(10, slovenian_league)
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