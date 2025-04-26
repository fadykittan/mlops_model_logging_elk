import pickle

class Model:

    def __init__(self, config):
        self.config = config

    def load_model(self):
        with open(self.config.MODEL_PATH, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, df):
        res = self.model.predict(df)
        return res
