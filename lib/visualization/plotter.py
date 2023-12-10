import pandas as pd
import matplotlib.pyplot as plt
from lib.data_processing.data_utils import sets, outcome_count
import lib.utils.input_handler as ask
plt.switch_backend('TkAgg')

def line_column_chart(correlated_data, outcome_count):
    outcomes = correlated_data.iloc[:, :outcome_count].copy()
    variables = correlated_data.iloc[:, outcome_count:].copy()

    chart_type = ask.for_single_input(['columns', 'lines'], 'Put outcomes as columns or as lines?:')
    if chart_type == 0:
        viz_columns = outcomes
        viz_lines = variables
    else:
        viz_columns = variables
        viz_lines = outcomes

    print('Plotting: %s' % ', '.join(map(str, outcomes.columns)),'...')

    ax1 = viz_lines.plot(
        kind='line',
        linestyle='-', linewidth=2,
        marker='o', markersize=4,
        figsize=(10, 6),
        zorder=2
    )

    # Add color mapping to lines
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
        ax2.bar(outcomes.index + pd.DateOffset(days=current_offset), outcomes[col], alpha=0.5, label=col, width=bar_width, zorder=1)

    # Set a half-day offset for the x-axis limits
    half_day_offset = pd.DateOffset(hours=12)
    ax1.set_xlim(outcomes.index.min() - half_day_offset, outcomes.index[-1] + half_day_offset)
    ax2.set_xlim(outcomes.index.min() - half_day_offset, outcomes.index[-1] + half_day_offset)

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

def visualise():
    plt.show()
