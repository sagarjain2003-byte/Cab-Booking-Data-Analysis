import pandas as pd
import matplotlib.pyplot as plt

# csv file ko load kar rahe hu
try:
    df = pd.read_csv("PROJECT TABLES/cab_booking_data.csv")
except FileNotFoundError:
    print("csv file nahi mili")
    exit()

# pehli 5 rows dekh raha hu
print(" First 5 Records ")
print(df.head())

# duplicate data hataya ha
df = df.drop_duplicates()

# agar koi value missing hai to usko fill kar do
df = df.fillna("Unknown")

# total bookings
print("Total Bookings :", len(df))

# city ke hisab se booking count
print("City Wise Bookings")
print(df["City"].value_counts())

# cab type ke hisab se booking count
print("Cab Type Count")
print(df["Cab_Type"].value_counts())

# total revenue nikal rahe hai
total_revenue = df["Fare_INR"].sum()
print("Total Revenue :", total_revenue)

# average fare
average_fare = df["Fare_INR"].mean()
print("Average Fare :", round(average_fare, 2))

# sabse jyada earning wali city
print("Revenue by City")
print(df.groupby("City")["Fare_INR"].sum())

# completed aur cancelled booking count
print("Booking Status")
print(df["Booking_Status"].value_counts())

# report ko save kar rahe hai
df.to_csv("cab_booking_report.csv", index=False)

print("Report save ho gayi")

# city wise graph ban jayega 
plt.figure(figsize=(8,5))
df["City"].value_counts().plot(kind="bar")
plt.title("City Wise Bookings")
plt.xlabel("City")
plt.ylabel("Bookings")
plt.tight_layout()
plt.show()

# cab type graph
plt.figure(figsize=(6,5))
df["Cab_Type"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Cab Type Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# rating ka histogram
plt.figure(figsize=(7,5))
plt.hist(df["Customer_Rating"], bins=5)
plt.title("Customer Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

print("Project Successfully Completed")
