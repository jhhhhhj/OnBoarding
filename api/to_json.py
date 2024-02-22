import pandas as pd

class TOJSON():
    def __init__(self):
        pass

    def save_dataframe_to_json(self, df, filename):
        df.to_json(filename, orient="records")