import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')  # to get seaborn scatter plot

# read the csv file to extract data

data = pd.read_csv('Label_Set_Finance -Correlation.csv')
x_value = data['Movie_actor_3_credit']
gross = data['Movie_ratings']

plt.scatter(x_value, gross, s=25, alpha=0.6, edgecolor='black', linewidth=1)

plt.title('Director awards vs Movie rating')
plt.xlabel('Movie_actor_3_credit')
plt.ylabel('Movie_ratings')

plt.tight_layout()
plt.show()
plt.savefig('p.png')
