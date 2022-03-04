import pandas as pd
import matplotlib.pyplot as plt

from data import games

# Select All Plays
plays = games[games['type'] == 'play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

# Select Only Hits
hits = plays.loc[plays['event'].str.contains(r'^(?:S(?!B)|D|T|HR)'), ['inning', 'event']]

# Convert Column Type
hits.loc[:, 'inning'] = pd.to_numeric(hits.loc[:, 'inning'])

# Replace Dictionary
replacements = {
    r'^S(.*)': 'single',
    r'^D(.*)': 'double',
    r'^T(.*)': 'triple',
    r'^HR(.*)': 'hr'
}

# Replace Function
hit_type = hits['event'].replace(replacements, regex=True)

# Add A New Column
hits = hits.assign(hit_type=hit_type)

# Group By Inning and Hit Type
hits = hits.groupby(['inning', 'hit_type']).size().reset_index(name='count')

# Convert Hit Type to Categorical
hits['hit_type'] = pd.Categorical(hits['hit_type'], ['single', 'double', 'triple', 'hr'])

# Sort Values
hits = hits.sort_values(['inning', 'hit_type'])

# Reshape With Pivot
hits = hits.pivot(index='inning', columns='hit_type', values='count')

# Stacked Bar Plot
hits.plot.bar(stacked=True)

plt.show()

print(hits.head(30))
