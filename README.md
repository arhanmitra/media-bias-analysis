# Political Polarization in News Media Headlines

## Objective
This project explores whether news outlets with different political leanings (Left, Center, Right) use different tones in their headlines. By applying sentiment analysis, we can detect patterns in how news is framed depending on bias.

---

## Steps

### 1. Data Collection
- Use a dataset of news headlines labeled by political bias (e.g., Left, Center, Right).
- Each headline is paired with its bias label so we can analyze groups.

### 2. Preprocessing
- Clean the text (remove missing values, standardize formats).
- Ensure each headline is ready for sentiment analysis.

### 3. Sentiment Analysis
- Apply the **VADER Sentiment Analyzer** to each headline.
- VADER assigns a score between `-1` (very negative) and `+1` (very positive).
- The **compound score** is used as the overall sentiment measure.

### 4. Aggregation
- Group headlines by political bias.
- Calculate the **average sentiment score** for each group.

### 5. Visualization
- Create a bar chart showing average sentiment for Left, Center, and Right.
- This allows for a visual comparison of tone across political leanings.

### 6. Article Counts
- Count how many headlines are in each bias category.
- Print totals at the end to check dataset balance.

---


