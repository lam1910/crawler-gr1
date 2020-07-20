- Console command:
```buildoutcfg
scrapy runspider travel-blog-crawler.py -o new-data.json
```
- ~~You will need to clean the data by hand. Read and select what we need. 
Or can filter the information at the pandas dataframe.~~ Already clean text. Not recommend 
put all the thing you crawl into database as postgresql varchar max 
at 10485760 chars. This example it can fit.
- The new-data.json is preprocessed data. world-travel-family.json is 
the processed data while world-travel-family.csv is the csv version of 
that json file. Data in both files have not been cleaned yet. backupdata.sql 
is the sql script to create the table in postgresql with dirty data.
