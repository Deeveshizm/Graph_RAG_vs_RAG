import pandas as pd
import numpy as np

def classify_description(row):
    if row['Quantity'] > 0:
        return 'Product'
    elif row['Quantity'] <= 0:
        if str(row['Description']).isupper():
            return 'Product'
        else:
            return 'Reason'
    return 'Unknown'

def clean_data(df):
    # Remove rows with missing values
    df['CustomerID'] = df['CustomerID'].fillna('Unknown_'+ df['InvoiceNo']).astype(str)
    
    # Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], dayfirst=True, errors='coerce').strftime('%Y-%m-%d %H:%M:%S')
    
    # Deciding if the transaction is a return
    df['IsReturn'] = df.apply(
    lambda row: True if row['Quantity'] < 0 or str(row['InvoiceNo']).startswith('C') else False, 
    axis=1
    )

    # Apply the classification
    df['DescriptionType'] = df.apply(classify_description, axis=1)

    # Save cleaned data
    df.to_csv('../data/Online Retail Data Set Cleaned.csv', index=False)


if __name__ == '__main__':
    data = pd.read_csv('../data/Online Retail Data Set.csv', encoding = 'ISO-8859-1')
    clean_data(data)