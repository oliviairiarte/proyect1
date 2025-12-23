
import csv

def add_to_report(lista): #list of dicts
    
    # 1. Define the header/field names
    names = ['Date n time','Original file','Final desktop','New file name']

    with open("data2.csv", "w",  newline="") s file:
        # Create a DictWriter instance
        writer = csv.DictWriter(file, fieldnames= names)
        
        # Write the header row
        writer.writeheader()
        
        # Write the data rows
        writer.writerows(lista)
