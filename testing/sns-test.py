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

# plot the data
sns.scatterplot(data=df, x='homeFinalScore', y='visitorFinalScore');
plt.show()