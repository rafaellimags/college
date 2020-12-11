# import pandas as pd

# paises = ['NOR', 'SWE', 'FIN']
# modalidades = ['Skiing', 'Curling', 'Skating', 'Ice Hockey']

# winter_medals = pd.read_csv('https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv')

# data = winter_medals.query("NOC in @paises and Sport in @modalidades and Year > 2000 and Medal == 'Gold'").groupby(['NOC']).count()

# m = data.sort_values(by=['Medal'], ascending=False).iloc[0]

# print(m)
