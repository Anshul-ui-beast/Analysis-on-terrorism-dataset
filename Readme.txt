Terrorism Data Analysis (1970–2017)

=>This project analyzes the Global Terrorism Dataset to uncover insights into terrorism trends,
casualties, and attack types across key South Asian countries: India, Afghanistan, and Iraq.
The analysis combines data cleaning, feature engineering, and visualizations to better 
understand terrorism patterns.

🔑 Features

1. Data Preprocessing & Cleaning
- Handled missing numerical values using SimpleImputer (median strategy).
- Reconstructed proper Date column from year, month, and day.
- Converted categorical columns (region_txt, attacktype1_txt) for optimized memory usage.

2. Exploratory Data Analysis (EDA)
- Frequency of terrorist attacks over time (1970–2017).
- Country-wise casualties (killed + wounded) visualized with stacked bar charts.
- Top 10 target types per country visualized with grouped bar plots.

3. Focus on South Asia
- Filtered dataset to analyze terrorism trends in India, Afghanistan, and Iraq.
- Comparative visualizations to highlight differences in attack frequency, casualties, and target types.

📊 Visualizations

- Line Plot: Number of attacks per year for India, Afghanistan, and Iraq.
- Stacked Bar Chart: Total casualties (fatalities + injuries) by country.
- Grouped Subplots: Top 10 target types for each country.

📂 File Workflow

terrorism_dataset.csv → Input dataset.
Script performs:
Data cleaning & imputation.
Feature creation (Date).
Filtering for selected countries.
Generating comparative plots.

🛠️ Technologies Used

- Python
- pandas, NumPy
- matplotlib, seaborn
- scikit-learn (for imputation)