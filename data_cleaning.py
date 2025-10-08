import sqlite3
import pandas as pd
from datetime import date

# ----------------------------
# Connect to the database
# ----------------------------
conn = sqlite3.connect("SupplyChain.db")

# Read table names from the database
tables_df = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table'", conn)
tables = tables_df['name'].tolist()

# ----------------------------
# Cleaning Functions per Table
# ----------------------------

def clean_products(df):
    """
    Cleans the Products DataFrame.
    
    - Removes duplicate rows.
    - Standardizes string columns (capitalization, whitespace).
    - Corrects illogical values for UnitPrice and CostPrice.
    - Corrects illogical LaunchDates.
    - Handles missing VendorID values.
    """
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Handle inconsistent text
    df['Category'] = df['Category'].str.strip().str.title()
    df['ProductStatus'] = df['ProductStatus'].str.strip().str.title()
    df['SupplierCategory'] = df['SupplierCategory'].str.strip().str.title().replace('Internationl', 'International')
    df['ProductName'] = df['ProductName'].str.strip()
    
    # Handle outliers and illogical values: `UnitPrice` and `CostPrice`
    # Calculate median *before* correcting outliers to ensure it's not skewed
    median_unit_price = df['UnitPrice'].median()
    median_cost_price = df['CostPrice'].median()

    df.loc[df['UnitPrice'] < 0, 'UnitPrice'] = median_unit_price
    df.loc[df['CostPrice'] < 0, 'CostPrice'] = median_cost_price
    # The cost should not be higher than the unit price. A reasonable fix is to set it to a portion of the UnitPrice.
    df.loc[df['CostPrice'] > df['UnitPrice'], 'CostPrice'] = df['UnitPrice'] * 0.8
    
    # Correct illogical values: `LaunchDate` must be in the past.
    df['LaunchDate'] = pd.to_datetime(df['LaunchDate'], errors='coerce')
    median_launch_date = df['LaunchDate'].median()
    df.loc[df['LaunchDate'] > pd.Timestamp(date.today()), 'LaunchDate'] = median_launch_date
    
    # Handle missing values: `VendorID`
    df['VendorID'].fillna(df['VendorID'].mode()[0], inplace=True)
    df['VendorID'] = df['VendorID'].astype(int)

    return df

def clean_customers(df):
    """
    Cleans the Customers DataFrame.
    
    - Removes duplicates.
    - Fills missing values.
    - Normalizes string columns.
    - Handles outliers for LoyaltyScore.
    """
    df['CustomerID'] = pd.to_numeric(df['CustomerID'], errors='coerce')
    df = df.drop_duplicates(subset=["CustomerID"])
    
    df['CustomerName'] = df['CustomerName'].fillna('Unknown').str.strip()
    
    # Use dictionary for more robust replacement
    df['Region'] = df['Region'].replace({'NA': 'North America'}).str.strip().fillna('Unknown').str.title()
    
    df["Segment"] = df["Segment"].str.strip().str.title()
    df["JoinDate"] = pd.to_datetime(df["JoinDate"], errors="coerce")
    df["CustomerType"] = df["CustomerType"].str.strip().str.title()
    df["PreferredCategory"] = df["PreferredCategory"].str.strip().str.title()
    
    df["AvgOrderValue"].fillna(df["AvgOrderValue"].median(), inplace=True)
    
    # Handle outliers: `LoyaltyScore`
    df['LoyaltyScore'] = df['LoyaltyScore'].clip(lower=0, upper=10)
    df["LoyaltyScore"].fillna(df["LoyaltyScore"].median(), inplace=True)
    
    return df

def clean_vendors(df):
    """
    Cleans the Vendors DataFrame.
    
    - Removes duplicates.
    - Fills missing values.
    - Handles outliers for RatingScore and LeadTimeDays.
    - Corrects data types.
    """
    df = df.drop_duplicates(subset=['VendorID'])
    
    df['VendorName'] = df['VendorName'].fillna('Unknown Vendor').str.strip().str.title()
    df['ReliabilityScore'].fillna(df['ReliabilityScore'].median(), inplace=True)
    df['ReliabilityScore'] = pd.to_numeric(df['ReliabilityScore'])
    
    df['RatingScore'] = df['RatingScore'].clip(lower=0, upper=10)
    df['Region'] = df['Region'].str.strip().str.title()
    
    df['LeadTimeDays'] = df['LeadTimeDays'].clip(lower=0)
    
    return df

def clean_warehouses(df):
    """
    Cleans the Warehouses DataFrame.
    
    - Removes duplicates.
    - Normalizes text columns.
    - Handles illogical values for CapacityUsed.
    - Handles negative AvgDispatchTime.
    """
    df = df.drop_duplicates(subset=['WarehouseID'])
    
    df['Location'] = df['Location'].str.strip().str.title()
    df['TemperatureControlled'] = df['TemperatureControlled'].str.strip().str.title()
    df['AvgDispatchTime'] = df['AvgDispatchTime'].clip(lower=0)
    
    df['CapacityUsed'] = df['CapacityUsed'].clip(lower=0, upper=1.0)
    
    return df

def clean_inventory(df):
    """
    Cleans the Inventory DataFrame.
    
    - Removes duplicates.
    - Handles missing values for ReorderLevel.
    - Corrects illogical values for StockOnHand and StockAgeDays.
    - Corrects illogical values for AvgMonthlySales.
    - Normalizes strings for StockStatus.
    """
    df = df.drop_duplicates(subset=['ProductID', 'WarehouseID'])
    
    df['ReorderLevel'].fillna(df['ReorderLevel'].median(), inplace=True)
    
    df['StockOnHand'] = df['StockOnHand'].clip(lower=0)
    df['StockAgeDays'] = df['StockAgeDays'].clip(lower=0)
    df['AvgMonthlySales'] = df['AvgMonthlySales'].clip(lower=0)
    
    df['LastUpdated'] = pd.to_datetime(df['LastUpdated'], errors='coerce')
    
    # Use `.str.replace()` for string replacement
    df['StockStatus'] = df['StockStatus'].str.strip().str.title().str.replace('Stock_Low', 'Low')
    
    return df

def clean_sales(df):
    """
    Cleans the Sales DataFrame.
    
    - Removes duplicates.
    - Corrects negative values for Quantity and ShippingCost.
    - Fills missing SalesAmount.
    - Normalizes strings for SalesChannel, PaymentMethod and OrderStatus.
    - Converts Date column to datetime.
    """
    df = df.drop_duplicates()
    
    df['Quantity'] = df['Quantity'].clip(lower=0)
    df['ShippingCost'] = df['ShippingCost'].clip(lower=0)
    
    df['SalesAmount'] = df['SalesAmount'].fillna(0).clip(lower=0)
    
    df['SalesChannel'] = df['SalesChannel'].str.strip().str.title().replace('Website', 'Online')
    df['OrderStatus'] = df['OrderStatus'].str.strip().str.title()
    df['PaymentMethod'] = df['PaymentMethod'].str.strip()
    
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    return df

def clean_shipments(df):
    """
    Cleans the Shipments DataFrame.
    
    - Removes duplicates.
    - Corrects illogical dates.
    - Handles missing DeliveryCost and TrackingID.
    - Imputes missing DeliveryDates with a logical value.
    - Normalizes string columns.
    """
    df = df.drop_duplicates(subset=['ShipmentID'])
    
    df['TrackingID'].fillna('Unknown', inplace=True)
    
    df['ShipDate'] = pd.to_datetime(df['ShipDate'], errors='coerce')
    df['ActualDeliveryDate'] = pd.to_datetime(df['ActualDeliveryDate'], errors='coerce')
    
    # Correct illogical values: DeliveryDate must be on or after ShipDate.
    df.loc[df['ActualDeliveryDate'] < df['ShipDate'], 'ActualDeliveryDate'] = df['ShipDate']
    
    # Impute missing DeliveryDates
    # Calculate median delay from non-null values
    df['DelayDays'] = (df['ActualDeliveryDate'] - df['ShipDate']).dt.days
    median_delay = df['DelayDays'].median()
    df['ActualDeliveryDate'].fillna(df['ShipDate'] + pd.to_timedelta(median_delay, unit='D'), inplace=True)
    
    # Re-calculate delay days with all values to capture the imputed dates
    df['DelayDays'] = (df['ActualDeliveryDate'] - df['ShipDate']).dt.days
    
    # Handle negative values for DeliveryCost
    df.loc[df['DeliveryCost'] < 0, 'DeliveryCost'] = df['DeliveryCost'].median()
    
    # Normalize strings
    df['Status'] = df['Status'].str.strip().str.title()
    df['ShippingMode'] = df['ShippingMode'].str.strip().str.title()
    df['CarrierName'] = df['CarrierName'].str.strip()
    
    return df

# -------------------------
# Main Cleaning Function
# -------------------------

def clean_all_tables():
    """
    Main function to read, clean, and write all tables in the database.
    """
    print("Starting data cleaning process...")
    cleaned_dfs = {}
    for table in tables:
        print(f"Cleaning Table: {table}...")
        df = pd.read_sql(f"SELECT * FROM {table}", conn)
        
        # Use a more flexible if/elif structure or a dictionary for function mapping
        if table == 'products':
            df = clean_products(df)
        elif table == 'vendors':
            df = clean_vendors(df)
        elif table == 'warehouses':
            df = clean_warehouses(df)
        elif table == 'customers':
            df = clean_customers(df)
        elif table == 'inventory':
            df = clean_inventory(df)
        elif table == 'sales':
            df = clean_sales(df)
        elif table == 'shipments':
            df = clean_shipments(df)
            
        cleaned_dfs[table] = df
        print(f"Completed cleaning: {table}, Shape: {df.shape}\n")
    
    print("All tables cleaned successfully!")
    return cleaned_dfs
    
if __name__ == "__main__":
    clean_all_tables()
    conn.close()