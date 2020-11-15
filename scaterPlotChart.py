import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')  # to get seaborn scatter plot

# read the csv file to extract data

data = pd.read_csv('Label_Set_Finance - Sheet1.csv')
x_value = data['Budget']
gross = data['Movie_ratings']

plt.scatter(x_value, gross, s=25, alpha=0.6, edgecolor='black', linewidth=1)

plt.title('Trending Videos')
plt.xlabel('Budget')
plt.ylabel('Movie_ratings')

plt.tight_layout()
plt.show()
plt.savefig('p.png')
