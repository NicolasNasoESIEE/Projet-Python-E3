import os
import shutil

FILENAME = "us_tornado_dataset_1950_2021.csv"

def api_csv():
    if os.path.exists(FILENAME) :  
        os.remove(FILENAME)
    username = os.environ['USERNAME']
    json_path = 'C:\\Users\\'+username+'\\.kaggle'
    if not os.path.exists(json_path) : 
        os.mkdir(json_path)
    shutil.copy('kaggle.json', json_path)
    os.system('kaggle datasets download -d danbraswell/us-tornado-dataset-1950-2021')
    os.system('tar -xf us-tornado-dataset-1950-2021.zip')
    os.remove("us-tornado-dataset-1950-2021.zip")