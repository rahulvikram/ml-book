import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns

# very simple ETL pipeline
# extract game data from our dataset
df = pd.read_csv("C:/Users/rahul/Documents/ml-book/testing/data/games.csv");

# transform the data: drop unnecessary columns
df.drop(['gameId', 'season', 'gameDate', 'gameTimeEastern'], axis=1, inplace=True);

# set the style
sns.set_style("darkgrid") 

# plot the data
sns.scatterplot(data=df,
                x='homeFinalScore',
                y='visitorFinalScore',
                hue='week',
                palette='viridis',
                );

plt.title("2022 NFL Weeks 1-9 Scores")
plt.xlabel("Home")
plt.ylabel("Away")

def label_point(x, y, val, ax):
    a = pd.concat({'x': x, 'y': y, 'val': val}, axis=1)
    for i, point in a.iterrows():
        if (point['x'] > 38 or point['y'] > 40 or point['x']-point['y'] > 20):
            ax.text(point['x']+.2, point['y'], str(point['val']), fontsize=6)

# concatenate the visitor and home team abbreviations, and label the points
label_text = df['visitorTeamAbbr'] + ' @ ' + df['homeTeamAbbr']
label_point(df['homeFinalScore'], df['visitorFinalScore'], label_text, plt.gca())

plt.show();