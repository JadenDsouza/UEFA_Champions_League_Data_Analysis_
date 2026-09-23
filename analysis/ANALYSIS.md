# Dashboard Measures — Analysis Notes

Source: `UCL_AllTime_Performance_Table.csv` (354 clubs, all-time UEFA Champions League / European Cup records).

## Data quality issues found & fixed

1. **`points` column is invalid.** Every row's `points` value is an exact duplicate
   of `goal_difference` (354/354 rows match) — a source export error, not real
   competition points. Fixed by recomputing `points = wins*3 + draws` (standard
   3/1/0 scoring).
2. **`goals` column corrupted for 113 clubs.** For the most historically prominent
   clubs (Real Madrid, Bayern Munich, Barcelona, Man Utd, Juventus, Liverpool,
   Porto, Benfica, and more), spreadsheet software auto-converted the `goals`
   field into a time value (e.g. `"1076:55:00"`), corrupting Goals Against.
   Goals For survived. Fixed by recalculating
   `goals_against = goals_for - goal_difference` (goal_difference itself checks
   out against the 241 unaffected rows and produces realistic goals-against
   figures for the rest).
3. Two rows (Linfield FC, 1. FC Frankfurt (Oder)) have `wins+draws+losses` off by
   1 from `matches_played` — left as-is, flagged via `matches_check_ok`.

`build_clean.py` reproduces `UCL_Cleaned_Performance_Data.csv` from the original source.

## Deliverables

- **`UCL_Cleaned_Performance_Data.csv`** — cleaned fact table with all derived measures.
- **`UCL_Dashboard_Measures.xlsx`** — the same data as a dashboard-ready workbook:
  `Fact_Team_Performance` (main table), `Measures` (formula catalog), `Top10_Tables`,
  `Tier_Summary`, `Long_Format` (tidy, for pivot/BI tools), and a `ReadMe` tab.
- **`UCL_Dashboard.html`** — a working interactive dashboard (filters, Top-15 points
  chart, win-rate vs. goals scatter, tier cards, sortable club table). Open directly
  in a browser, or use as a template for a BI tool.

## Key measures

| Measure | Formula |
|---|---|
| Win / Draw / Loss rate | wins (or draws/losses) / matches_played |
| Points | wins×3 + draws |
| Points per match | points / matches_played |
| Points efficiency % | points / (matches_played×3) |
| Goals for/against per match | goals_for (or goals_against) / matches_played |
| Goal diff per match | goal_difference / matches_played |
| Win/loss ratio | wins / losses |
| Experience tier | Elite 200+ / Established 100–199 / Emerging 50–99 / Occasional <50 matches |

## Headline findings

- Real Madrid leads on every major measure: 958 pts, 533 goal difference, 59.9% win rate over 486 matches.
- Only 11 clubs (3.1%) reach "Elite" tier (200+ matches); they average a 51.6% win rate, well above the tournament-wide baseline.
- Win rate and points-per-match track closely for top clubs, but attacking output (goals/match) separates "efficient" clubs (high win rate, moderate goals) from "expansive" ones (high goals, lower win rate) — see the Efficiency scatter in the dashboard.
