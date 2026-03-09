import pandas as pd
import matplotlib.pyplot as plt
import os


# Get the directory of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "..", "dataset", "superstore.csv")   # dataset folder

df = pd.read_csv(file_path, encoding='latin1')

print("Dataset Loaded Successfully")
print(df.head())


# check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# remove duplicates
df = df.drop_duplicates()

# convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# create extra columns
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Month_Name'] = df['Order Date'].dt.month_name()

print("\nData Cleaning Completed")


sales_trend = df.groupby("Year")["Sales"].sum()

print("\nYearly Sales Trend:")
print(sales_trend)

plt.figure()
sales_trend.plot(marker="o")
plt.title("Yearly Sales Trend")
plt.xlabel("Year")
plt.ylabel("Sales")
plt.savefig(os.path.join(base_dir, "..", "screenshots", "yearly_sales_trend.png"))
plt.close()


top_products = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)

print("\nTop Selling Products:")
print(top_products.head(10))

plt.figure()
top_products.head(10).plot(kind="bar")
plt.title("Top 10 Selling Products")
plt.xlabel("Sub Category")
plt.ylabel("Sales")
plt.savefig(os.path.join(base_dir, "..", "screenshots", "top_selling_products.png"))
plt.close()

region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales)

plt.figure()
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.savefig(os.path.join(base_dir, "..", "screenshots", "sales_by_region.png"))
plt.close()

output_path = os.path.join(base_dir, "..", "dataset", "cleaned_superstore.csv")

df.to_csv(output_path, index=False)

print("\nCleaned dataset saved for Power BI!")