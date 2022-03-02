import pandas as pd

import matplotlib.pyplot as plt

from data import games

# Select Attendance
attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'), ['year', 'multi3']]

# Column Labels
attendance.columns = ['year', 'attendance']

# Convert to Numeric
attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])

# Plot DataFrame
attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')

# Axis Labels
plt.xlabel('Year')
plt.ylabel('Attendance')

# Mean Line
plt.axhline(y=attendance['attendance'].mean(), label='Mean', color='green', linestyle='--')

plt.show()


