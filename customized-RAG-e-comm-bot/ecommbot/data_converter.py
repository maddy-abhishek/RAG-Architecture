import pandas as pd
from langchain_core.documents import Document
from pathlib import Path


def dataconveter():
    # Get the path to the current file (data_converter.py)
    current_file_path = Path(__file__)
    
    # Go up two levels (ecommbot -> E-Commerce-Chatbot) and then to data/file.csv
    csv_file_path = current_file_path.parent.parent / "data" / "flipkart_product_review.csv"
    
    print(f"Attempting to load data from: {csv_file_path}") # Good for debugging
    
    product_data = pd.read_csv(csv_file_path)

    data=product_data[["product_title","review"]]

    product_list = []

    # Iterate over the rows of the DataFrame
    for index, row in data.iterrows():
        # Construct an object with 'product_name' and 'review' attributes
        obj = {
                'product_name': row['product_title'],
                'review': row['review']
            }
        # Append the object to the list
        product_list.append(obj)

        
            
    docs = []
    for entry in product_list:
        metadata = {"product_name": entry['product_name']}
        doc = Document(page_content=entry['review'], metadata=metadata)
        docs.append(doc)
    return docs