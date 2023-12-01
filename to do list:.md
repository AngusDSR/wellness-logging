Nutrition tracker to do list:
- find a way to show correlations with different columns
- colour blind friendly colour scheme
- stacked histogram for rolling average of intakes: https://seaborn.pydata.org/examples/histogram_stacked.html
- clarify positive and negative correlations - in which direction
- turn times into AM, PM, ALL DAY and aggregate by those.
  - Allocate a number for each 0 all day, then only agregate with rows with a number higher than self. E.g. 0 day can agregate with all, PM only with PM, etc.
- More each nutrient or intake, calculate average and allocate a number 0-10/0-3 for high medium/low etc and then turn these into factors
- remove the method on 'default'
- create an app file and ask which chart we want to make/what analysis
- make prettier (remove frame, make bigger) and full screen
- copy over date from work stuff (delete from folder)
- research effect of cumulative nutritients
- pass cleaned data into library in data module (data.inputs.nutrition, data.outcomes.health, etc.)
- groupings of factors: what are the common (5) facotrs at play on days with abkvw average mood energy whatever
- add back and restart to menus
- find a way to differenciate between negative and positive correlations
- add max averaging of days based on realistic range of dates
- negative correlations highlgihted better, should appear to pull it down somehow or be below the x axis?
- After splitting days into sections: showing key wellbeing outcomes over time https://images.app.goo.gl/aXCW2AeiwLF1MVqSA
- Add a stacked column chart with different outcomes stacked per column: https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html
- add curves to lines
- count gratitudes
- bring in Trello data
<!-- - bring in Weather data: https://meteostat.net/en/place/gb/new-cross?s=03779&t=2023-11-01/2023-11-30 -->
- bring in Spotify data: https://towardsdatascience.com/get-your-spotify-streaming-history-with-python-d5a208bbcbd3

<!-- project_folder/
│
├── lib/
│   ├── __init__.py
│   ├── data_processing/
│   │   ├── __init__.py
│   │   └── data_combiner.py
│   │   └── data.py
│   │   └── bearable_data.py
│   │   └── nutrition_data.py
│   │
│   ├── utils/
│   |   ├── __init__.py
│   |   └── input_handler.py
│   |
│   └── visualization/
│       ├── __init__.py
│       └── plotter.py
│
├── data/
|   ├── bearable-export-01-12-2023.csv
|   └── dailysummary.csv
|
└── interface.py -->
