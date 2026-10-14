"""
================================================================================
Practical Task: Develop a Simple Recommendation System
Domain: Movie Recommendation System
Technology: Python & Pandas
Description:
    This program creates and processes a dataset of movies using a Pandas DataFrame.
    It recommends the Top 3 or Top 5 movies based on multiple criteria:
    1. Overall Highest Rating (Global Top 5)
    2. User Genre Preference (Filtered Top 3 / Top 5)
    3. Weighted Score (Balancing Rating and Popularity/Votes)
================================================================================
"""

import os
import pandas as pd

def load_movie_dataset(csv_path="movies_dataset.csv"):
    """
    Loads movie dataset from CSV if available, or initializes from a built-in dictionary.
    Ensures the data is stored in a Pandas DataFrame.
    """
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        print(f"[INFO] Successfully loaded dataset from '{csv_path}'")
    else:
        # Fallback dataset with 15 movies (satisfies >= 10 items requirement)
        data = {
            "Movie_ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            "Title": [
                "Inception", "The Dark Knight", "Interstellar", "Parasite", "Spirited Away",
                "Avengers: Endgame", "The Shawshank Redemption", "Whiplash",
                "Spider-Man: Into the Spider-Verse", "The Matrix", "Gladiator", "Coco",
                "Forrest Gump", "Dune: Part Two", "La La Land"
            ],
            "Genre": [
                "Sci-Fi", "Action", "Sci-Fi", "Drama", "Animation",
                "Action", "Drama", "Drama", "Animation", "Sci-Fi",
                "Action", "Animation", "Drama", "Sci-Fi", "Romance"
            ],
            "Rating": [8.8, 9.0, 8.7, 8.5, 8.6, 8.4, 9.3, 8.5, 8.4, 8.7, 8.5, 8.4, 8.8, 8.6, 8.0],
            "Votes": [
                2400000, 2700000, 1900000, 850000, 790000,
                1180000, 2750000, 900000, 590000, 1950000,
                1530000, 530000, 2100000, 420000, 600000
            ],
            "Release_Year": [2010, 2008, 2014, 2019, 2001, 2019, 1994, 2014, 2018, 1999, 2000, 2017, 1994, 2024, 2016]
        }
        df = pd.DataFrame(data)
        print("[INFO] Loaded fallback embedded dataset into DataFrame.")
    return df


def display_dataset_overview(df):
    """
    Displays the dataset overview, shape, and first few records.
    """
    print("\n" + "=" * 70)
    print("                     MOVIE DATASET OVERVIEW")
    print("=" * 70)
    print(f"Total Movies in Dataset: {len(df)}")
    print(f"Columns / Attributes ({len(df.columns)}): {list(df.columns)}")
    print("\n--- First 5 Records ---")
    print(df.head().to_string(index=False))
    print("\n--- Summary Statistics (Rating & Votes) ---")
    print(df[["Rating", "Votes"]].describe().round(2).to_string())
    print("=" * 70)


def recommend_top_by_rating(df, top_n=5):
    """
    Criterion 1: Recommends Top N movies based on highest rating.
    Sorts by Rating (descending), using Votes as a secondary tie-breaker.
    """
    recommended = df.sort_values(by=["Rating", "Votes"], ascending=[False, False]).head(top_n)
    
    print("\n" + "=" * 70)
    print(f"       TOP {top_n} MOVIE RECOMMENDATIONS (CRITERION: HIGHEST RATING)")
    print("=" * 70)
    display_df = recommended[["Title", "Genre", "Rating", "Votes", "Release_Year"]].reset_index(drop=True)
    display_df.index = display_df.index + 1  # 1-based rank
    print(display_df.to_string())
    print("=" * 70)
    return recommended


def recommend_by_genre(df, user_genre="Sci-Fi", top_n=3):
    """
    Criterion 2: Recommends Top N movies filtered by user's preferred Genre.
    Filters by Genre, then sorts by Rating descending.
    """
    # Case-insensitive filtering
    filtered = df[df["Genre"].str.lower() == user_genre.strip().lower()]
    
    print("\n" + "=" * 70)
    print(f"   TOP {top_n} RECOMMENDATIONS FOR PREFERRED GENRE: '{user_genre.upper()}'")
    print("=" * 70)
    
    if filtered.empty:
        print(f"No movies found for genre '{user_genre}'. Available genres: {list(df['Genre'].unique())}")
        return filtered
    
    recommended = filtered.sort_values(by=["Rating", "Votes"], ascending=[False, False]).head(top_n)
    display_df = recommended[["Title", "Genre", "Rating", "Votes", "Release_Year"]].reset_index(drop=True)
    display_df.index = display_df.index + 1
    print(display_df.to_string())
    print("=" * 70)
    return recommended


def recommend_by_weighted_score(df, top_n=5):
    """
    Criterion 3: Recommends Top N movies using a Weighted Score (IMDb formula).
    Balances average rating and popularity (vote count).
    Formula:
        Weighted_Score = (v / (v + m)) * R + (m / (v + m)) * C
    where:
        R = individual movie rating
        v = number of votes for the movie
        m = minimum votes required to be listed (e.g., 25th percentile)
        C = mean rating across the whole dataset
    """
    C = df["Rating"].mean()
    m = df["Votes"].quantile(0.25)
    
    df_scored = df.copy()
    df_scored["Weighted_Score"] = (
        (df_scored["Votes"] / (df_scored["Votes"] + m)) * df_scored["Rating"] +
        (m / (df_scored["Votes"] + m)) * C
    ).round(2)
    
    recommended = df_scored.sort_values(by="Weighted_Score", ascending=False).head(top_n)
    
    print("\n" + "=" * 70)
    print(f"     TOP {top_n} RECOMMENDATIONS (CRITERION: WEIGHTED POPULARITY & RATING)")
    print("=" * 70)
    display_df = recommended[["Title", "Genre", "Rating", "Votes", "Weighted_Score"]].reset_index(drop=True)
    display_df.index = display_df.index + 1
    print(display_df.to_string())
    print("=" * 70)
    return recommended


def main():
    print("\n======================================================================")
    print("      WELCOME TO THE PANDAS-BASED MOVIE RECOMMENDATION SYSTEM")
    print("======================================================================")
    
    # Step 1 & 2: Load data into Pandas DataFrame
    df = load_movie_dataset()
    
    # Step 3: Display Dataset Overview
    display_dataset_overview(df)
    
    # Step 4 & 5: Apply Recommendation Criteria and Display Top 5
    # Criterion 1: Top 5 Highest Rated Movies
    recommend_top_by_rating(df, top_n=5)
    
    # Criterion 2: Genre-based recommendations (User Preference: Sci-Fi, Action, Animation)
    recommend_by_genre(df, user_genre="Sci-Fi", top_n=3)
    recommend_by_genre(df, user_genre="Animation", top_n=3)
    
    # Criterion 3: Top 5 by Weighted Score
    recommend_by_weighted_score(df, top_n=5)
    
    print("\n[SUCCESS] Recommendation System executed successfully!")


if __name__ == "__main__":
    main()
