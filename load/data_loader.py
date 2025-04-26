import pandas as pd
import os

class DataLoader:

    def __init__(self, config):
        self.config = config

    def load(self):
        print(os.getcwd())
        df = pd.read_csv(self.config.FILE_PATH)
        return df
