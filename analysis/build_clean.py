import pandas as pd
import numpy as np

SRC = "/home/user/UEFA_Champions_League_Data_Analysis_/UCL_AllTime_Performance_Table.csv"
raw = pd.read_csv(SRC)

def parse_gf(s):
    return int(str(s).split(":")[0])

df = pd.DataFrame()
df["rank_original"] = raw["#"]
df["team"] = raw["Team"].str.strip()
df["matches_played"] = raw["matches_played"].astype(int)
df["wins"] = raw["wins"].astype(int)
df["draws"] = raw["draws"].astype(int)
df["losses"] = raw["losses"].astype(int)
df["goal_difference"] = raw["goal_difference"].astype(int)

goals_field = raw["goals"].astype(str)
df["goals_for"] = goals_field.apply(parse_gf)
df["goals_against"] = df["goals_for"] - df["goal_difference"]

# flag rows where the raw "goals" text was corrupted by spreadsheet auto time-formatting
df["goals_field_was_corrupted"] = goals_field.str.count(":") == 2

# original "points" column in the source file is a byte-for-byte duplicate of
# goal_difference (verified: 354/354 rows match) -- not real competition points.
df["points_source_invalid"] = True
df["points"] = df["wins"] * 3 + df["draws"]  # standard 3-1-0 competition scoring

# sanity check matches_played
df["matches_check_ok"] = (df["wins"] + df["draws"] + df["losses"]) == df["matches_played"]

# ---- derived rate / efficiency measures ----
mp = df["matches_played"]
df["win_rate"] = (df["wins"] / mp).round(4)
df["draw_rate"] = (df["draws"] / mp).round(4)
df["loss_rate"] = (df["losses"] / mp).round(4)
df["points_per_match"] = (df["points"] / mp).round(4)
df["goals_for_per_match"] = (df["goals_for"] / mp).round(3)
df["goals_against_per_match"] = (df["goals_against"] / mp).round(3)
df["goal_diff_per_match"] = (df["goal_difference"] / mp).round(3)
df["win_loss_ratio"] = (df["wins"] / df["losses"].replace(0, np.nan)).round(3)
df["max_possible_points"] = mp * 3
df["points_efficiency_pct"] = (df["points"] / df["max_possible_points"] * 100).round(2)

# tier segmentation by experience (matches played)
def tier(m):
    if m >= 200:
        return "1 - Elite (200+ matches)"
    elif m >= 100:
        return "2 - Established (100-199)"
    elif m >= 50:
        return "3 - Emerging (50-99)"
    else:
        return "4 - Occasional (<50)"
df["experience_tier"] = mp.apply(tier)

# ranks by key measures (1 = best)
df["rank_by_points"] = df["points"].rank(ascending=False, method="min").astype(int)
df["rank_by_win_rate"] = df["win_rate"].rank(ascending=False, method="min").astype(int)
df["rank_by_goal_difference"] = df["goal_difference"].rank(ascending=False, method="min").astype(int)
df["rank_by_points_per_match"] = df["points_per_match"].rank(ascending=False, method="min").astype(int)

df = df.sort_values("points", ascending=False).reset_index(drop=True)
df.insert(0, "rank", df.index + 1)

out_csv = "/tmp/claude-0/-home-user-UEFA-Champions-League-Data-Analysis-/f95957cd-5ec0-5766-bdeb-9e1b993bfca2/scratchpad/ucl_clean.csv"
df.to_csv(out_csv, index=False)

print(df.shape)
print(df.head(15)[["rank","team","matches_played","wins","draws","losses","goals_for","goals_against","goal_difference","points","win_rate","points_per_match","experience_tier"]].to_string(index=False))
print("\nCorrupted goals field count:", df["goals_field_was_corrupted"].sum())
print("matches_check_ok all true:", df["matches_check_ok"].all())
