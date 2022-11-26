import pymongo
import json
import pandas as pd
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
Database_nme = "aps"
collection_nme = "sensor"
File_path = '/config/workspace/aps_failure_training_set1.csv'
if __name__== "__main__":
   df = pd.read_csv(File_path) 
   
   # convert df into json so that we can dump this record into Mongo DB
   df.reset_index(drop=True,inplace=True)

   json_record = list(json.loads(df.T.to_json()).values())
   json_record = list(json.loads(df.T.to_json()).values())
   json_record = list(json.loads(df.T.to_json()).values())
   print(json_record[0])

   #insert converted json into mongo db
   client[Database_nme][collection_nme].insert_many(json_record)
   