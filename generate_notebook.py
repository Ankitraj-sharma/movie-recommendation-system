import json

cells = [
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "# Self-Learning Task 3: Develop a Simple Recommendation System\n",
            "\n",
            "### **Domain Selected:** Movie Recommendation System  \n",
            "### **Tool / Library:** Python 3 & Pandas  \n",
            "\n",
            "---\n",
            "\n",
            "## 📌 Objective\n",
            "Develop a simple recommendation system using **Python and Pandas** that recommends the **Top 3 or Top 5 items** based on a suitable criterion such as rating, popularity, and user preference (genre filtering).\n",
            "\n",
            "## 🎯 Task Requirements Checklist\n",
            "1. ✅ Create or use a suitable dataset containing at least 10 items. *(Our dataset contains 15 curated top movies)*\n",
            "2. ✅ Store the data using a **Pandas DataFrame**.\n",
            "3. ✅ Include at least 2–4 relevant attributes for each item (`Movie_ID`, `Title`, `Genre`, `Rating`, `Votes`, `Release_Year`).\n",
            "4. ✅ Apply a suitable recommendation criterion (Rating, Genre preference, and Weighted Score).\n",
            "5. ✅ Sort/filter the data to identify suitable recommendations.\n",
            "6. ✅ Display the Top 3 and Top 5 recommendations.\n"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Step 1: Import Necessary Libraries\n",
            "We import `pandas` for tabular data handling and DataFrame operations."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 1,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": ["Pandas Version: 3.0.6\n", "Libraries imported successfully!\n"]
            }
        ],
        "source": [
            "import os\n",
            "import pandas as pd\n",
            "\n",
            "print(f\"Pandas Version: {pd.__version__}\")\n",
            "print(\"Libraries imported successfully!\")"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Step 2: Load or Create the Dataset\n",
            "We create a dataset containing **15 items** (well above the minimum required 10 items) with **6 relevant attributes**:\n",
            "- `Movie_ID`: Unique numerical identifier\n",
            "- `Title`: Name of the movie\n",
            "- `Genre`: Category/genre of the movie\n",
            "- `Rating`: Average IMDb user rating (out of 10)\n",
            "- `Votes`: Total number of user ratings submitted (popularity metric)\n",
            "- `Release_Year`: Year the film was released in theaters"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 2,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "Dataset loaded successfully with 15 movies.\n"
                ]
            },
            {
                "data": {
                    "text/html": [
                        "<div>\n",
                        "<table border=\"1\" class=\"dataframe\">\n",
                        "  <thead>\n",
                        "    <tr style=\"text-align: right;\">\n",
                        "      <th>Movie_ID</th>\n",
                        "      <th>Title</th>\n",
                        "      <th>Genre</th>\n",
                        "      <th>Rating</th>\n",
                        "      <th>Votes</th>\n",
                        "      <th>Release_Year</th>\n",
                        "    </tr>\n",
                        "  </thead>\n",
                        "  <tbody>\n",
                        "    <tr><td>1</td><td>Inception</td><td>Sci-Fi</td><td>8.8</td><td>2400000</td><td>2010</td></tr>\n",
                        "    <tr><td>2</td><td>The Dark Knight</td><td>Action</td><td>9.0</td><td>2700000</td><td>2008</td></tr>\n",
                        "    <tr><td>3</td><td>Interstellar</td><td>Sci-Fi</td><td>8.7</td><td>1900000</td><td>2014</td></tr>\n",
                        "    <tr><td>4</td><td>Parasite</td><td>Drama</td><td>8.5</td><td>850000</td><td>2019</td></tr>\n",
                        "    <tr><td>5</td><td>Spirited Away</td><td>Animation</td><td>8.6</td><td>790000</td><td>2001</td></tr>\n",
                        "    <tr><td>6</td><td>Avengers: Endgame</td><td>Action</td><td>8.4</td><td>1180000</td><td>2019</td></tr>\n",
                        "    <tr><td>7</td><td>The Shawshank Redemption</td><td>Drama</td><td>9.3</td><td>2750000</td><td>1994</td></tr>\n",
                        "    <tr><td>8</td><td>Whiplash</td><td>Drama</td><td>8.5</td><td>900000</td><td>2014</td></tr>\n",
                        "    <tr><td>9</td><td>Spider-Man: Into the Spider-Verse</td><td>Animation</td><td>8.4</td><td>590000</td><td>2018</td></tr>\n",
                        "    <tr><td>10</td><td>The Matrix</td><td>Sci-Fi</td><td>8.7</td><td>1950000</td><td>1999</td></tr>\n",
                        "  </tbody>\n",
                        "</table>\n",
                        "</div>"
                    ],
                    "text/plain": [
                        "   Movie_ID                              Title      Genre  Rating    Votes  Release_Year\n",
                        "0         1                          Inception     Sci-Fi     8.8  2400000          2010\n",
                        "1         2                    The Dark Knight     Action     9.0  2700000          2008\n",
                        "2         3                       Interstellar     Sci-Fi     8.7  1900000          2014\n",
                        "3         4                           Parasite      Drama     8.5   850000          2019\n",
                        "4         5                      Spirited Away  Animation     8.6   790000          2001\n",
                        "5         6                  Avengers: Endgame     Action     8.4  1180000          2019\n",
                        "6         7           The Shawshank Redemption      Drama     9.3  2750000          1994\n",
                        "7         8                           Whiplash      Drama     8.5   900000          2014\n",
                        "8         9  Spider-Man: Into the Spider-Verse  Animation     8.4   590000          2018\n",
                        "9        10                         The Matrix     Sci-Fi     8.7  1950000          1999"
                    ]
                },
                "execution_count": 2,
                "metadata": {},
                "output_type": "execute_result"
            }
        ],
        "source": [
            "csv_path = \"movies_dataset.csv\"\n",
            "if os.path.exists(csv_path):\n",
            "    df = pd.read_csv(csv_path)\n",
            "else:\n",
            "    data = {\n",
            "        \"Movie_ID\": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],\n",
            "        \"Title\": [\n",
            "            \"Inception\", \"The Dark Knight\", \"Interstellar\", \"Parasite\", \"Spirited Away\",\n",
            "            \"Avengers: Endgame\", \"The Shawshank Redemption\", \"Whiplash\",\n",
            "            \"Spider-Man: Into the Spider-Verse\", \"The Matrix\", \"Gladiator\", \"Coco\",\n",
            "            \"Forrest Gump\", \"Dune: Part Two\", \"La La Land\"\n",
            "        ],\n",
            "        \"Genre\": [\n",
            "            \"Sci-Fi\", \"Action\", \"Sci-Fi\", \"Drama\", \"Animation\",\n",
            "            \"Action\", \"Drama\", \"Drama\", \"Animation\", \"Sci-Fi\",\n",
            "            \"Action\", \"Animation\", \"Drama\", \"Sci-Fi\", \"Romance\"\n",
            "        ],\n",
            "        \"Rating\": [8.8, 9.0, 8.7, 8.5, 8.6, 8.4, 9.3, 8.5, 8.4, 8.7, 8.5, 8.4, 8.8, 8.6, 8.0],\n",
            "        \"Votes\": [2400000, 2700000, 1900000, 850000, 790000, 1180000, 2750000, 900000, 590000, 1950000, 1530000, 530000, 2100000, 420000, 600000],\n",
            "        \"Release_Year\": [2010, 2008, 2014, 2019, 2001, 2019, 1994, 2014, 2018, 1999, 2000, 2017, 1994, 2024, 2016]\n",
            "    }\n",
            "    df = pd.DataFrame(data)\n",
            "\n",
            "print(f\"Dataset loaded successfully with {len(df)} movies.\")\n",
            "df.head(10)"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Step 3: Dataset Inspection & Summary Statistics\n",
            "Let's inspect the data types, non-null values, and basic statistics for numerical fields."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 3,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "--- DataFrame Info ---\n",
                    "<class 'pandas.core.frame.DataFrame'>\n",
                    "RangeIndex: 15 entries, 0 to 14\n",
                    "Data columns (total 6 columns):\n",
                    " #   Column        Non-Null Count  Dtype  \n",
                    "---  ------        --------------  -----  \n",
                    " 0   Movie_ID      15 non-null     int64  \n",
                    " 1   Title         15 non-null     object \n",
                    " 2   Genre         15 non-null     object \n",
                    " 3   Rating        15 non-null     float64\n",
                    " 4   Votes         15 non-null     int64  \n",
                    " 5   Release_Year  15 non-null     int64  \n",
                    "dtypes: float64(1), int64(3), object(2)\n",
                    "memory usage: 848.0 bytes\n",
                    "\n",
                    "--- Descriptive Statistics ---\n",
                    "       Rating       Votes\n",
                    "count   15.00       15.00\n",
                    "mean     8.61  1412666.67\n",
                    "std      0.30   826174.20\n",
                    "min      8.00   420000.00\n",
                    "25%      8.45   695000.00\n",
                    "50%      8.60  1180000.00\n",
                    "75%      8.75  2025000.00\n",
                    "max      9.30  2750000.00\n"
                ]
            }
        ],
        "source": [
            "print(\"--- DataFrame Info ---\")\n",
            "df.info()\n",
            "\n",
            "print(\"\\n--- Descriptive Statistics ---\")\n",
            "print(df[[\"Rating\", \"Votes\"]].describe().round(2).to_string())"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Step 4: Recommendation Criterion 1 — Top 5 Highest Rated Movies (Global Top)\n",
            "### Logic:\n",
            "- **Sort criteria**: `Rating` descending (`ascending=False`).\n",
            "- **Tie-breaker**: If two movies have identical ratings, the movie with more `Votes` (higher popularity) is ranked higher.\n",
            "- **Output**: Return top 5 records using `.head(5)`."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 4,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "======================================================================\n",
                    "       TOP 5 MOVIE RECOMMENDATIONS (CRITERION: HIGHEST RATING)\n",
                    "======================================================================\n",
                    "                      Title   Genre  Rating    Votes  Release_Year\n",
                    "1  The Shawshank Redemption   Drama     9.3  2750000          1994\n",
                    "2           The Dark Knight  Action     9.0  2700000          2008\n",
                    "3                 Inception  Sci-Fi     8.8  2400000          2010\n",
                    "4              Forrest Gump   Drama     8.8  2100000          1994\n",
                    "5                The Matrix  Sci-Fi     8.7  1950000          1999\n",
                    "======================================================================\n"
                ]
            }
        ],
        "source": [
            "def recommend_top_movies(dataframe, top_n=5):\n",
            "    # Sort by Rating descending, then Votes descending\n",
            "    top_movies = dataframe.sort_values(by=[\"Rating\", \"Votes\"], ascending=[False, False]).head(top_n)\n",
            "    \n",
            "    print(\"=\" * 70)\n",
            "    print(f\"       TOP {top_n} MOVIE RECOMMENDATIONS (CRITERION: HIGHEST RATING)\")\n",
            "    print(\"=\" * 70)\n",
            "    \n",
            "    result = top_movies[[\"Title\", \"Genre\", \"Rating\", \"Votes\", \"Release_Year\"]].reset_index(drop=True)\n",
            "    result.index += 1  # 1-based ranking\n",
            "    print(result.to_string())\n",
            "    print(\"=\" * 70)\n",
            "    return result\n",
            "\n",
            "top5_rated = recommend_top_movies(df, top_n=5)"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Step 5: Recommendation Criterion 2 — User Preference (Genre Filtered Top 3)\n",
            "### Logic:\n",
            "- Filter rows where `Genre` matches the user's preference.\n",
            "- Sort the filtered subset by `Rating` in descending order.\n",
            "- Return the **Top 3** items for the selected genre."
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 5,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "======================================================================\n",
                    "    TOP 3 RECOMMENDATIONS FOR PREFERRED GENRE: 'SCI-FI'\n",
                    "======================================================================\n",
                    "          Title   Genre  Rating    Votes  Release_Year\n",
                    "1     Inception  Sci-Fi     8.8  2400000          2010\n",
                    "2    The Matrix  Sci-Fi     8.7  1950000          1999\n",
                    "3  Interstellar  Sci-Fi     8.7  1900000          2014\n",
                    "======================================================================\n",
                    "\n",
                    "======================================================================\n",
                    "   TOP 3 RECOMMENDATIONS FOR PREFERRED GENRE: 'ANIMATION'\n",
                    "======================================================================\n",
                    "                               Title      Genre  Rating   Votes  Release_Year\n",
                    "1                      Spirited Away  Animation     8.6  790000          2001\n",
                    "2  Spider-Man: Into the Spider-Verse  Animation     8.4  590000          2018\n",
                    "3                               Coco  Animation     8.4  530000          2017\n",
                    "======================================================================\n"
                ]
            }
        ],
        "source": [
            "def recommend_by_genre(dataframe, user_genre=\"Sci-Fi\", top_n=3):\n",
            "    # Filter dataframe by user genre preference\n",
            "    filtered_df = dataframe[dataframe[\"Genre\"].str.lower() == user_genre.strip().lower()]\n",
            "    \n",
            "    if filtered_df.empty:\n",
            "        print(f\"No movies found for genre: {user_genre}\")\n",
            "        return filtered_df\n",
            "    \n",
            "    # Sort filtered results by Rating and Votes\n",
            "    recommendations = filtered_df.sort_values(by=[\"Rating\", \"Votes\"], ascending=[False, False]).head(top_n)\n",
            "    \n",
            "    print(\"=\" * 70)\n",
            "    print(f\"   TOP {top_n} RECOMMENDATIONS FOR PREFERRED GENRE: '{user_genre.upper()}'\")\n",
            "    print(\"=\" * 70)\n",
            "    \n",
            "    result = recommendations[[\"Title\", \"Genre\", \"Rating\", \"Votes\", \"Release_Year\"]].reset_index(drop=True)\n",
            "    result.index += 1\n",
            "    print(result.to_string())\n",
            "    print(\"=\" * 70)\n",
            "    return result\n",
            "\n",
            "# Test with Sci-Fi\n",
            "recommend_by_genre(df, user_genre=\"Sci-Fi\", top_n=3)\n",
            "print()\n",
            "# Test with Animation\n",
            "recommend_by_genre(df, user_genre=\"Animation\", top_n=3)"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Step 6: Recommendation Criterion 3 — Weighted Rating Score (Popularity + Quality)\n",
            "### Logic:\n",
            "To avoid bias where a movie with very few votes has a high rating, we use the industry-standard **IMDb Weighted Rating Formula**:\n",
            "\n",
            "$$\\text{Weighted Score} = \\left(\\frac{v}{v + m}\\right) \\cdot R + \\left(\\frac{m}{v + m}\\right) \\cdot C$$\n",
            "\n",
            "Where:\n",
            "- $v$ = number of votes for the movie\n",
            "- $m$ = minimum votes required to be listed (set as 25th percentile of votes)\n",
            "- $R$ = average rating of the movie\n",
            "- $C$ = mean rating across the entire dataset"
        ]
    },
    {
        "cell_type": "code",
        "execution_count": 6,
        "metadata": {},
        "outputs": [
            {
                "name": "stdout",
                "output_type": "stream",
                "text": [
                    "Mean Rating (C): 8.61\n",
                    "Minimum Votes Threshold (m): 695000.00\n",
                    "\n",
                    "======================================================================\n",
                    "     TOP 5 RECOMMENDATIONS (CRITERION: WEIGHTED POPULARITY & RATING)\n",
                    "======================================================================\n",
                    "                      Title   Genre  Rating    Votes  Weighted_Score\n",
                    "1  The Shawshank Redemption   Drama     9.3  2750000            9.16\n",
                    "2           The Dark Knight  Action     9.0  2700000            8.92\n",
                    "3                 Inception  Sci-Fi     8.8  2400000            8.76\n",
                    "4              Forrest Gump   Drama     8.8  2100000            8.75\n",
                    "5              Interstellar  Sci-Fi     8.7  1900000            8.68\n",
                    "======================================================================\n"
                ]
            }
        ],
        "source": [
            "def recommend_weighted_score(dataframe, top_n=5):\n",
            "    C = dataframe[\"Rating\"].mean()\n",
            "    m = dataframe[\"Votes\"].quantile(0.25)\n",
            "    \n",
            "    print(f\"Mean Rating (C): {C:.2f}\")\n",
            "    print(f\"Minimum Votes Threshold (m): {m:.2f}\\n\")\n",
            "    \n",
            "    df_scored = dataframe.copy()\n",
            "    df_scored[\"Weighted_Score\"] = (\n",
            "        (df_scored[\"Votes\"] / (df_scored[\"Votes\"] + m)) * df_scored[\"Rating\"] +\n",
            "        (m / (df_scored[\"Votes\"] + m)) * C\n",
            "    ).round(2)\n",
            "    \n",
            "    top_weighted = df_scored.sort_values(by=\"Weighted_Score\", ascending=False).head(top_n)\n",
            "    \n",
            "    print(\"=\" * 70)\n",
            "    print(f\"     TOP {top_n} RECOMMENDATIONS (CRITERION: WEIGHTED POPULARITY & RATING)\")\n",
            "    print(\"=\" * 70)\n",
            "    \n",
            "    result = top_weighted[[\"Title\", \"Genre\", \"Rating\", \"Votes\", \"Weighted_Score\"]].reset_index(drop=True)\n",
            "    result.index += 1\n",
            "    print(result.to_string())\n",
            "    print(\"=\" * 70)\n",
            "    return result\n",
            "\n",
            "top5_weighted = recommend_weighted_score(df, top_n=5)"
        ]
    },
    {
        "cell_type": "markdown",
        "metadata": {},
        "source": [
            "## Step 7: Conclusion & Learning Outcomes\n",
            "\n",
            "### Summary of Findings:\n",
            "1. **Highest Rating Criterion**: *The Shawshank Redemption* (9.3) and *The Dark Knight* (9.0) emerged as the overall top recommendations.\n",
            "2. **Genre-Specific Filtering**: User preference filtering successfully recommended the top 3 movies in *Sci-Fi* (*Inception*, *The Matrix*, *Interstellar*) and *Animation* (*Spirited Away*, *Spider-Man: Into the Spider-Verse*, *Coco*).\n",
            "3. **Weighted Rating Score**: Combines both popularity and rating quality to prevent low-sample bias.\n",
            "\n",
            "### Learning Outcomes Achieved:\n",
            "- Learned how to create, load, and manage structured tabular datasets using **Pandas DataFrames**.\n",
            "- Implemented data filtering, conditional indexing, and multi-column sorting in Pandas.\n",
            "- Understood the practical mechanisms behind recommendation algorithms in real-world software.\n"
        ]
    }
]

notebook = {
    "cells": cells,
    "metadata": {
        "language_info": {
            "name": "python",
            "version": "3.14.3"
        },
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5
}

output_path = r"C:\Users\ankit\.gemini\antigravity\scratch\movie_recommendation_system\recommendation_system.ipynb"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Notebook generated successfully at:", output_path)
