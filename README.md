# UEFA_Champions_League_Data_Analysis

# Football Team Performance Analysis

## Project Overview
This repository contains a comprehensive analysis of top European football teams' performance metrics. The analysis examines key statistics including matches played, wins, draws, losses, goals scored, and derived performance indicators to provide insights into team effectiveness and efficiency.

## Dataset Description
The dataset includes performance metrics for top European football clubs including Real Madrid, Bayern Munich, FC Barcelona, Manchester United, and Juventus. The data appears to be from major European competitions, potentially spanning multiple seasons.

Key metrics in the dataset:
- Team name
- Matches played
- Wins, draws, and losses
- Goals scored
- Goal difference
- Points earned

## Analysis Components

### 1. Data Preparation
- Data cleaning and validation
- Type conversion ensuring all numerical values are properly formatted
- Addition of derived metrics (win rate, goals per match, points per match)

### 2. Exploratory Data Analysis
- Statistical summary of team performance
- Distribution of key metrics
- Relationship between matches played and performance outcomes

### 3. Performance Metrics Analysis
- Team efficiency calculations
- Radar charts for multi-dimensional performance comparison
- Win-rate and goals-per-match analysis

### 4. Statistical Tests
- Regression analysis on the impact of experience (matches played) on performance
- Team performance comparisons
- Efficiency and consistency measurements

### 5. Interactive Dashboard
- Visualization tool for exploring team metrics
- Dynamic comparison of teams across different performance indicators
- Sortable statistics and graphical representations
### Visualizations
![Image](https://github.com/user-attachments/assets/d4de2f31-8485-45b6-8303-a3daa7264840)

![Image](https://github.com/user-attachments/assets/79b6768e-d4ae-4c77-b057-50be303fd99c)

![Image](https://github.com/user-attachments/assets/1d28684c-5bcf-4eff-a758-42014ce81e5a)

![Image](https://github.com/user-attachments/assets/6d473c44-f747-4e58-9434-9d36c3ae87b7)


## Key Findings

1. **Team Rankings**:
   - Real Madrid leads in total matches played (486), wins (291), and goal difference (533)
   - Bayern Munich demonstrates exceptional efficiency with win rates comparable to Real Madrid
   - FC Barcelona maintains strong performance metrics despite fewer matches played

2. **Performance Insights**:
   - Win rates range from approximately 51% to 60% among top teams
   - Goals per match averages vary from 1.59 (Juventus) to 2.21 (Real Madrid)
   - Points per match analysis shows Real Madrid and Bayern Munich with similar efficiency (~1.10)

3. **Statistical Correlations**:
   - Positive correlation between matches played and win rate
   - Strong relationship between goals per match and overall team success
   - Win-to-loss ratio highlights team dominance patterns

## Usage Instructions

### Requirements
- Python 3.7+
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy

### Installation
```bash
# Clone this repository
git clone https://github.com/yourusername/football-team-analysis.git

# Install required Python packages
pip install -r requirements.txt


### Running the Analysis
```bash
python src/data_preparation.py
python src/exploratory_analysis.py
python src/performance_metrics.py
python src/statistical_tests.py
```

## Dashboard Preview
The interactive dashboard provides dynamic visualization of team performance metrics, allowing users to:
- Compare teams across different performance indicators
- View rankings based on selected metrics
- Analyze efficiency and consistency patterns
- Access detailed team statistics

## Future Work
- Extend analysis to include more teams and leagues
- Add temporal analysis to track performance changes over seasons
- Incorporate player-level statistics to connect individual and team performance
- Implement predictive models for match outcomes based on historical performance

## Contributing
Contributions to extend or improve the analysis are welcome. Please feel free to submit pull requests or open issues with suggestions.

