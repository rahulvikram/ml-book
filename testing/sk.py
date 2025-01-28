# load data into pandas df
import pandas as pd
from sklearn.preprocessing import LabelBinarizer, LabelEncoder, OneHotEncoder
import seaborn as sns
import matplotlib.pyplot as plt

# keep track of original data while dropping missing values
original_data = pd.read_csv('C:/Users/rahul/Documents/ml-book/testing/test_data/imdb.csv')
original_data.dropna(axis=0, how='any', inplace=True)

# generate data copy for label encoding
data = original_data.copy()
# print(data.head())

# encode labels
encoder = LabelEncoder()
title = data['Title']
title_encoded = encoder.fit_transform(title)
print(title_encoded)

# rating vs gross worldwide
sns.set_theme(style="darkgrid", palette="flare")
plot_data = data[['Year', 'grossWorldWide']]
# print(plot_data.head())
sns.scatterplot(x='Year', y='grossWorldWide', data=plot_data)
plt.show()


