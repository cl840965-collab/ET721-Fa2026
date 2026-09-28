"""
Claudio Lopez
Sep 28, 2026
Lab 7: API and Data Collection
"""
import pandas as pd
dict_ = {'a': [11,21,31],
         'b': [12,22,32]}
df = pd.DataFrame(dict_)
print(df.head())
print(df.mean())

from static import get_teams
nba_teams = get_teams()
print(f"First 2 teams: {nba_teams[:2]}")
df_teams = pd.DataFrame(nba_teams)
print(df_teams.head())
df_warriors = df_teams[df_teams["nickname"]=="Warriors"]
print(df_warriors)
id_warriors=df_warriors[['id']].values[0][0]
print(id_warriors)


import requests
url = "https://s3-api.us-geo.objectstorage.softlayer.net/cfcoursesdata/CognitiveClass/PY0101EN/Chapter%205/Labs/Golden_State.pkl"

file_name = "Golden_State.pkl"
print("\nDownloading external data")
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded complete")
else:
    print("Download failed.")

games = pd.read_pickle(file_name)
print("\nGames data from pickle file:")
print(games.head())

warriors_vs_raptors = games[games['MATCHUP'].str.contains('TOR')]
gsw_home_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' vs. ')]
gsw_away_vs_raptors = warriors_vs_raptors[warriors_vs_raptors['MATCHUP'].str.contains(' @ ')]

home_avg_plus = gsw_home_vs_raptors['PLUS_MINUS'].mean()
away_avg_plus = gsw_away_vs_raptors['PLUS_MINUS'].mean()
home_avg_pts = gsw_home_vs_raptors['PTS'].mean()
away_avg_pts = gsw_away_vs_raptors['PTS'].mean()

print(f"Warriors home average {home_avg_plus}")
print(f"Warriors away average {away_avg_plus}")

print("EXERCISE")
url1 = "https://datahub.io/core/english-premier-league/r/season-2324.csv" 

file_name1 = "epl_matches.csv"
response1 = requests.get(url1)
if response1.status_code == 200:
    with open(file_name1, 'wb') as f:
        f.write(response1.content)
    print(f"Downloaded complete")
else:
    print("Download failed.")

games1 = pd.read_csv(file_name1)
print(games1.head())

burnley_v_manc = games1[games1['HomeTeam'].str.contains('Burnley')]
f_burnley_v_manc = games1[games1['AwayTeam'].str.contains('Burnley')]
manc_v_burnley = games1[games1['HomeTeam'].str.contains('Man City')]
f_manc_v_burnley = games1[games1['AwayTeam'].str.contains('Man City')]

b_home_avg_plus = burnley_v_manc['FTHG'].mean()
b_away_avg_pts = f_burnley_v_manc['FTAG'].mean()
mc_away_avg_pts = f_manc_v_burnley['FTAG'].mean()
mc_home_avg_plus = manc_v_burnley['FTHG'].mean()
print(f"Burnley home average {b_home_avg_plus}")
print(f"Burnley away average {b_away_avg_pts}")
print(f"Man City home average {mc_home_avg_plus}")
print(f"Man City away average {mc_away_avg_pts}")

import matplotlib.pyplot as plt
metrics = ['FTAG', 'FTHG']
home_values = ['b_home_avg_plus', 'mc_home_avg_plus']
away_values = ['b_away_avg_pts', 'mc_away_avg_pts']

x = range(len(metrics))
bar_width = 0.35

plt.figure(figsize=(8, 5))
plt.bar([i - bar_width/2 for i in x], home_values, width = bar_width, label='Home', color='skyblue')
plt.bar([i + bar_width/2 for i in x], away_values, width = bar_width, label='Away', color='orange')

plt.xticks(x, metrics)
plt.title('Burnley vs Man City — Home vs Away Comparison')
plt.ylabel('Average Value')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show(block=True)
input("Press Enter to close...")