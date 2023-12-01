import pandas as pd
import matplotlib.pyplot as plt
from lib.data_processing.data_combiner import df, outcome_count
import lib.utils.input_handler as ask
plt.switch_backend('TkAgg')

outcomes = df[df.columns[:outcome_count]]
nutrients = df[df.columns[outcome_count:]]
nutrient_count = len(nutrients.columns)

print(nutrient_count)

# Plot 2-y-axes chart: excluding any blank rows (from averaging)
blank_rows_from_averaging = nutrients[nutrients.isnull().any(axis=1)].shape[0]

# DEBUG
# DEBUG
chart_type = ask.asker('Put outcomes as columns or as lines?:', ['columns', 'lines'])
if chart_type == 'columns':
    viz_columns = outcomes.columns
    viz_lines = nutrients[blank_rows_from_averaging:]
# DEBUG

print('Plotting: %s' % ', '.join(map(str, outcomes.columns)),'...')

# Plot lines axes
# DEBUG
# ax1 = nutrients[blank_rows_from_averaging:].plot(
ax1 = viz_lines.plot(
    kind='line',
    linestyle='-', linewidth=2,
    marker='o', markersize=4,
    figsize=(10, 6),
    zorder=2
)
# Add color mapping to lines
# DEBUG - PAUSE FOR NOW
input('Negative colouring on pause for debug')
for line in ax1.get_lines():
    if line.get_label().endswith('(neg)'):
        line.set_linestyle('--')
        line.set_color('blue')

ax2 = ax1.twinx()

# Plot bars for each outcome column with offset if multiple outcomes
bar_width = 0.3 / outcome_count
offset = bar_width / 2

# DEBUG
# for i, col in enumerate(outcomes.columns):
for i, col in enumerate(viz_columns):
    current_offset = (i - (outcome_count - 1) / 2) * bar_width  # Distribute bars evenly
    ax2.bar(df.index + pd.DateOffset(days=current_offset), outcomes[col], alpha=0.5, label=col, width=bar_width, zorder=1)

# Set a half-day offset for the x-axis limits
half_day_offset = pd.DateOffset(hours=12)
ax1.set_xlim(df.index.min() - half_day_offset, df.index[-1] + half_day_offset)
ax2.set_xlim(df.index.min() - half_day_offset, df.index[-1] + half_day_offset)

# set labels and legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.set_title(f'Nutritional intakes vs {", ".join(outcomes)} over time')
ax1.set_xlabel('')
ax1.set_ylabel('')
ax2.set_ylabel('')
ax1.set_yticklabels([])
ax2.set_yticklabels([])
ax1.tick_params(axis='y', which='both', left=False, right=False)
ax2.tick_params(axis='y', which='both', left=False, right=False)

plt.show()
