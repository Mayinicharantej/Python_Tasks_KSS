#Data Analytics Project: Railway Gauges Data Analysis
#Dataset Used: railway_gauges 1.csv
#Project Title: Railway Gauges Data Analysis

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Setup: Automatically find the folder where this script is saved and create a 'graphs' folder
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'railway_gauges 1.csv')
graphs_dir = os.path.join(script_dir, 'graphs')
os.makedirs(graphs_dir, exist_ok=True)


# ==========================================
# Scenario 1: Basic Data Loading & Cleaning
# ==========================================
print("--- SCENARIO 1: BASIC DATA LOADING & CLEANING ---")

# Task 1: Load the dataset into a Pandas DataFrame
df = pd.read_csv(csv_path)

# Task 2: Display the first 5 rows and column names
print("\nFirst 5 rows:")
print(df.head())
print("\nColumn Names:", df.columns.tolist())

# Task 3: Check for missing values and replace them with 0
print("\nMissing values before cleaning:\n", df.isnull().sum())
df = df.fillna(0)

# Task 4: Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types
gauge_cols = ['Broad Gauge', 'Metre Gauge', 'Narrow Gauge', 'Total']
for col in gauge_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Helper step: Extract starting year (e.g., 1964 from '1964-65') for easy plotting and filtering
df['Start_Year'] = df['Year'].astype(str).str.split('-').str[0].astype(int)


# ==========================================
# Scenario 2: Simple Visualization
# ==========================================
print("\n--- SCENARIO 2: SIMPLE VISUALIZATION ---")

# Task 1: Extract Year and Total columns
years = df['Start_Year']
total_tracks = df['Total']

# Task 2: Plot a line graph showing Total tracks over years
plt.figure(figsize=(10, 5))
plt.plot(years, total_tracks, marker='o', color='blue', linewidth=2)

# Task 3: Add Title, X and Y labels (and save the graph)
plt.title('Total Railway Tracks Over Years')
plt.xlabel('Year')
plt.ylabel('Total Tracks')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'total_tracks_trend.png'))
plt.show()

# Task 4: Identify whether the trend is increasing or decreasing
trend = "increasing" if df['Total'].iloc[-1] > df['Total'].iloc[0] else "decreasing"
print(f"Total tracks changed from {df['Total'].iloc[0]} to {df['Total'].iloc[-1]} -> Overall trend is {trend}.")


# ==========================================
# Scenario 3: Filtering + Bar Chart
# ==========================================
print("\n--- SCENARIO 3: FILTERING + BAR CHART ---")

# Task 1: Filter the dataset for years after 2000
df_after_2000 = df[df['Start_Year'] > 2000]

# Task 2: Select Broad Gauge, Metre Gauge, and Narrow Gauge
broad = df_after_2000['Broad Gauge']
metre = df_after_2000['Metre Gauge']
narrow = df_after_2000['Narrow Gauge']

# Task 3: Plot a grouped bar chart comparing all three gauges
x = np.arange(len(df_after_2000['Year']))
width = 0.25

plt.figure(figsize=(12, 6))
plt.bar(x - width, broad, width, label='Broad Gauge')
plt.bar(x, metre, width, label='Metre Gauge')
plt.bar(x + width, narrow, width, label='Narrow Gauge')

# Task 4: Add legend and proper labels (and save the graph)
plt.title('Comparison of Railway Gauges (After 2000)')
plt.xlabel('Year')
plt.ylabel('Track Length')
plt.xticks(x, df_after_2000['Year'], rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'gauges_after_2000_bar.png'))
plt.show()

# Task 5: Identify which gauge dominates in recent years
recent_dominant = df_after_2000[['Broad Gauge', 'Metre Gauge', 'Narrow Gauge']].sum().idxmax()
print(f"Dominant gauge in recent years (after 2000): {recent_dominant}")


# ==========================================
# Scenario 4: Feature Engineering + Pie Chart
# ==========================================
print("\n--- SCENARIO 4: FEATURE ENGINEERING + PIE CHART ---")

# Task 1: Calculate total sum of each gauge across all years
broad_sum = df['Broad Gauge'].sum()
metre_sum = df['Metre Gauge'].sum()
narrow_sum = df['Narrow Gauge'].sum()

# Task 2: Create a new structure (Series) for totals
gauge_totals = pd.Series({
    'Broad Gauge': broad_sum,
    'Metre Gauge': metre_sum,
    'Narrow Gauge': narrow_sum
})
print("Total sum of each gauge:\n", gauge_totals)

# Task 3 & Task 4: Plot a pie chart showing percentage contribution and add percentage labels (autopct)
plt.figure(figsize=(7, 7))
plt.pie(gauge_totals, labels=gauge_totals.index, autopct='%1.1f%%', startangle=140)
plt.title('Percentage Contribution of Each Railway Gauge (All Years)')
plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'gauge_contribution_pie.png'))
plt.show()

# Task 5: Interpret which gauge contributes the most
print(f"Gauge contributing the most overall: {gauge_totals.idxmax()}")


# ==========================================
# Scenario 5: Advanced Analysis + Multiple Graphs
# ==========================================
print("\n--- SCENARIO 5: ADVANCED ANALYSIS + MULTIPLE GRAPHS ---")

# Task 1: Create new columns: % Broad Gauge, % Metre Gauge, % Narrow Gauge
df['% Broad Gauge'] = (df['Broad Gauge'] / df['Total']) * 100
df['% Metre Gauge'] = (df['Metre Gauge'] / df['Total']) * 100
df['% Narrow Gauge'] = (df['Narrow Gauge'] / df['Total']) * 100

# Task 2: Use NumPy (np.diff) to calculate yearly growth of Total tracks
yearly_growth = np.diff(df['Total'])
df['Yearly_Growth'] = np.insert(yearly_growth, 0, 0)  # First year has 0 growth

# Task 3a: Plot Line graph for all gauges
plt.figure(figsize=(10, 5))
plt.plot(df['Start_Year'], df['Broad Gauge'], label='Broad Gauge', linewidth=2)
plt.plot(df['Start_Year'], df['Metre Gauge'], label='Metre Gauge', linewidth=2)
plt.plot(df['Start_Year'], df['Narrow Gauge'], label='Narrow Gauge', linewidth=2)
plt.title('Trend of All Railway Gauges Over Years')
plt.xlabel('Year')
plt.ylabel('Track Length')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'all_gauges_line.png'))
plt.show()

# Task 3b: Plot Stacked bar chart showing composition
plt.figure(figsize=(14, 6))
plt.bar(df['Year'], df['Broad Gauge'], label='Broad Gauge')
plt.bar(df['Year'], df['Metre Gauge'], bottom=df['Broad Gauge'], label='Metre Gauge')
plt.bar(df['Year'], df['Narrow Gauge'], bottom=df['Broad Gauge'] + df['Metre Gauge'], label='Narrow Gauge')
plt.title('Composition of Railway Gauges Over Years (Stacked)')
plt.xlabel('Year')
plt.ylabel('Track Length')
plt.xticks(rotation=90, fontsize=8)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(graphs_dir, 'gauges_composition_stacked.png'))
plt.show()

# Task 4: Highlight years with highest growth and decline in any gauge
max_growth_row = df.loc[df['Yearly_Growth'].idxmax()]
print(f"Highest Growth Year: {max_growth_row['Year']} (+{max_growth_row['Yearly_Growth']})")
print(f"Metre Gauge declined from {df['% Metre Gauge'].iloc[0]:.1f}% to {df['% Metre Gauge'].iloc[-1]:.1f}%")
print(f"Narrow Gauge declined from {df['% Narrow Gauge'].iloc[0]:.1f}% to {df['% Narrow Gauge'].iloc[-1]:.1f}%")

