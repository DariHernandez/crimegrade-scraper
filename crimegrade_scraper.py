import os
import time
import bs4
import requests
from scraping_manager.automate import Web_scraping



# Get zip codes
zipcodes = []
zipcodes_path = os.path.join(os.path.dirname(__file__), "zipcodes.txt")
with open (zipcodes_path, "r") as file:
    zipcodes = file.readlines()
    
# Loop for each zip code in list
for zipcode in zipcodes: 
    zipcode_formated = zipcode.replace("\n", "")
    page = f"https://crimegrade.org/safest-places-in-{zipcode_formated}/"
    
    # Instance of selenium
    scraper = Web_scraping(page, headless=True, user_agent=True)
    
    
    tables_selectors = [
        "p + .one_third", 
        ".one_third + .one_third", 
        ".one_third.et_column_last"
    ]
    
    data = {}
    for table_selector in tables_selectors: 

        #  Get data for each table
        selector_row_vcr = f"{table_selector} > .SummaryStats.mtr-table.mtr-tr-th tr"
        rows_vcr = scraper.get_elems(selector_row_vcr)
        
        # Loopf ro each row in table
        for index_row in range(0, len(rows_vcr)+1): 
            title_selector = selector_row_vcr + f":nth-child({index_row}) > *:nth-child(1)"
            value_selector = selector_row_vcr + f":nth-child({index_row}) > *:nth-child(2)"
            
            title = str(scraper.get_text(title_selector)).strip()
            value = str(scraper.get_text(value_selector)).strip()
        
            # Clean data
            sktip_tiles = [None, "Crime Type", "None"]
            if title and value and not title in sktip_tiles:
                
                data[title] = value
        
    import pprint
    pprint.pprint (data)

        
    
    # End browser
    scraper.end_browser()
    
    break
    