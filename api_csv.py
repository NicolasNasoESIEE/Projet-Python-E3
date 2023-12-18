import os
import shutil
import json

FILENAME = "us_tornado_dataset_1950_2021.csv"

DATA = {"username":"nicolasnaso","key":"dfd72dc597bb350a527001eec6b7c699"}

def api_csv():
    if os.path.exists(FILENAME) :  
        os.remove(FILENAME)
    username = os.environ['USERNAME']
    json_path = 'C:\\Users\\'+username+'\\.kaggle'
    if not os.path.exists(json_path) : 
        os.mkdir(json_path)
    with open(json_path+"\\kaggle.json", 'w') as f:
        json.dump(DATA,f)
    #shutil.copy('kaggle.json', json_path)
    os.system('kaggle datasets download -d danbraswell/us-tornado-dataset-1950-2021')
    os.system('tar -xf us-tornado-dataset-1950-2021.zip')
    os.remove("us-tornado-dataset-1950-2021.zip")