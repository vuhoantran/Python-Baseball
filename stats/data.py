import os
import glob
import pandas as pd

# Python File Management
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE'))

# Sorting File Names
game_files.sort()

# Append Game Frames
game_frames = []

# Read CSV Files
for game_file in game_files:
    game_frame = pd.read_csv(game_file, names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)

# Concatenate DataFrames
games = pd.concat(game_frames)

# Clean Values
games.loc[games['multi5'] == '??', ['multi5']] = ''

# Extract Identifiers
identifiers = games['multi2'].str.extract(r'(.LS(\d{4})\d{5})')

# Forward Fill Identifiers
identifiers = identifiers.fillna(method='ffill')

# Rename Columns
identifiers.columns = ['game_id', 'year']

# Concatenate Identifier Columns
games = pd.concat([games, identifiers], axis=1, sort=False)

# Fill NaN Values
games = games.fillna(' ')

# Categorical Event Type
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

# Print DataFrame
print(games.head(5))
