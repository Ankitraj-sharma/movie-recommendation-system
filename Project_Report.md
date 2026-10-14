# Self-Learning Task 3: Develop a Simple Recommendation System
## Project Report: Movie Recommendation System

---

### **Student & Task Information**
- **Course / Practical**: Practical 11 - Recommendation Systems
- **Task**: Self-Learning Task 3
- **Application Domain**: Movie Recommendation System
- **Implementation Language**: Python 3
- **Core Library**: Pandas (`pandas.DataFrame`)

---

## 1. Problem Selected

### **Domain**: Movie Recommendation System
In today's digital streaming era (e.g., Netflix, Amazon Prime, Disney+), users face choice overload when browsing through thousands of movies. A **Recommendation System** helps users discover movies matching their tastes by filtering and ranking items based on historical ratings, popularity, and specific preferences (like genre).

### **Objective**
The objective of this project is to develop a functional recommendation system using **Python and Pandas** that:
1. Represents structured movie data in a `pandas.DataFrame`.
2. Applies various recommendation criteria (Highest Rating, User Genre Preference, and Weighted Rating Score).
3. Sorts and filters the dataset to present the **Top 3 or Top 5** recommendations.

---

## 2. Dataset Description

The dataset was constructed and stored as a structured CSV file (`movies_dataset.csv`). It contains **15 items** (exceeding the required minimum of 10 items) and **6 relevant attributes** per movie (exceeding the required 2–4 attributes).

### **Attributes / Features:**
| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `Movie_ID` | Integer (`int64`) | Unique numeric identifier for each movie. |
| `Title` | String (`object`) | The official title of the movie. |
| `Genre` | String (`object`) | Primary genre category (e.g., Sci-Fi, Action, Drama, Animation, Romance). |
| `Rating` | Float (`float64`) | Average viewer score on a scale from 1.0 to 10.0 (IMDb metric). |
| `Votes` | Integer (`int64`) | Total count of user ratings submitted (proxy for popularity). |
| `Release_Year` | Integer (`int64`) | The calendar year in which the movie was released. |

### **Dataset Records (15 Movies):**
| Movie_ID | Title | Genre | Rating | Votes | Release_Year |
| :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | Inception | Sci-Fi | 8.8 | 2,400,000 | 2010 |
| 2 | The Dark Knight | Action | 9.0 | 2,700,000 | 2008 |
| 3 | Interstellar | Sci-Fi | 8.7 | 1,900,000 | 2014 |
| 4 | Parasite | Drama | 8.5 | 850,000 | 2019 |
| 5 | Spirited Away | Animation | 8.6 | 790,000 | 2001 |
| 6 | Avengers: Endgame | Action | 8.4 | 1,180,000 | 2019 |
| 7 | The Shawshank Redemption | Drama | 9.3 | 2,750,000 | 1994 |
| 8 | Whiplash | Drama | 8.5 | 900,000 | 2014 |
| 9 | Spider-Man: Into the Spider-Verse | Animation | 8.4 | 590,000 | 2018 |
| 10 | The Matrix | Sci-Fi | 8.7 | 1,950,000 | 1999 |
| 11 | Gladiator | Action | 8.5 | 1,530,000 | 2000 |
| 12 | Coco | Animation | 8.4 | 530,000 | 2017 |
| 13 | Forrest Gump | Drama | 8.8 | 2,100,000 | 1994 |
| 14 | Dune: Part Two | Sci-Fi | 8.6 | 420,000 | 2024 |
| 15 | La La Land | Romance | 8.0 | 600,000 | 2016 |

---

## 3. Recommendation Logic

To fulfill the requirements, three distinct recommendation criteria were implemented using Pandas operations:

### **Criterion 1: Highest Rating (Global Top 5)**
- **Methodology**: Sorts the entire DataFrame in descending order of `Rating`. In the event of ties between two movies with identical ratings, `Votes` is used as a secondary descending sort key.
- **Pandas Operation**:
  ```python
  df.sort_values(by=["Rating", "Votes"], ascending=[False, False]).head(5)
  ```

### **Criterion 2: User Preference Filter by Genre (Top 3 Recommendations)**
- **Methodology**: Accepts the user's preferred genre (e.g., "Sci-Fi" or "Animation"), filters the DataFrame using conditional boolean indexing, and sorts the filtered subset by `Rating` descending.
- **Pandas Operation**:
  ```python
  filtered = df[df["Genre"].str.lower() == user_genre.lower()]
  top_recommendations = filtered.sort_values(by=["Rating", "Votes"], ascending=[False, False]).head(3)
  ```

### **Criterion 3: Weighted Rating Score (Popularity + Rating Balance)**
- **Methodology**: Uses the industry-standard formula (IMDb weighted formula) to prevent bias towards titles with high ratings but very few votes.
- **Formula**:
  $$\text{Weighted Score} = \left(\frac{v}{v + m}\right) \cdot R + \left(\frac{m}{v + m}\right) \cdot C$$
  - $R$ = Individual movie rating
  - $v$ = Number of votes for the movie
  - $m$ = Minimum votes threshold (25th percentile of votes = 695,000)
  - $C$ = Mean rating across the entire dataset ($8.61$)
- **Pandas Operation**:
  ```python
  df["Weighted_Score"] = ((df["Votes"] / (df["Votes"] + m)) * df["Rating"] + (m / (df["Votes"] + m)) * C).round(2)
  top_weighted = df.sort_values(by="Weighted_Score", ascending=False).head(5)
  ```

---

## 4. Sample Output

### **A. Dataset Overview & Statistics**
```text
Total Movies in Dataset: 15
Columns / Attributes (6): ['Movie_ID', 'Title', 'Genre', 'Rating', 'Votes', 'Release_Year']

--- Summary Statistics ---
       Rating       Votes
count   15.00       15.00
mean     8.61  1412666.67
std      0.30   826174.20
min      8.00   420000.00
25%      8.45   695000.00
50%      8.60  1180000.00
75%      8.75  2025000.00
max      9.30  2750000.00
```

### **B. Output 1: Top 5 Recommendations by Highest Rating**
| Rank | Title | Genre | Rating | Votes | Release_Year |
| :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | The Shawshank Redemption | Drama | 9.3 | 2,750,000 | 1994 |
| 2 | The Dark Knight | Action | 9.0 | 2,700,000 | 2008 |
| 3 | Inception | Sci-Fi | 8.8 | 2,400,000 | 2010 |
| 4 | Forrest Gump | Drama | 8.8 | 2,100,000 | 1994 |
| 5 | The Matrix | Sci-Fi | 8.7 | 1,950,000 | 1999 |

### **C. Output 2: Top 3 Recommendations by Genre Preference**
#### **Genre: Sci-Fi**
| Rank | Title | Genre | Rating | Votes | Release_Year |
| :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | Inception | Sci-Fi | 8.8 | 2,400,000 | 2010 |
| 2 | The Matrix | Sci-Fi | 8.7 | 1,950,000 | 1999 |
| 3 | Interstellar | Sci-Fi | 8.7 | 1,900,000 | 2014 |

#### **Genre: Animation**
| Rank | Title | Genre | Rating | Votes | Release_Year |
| :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | Spirited Away | Animation | 8.6 | 790,000 | 2001 |
| 2 | Spider-Man: Into the Spider-Verse | Animation | 8.4 | 590,000 | 2018 |
| 3 | Coco | Animation | 8.4 | 530,000 | 2017 |

### **D. Output 3: Top 5 Recommendations by Weighted Score**
| Rank | Title | Genre | Rating | Votes | Weighted_Score |
| :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | The Shawshank Redemption | Drama | 9.3 | 2,750,000 | 9.16 |
| 2 | The Dark Knight | Action | 9.0 | 2,700,000 | 8.92 |
| 3 | Inception | Sci-Fi | 8.8 | 2,400,000 | 8.76 |
| 4 | Forrest Gump | Drama | 8.8 | 2,100,000 | 8.75 |
| 5 | Interstellar | Sci-Fi | 8.7 | 1,900,000 | 8.68 |

---

## 5. Conclusion & Learning Outcome

### **Conclusion**
A Python and Pandas-based recommendation system was successfully designed and tested. The system effectively:
- Ingested structured tabular data into a Pandas DataFrame.
- Cleaned and prepared multi-attribute data for evaluation.
- Successfully sorted and filtered candidate items according to user preferences and statistical weighting.
- Provided concise, ranked Top 3 and Top 5 recommendations suitable for deployment in real-world entertainment portals.

### **Learning Outcome**
Through this self-learning task:
1. Understood how real-world tabular data can be modeled, inspected, and manipulated using **Pandas DataFrames**.
2. Mastered methods for conditional filtering (`df[df['Genre'] == ...]`) and composite sorting (`sort_values()`).
3. Gained hands-on practical intuition into recommendation algorithms, including how popularity and rating metrics interact to generate fair recommendations.
