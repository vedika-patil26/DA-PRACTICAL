import pandas as pd

df = pd.DataFrame({
    "name": [
        "Priyanka", "Vaishali", "Divya", "Pranjal",
        "Neha", "Vishal", "Vedant", "Rani",
        "Seema", "Tejas", "Parth", "Krushna",
        "Samarth", "Shiv", "Sahil", "Ritu"
    ],
    "marks": [
        99, 44, 86, 56, 34, 24, 37, 87,
        65, 45, 14, 53, 25, 60, 72, 45
    ],
    "dept": [
        "computer", "civil", "ETC", "IT",
        "mechanical", "chemical", "BCA", "MCA",
        "DataScience", "AI", "Diploma", "Mpharm",
        "Dpharm", "Bpharm", "Electrical", "ML"
    ]
})

print("Original Data:\n", df)

# Data subsetting
print("\nSubset (marks > 50):\n", df[df["marks"] > 50])

# Sorting in ascending order
print("\nSorted by marks (ascending):\n", df.sort_values("marks"))

# Sorting in descending order
print("\nSorted by marks (descending):\n",
      df.sort_values("marks", ascending=False))

# Grouping
print("\nGrouped (Average marks by department):\n",
      df.groupby("dept")["marks"].mean())

# Statistical operations
print("\nMean =", df["marks"].mean())
print("Median =", df["marks"].median())

print("Mode =")
print(df["marks"].mode())