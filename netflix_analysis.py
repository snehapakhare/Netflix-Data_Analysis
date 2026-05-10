import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("TV Shows - Netflix.csv")

# -----------------------------
# BASIC INFO
# -----------------------------
print("\nFirst 5 Rows:")
print(df.head())

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nNull Values:")
print(df.isnull().sum())

# -----------------------------
# DATA CLEANING
# -----------------------------
df.drop_duplicates(inplace=True)

# -----------------------------
# TOP IMDB RATED SHOWS
# -----------------------------
print("\nTop 10 IMDb Rated Shows:")
top_shows = df.sort_values(by='IMDB_Rating', ascending=False)

print(top_shows[['Titles', 'IMDB_Rating']].head(10))

# -----------------------------
# RATING DISTRIBUTION
# -----------------------------
plt.figure(figsize=(8,5))

sns.countplot(x='Rating', data=df)

plt.title("Netflix Content Ratings")
plt.xticks(rotation=45)

plt.savefig("ratings_distribution.png")

plt.show()

# -----------------------------
# YEAR-WISE CONTENT
# -----------------------------
plt.figure(figsize=(12,6))

sns.countplot(x='Year', data=df)

plt.title("Netflix Shows Released Per Year")
plt.xticks(rotation=90)
plt.savefig("yearwise_content.png")

plt.close()

# -----------------------------
# TOP 10 IMDB SHOWS GRAPH
# -----------------------------
top10 = top_shows.head(10)

plt.figure(figsize=(10,5))

sns.barplot(
    x='IMDB_Rating',
    y='Titles',
    data=top10
)

plt.title("Top 10 IMDb Rated Shows")

plt.savefig("top10_imdb.png")

plt.close()

# -----------------------------
# AVERAGE IMDB RATING
# -----------------------------
average_rating = df['IMDB_Rating'].mean()

print("\nAverage IMDb Rating:", round(average_rating, 2))

print("\nProject Analysis Completed Successfully!")

