import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from ..exception import CustomException


from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#in data ingestion we will read the data and split it into train and test set and save it in the local directory
#where i should dave the train and test data this we will mention in dataingestionconfig

class DataIngestionConfig:
    train_data_path=os.path.join('artifacts','train.csv')#train data will be saved in artificats folder
    test_data_path=os.path.join('artifacts','test.csv')#same for test data 
    raw_data_path=os.path.join('artifacts','data.csv')#raw data will be saved in artifacts folder

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()#creating an object of dataingestionconfig class

    def initiate_data_ingestion(self):
        logging.info('Entered the data ingestion method or component')
        try:
            df=pd.read_csv('notebook/data/stud.csv')#reading the data
            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)#creating the directory if it does not exist

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)#saving the raw data in the local directory

            logging.info('Train test split initiated')
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)#splitting the data into train and test set

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)#saving the train data in the local directory
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)#saving the test data in the local directory

            logging.info('Ingestion of the data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
if __name__=="__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()