import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import lib.utils.input_handler as ask
plt.switch_backend('TkAgg')

def line_column_chart(correlated_data, outcome_count, chart_type):
    outcomes = correlated_data.iloc[:, :outcome_count].copy()
    variables = correlated_data.iloc[:, outcome_count:].copy()

    if chart_type == 0:
        column_data = outcomes
        line_data = variables
    else:
        column_data = variables
        line_data = outcomes

    print('Plotting: %s' % ', '.join(map(str, outcomes.columns)),'...')

    # Plot and colour lines
    ax1 = line_data.plot(
        kind='line',
        linestyle='-', linewidth=len(outcomes.index) / 5,
        marker='o', markersize=4,
        figsize=(10, 6),
        zorder=2
    )
    cmap = cm.get_cmap('Blues')
    lines = [line for line in ax1.get_lines() if line.get_label().endswith('(neg)')]
    for count, line in enumerate(lines):
        line.set_linestyle('--')
        line.set_color(cmap(count + 0.3))

    ax2 = ax1.twinx()

    # Plot bars for each outcome column with offset if multiple outcomes
    bar_width = 0.3 / len(column_data.columns)
    for i, col in enumerate(column_data):
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
