import pandas as pd
from datetime import datetime

class MAILSEND():
    def __init__(self):
        pass

    def load_dataframe_from_json(self, filename):
        # JSON 파일에서 데이터를 읽어와 데이터프레임으로 변환
        df = pd.read_json(filename, orient="records")
        return df

    def user_matching(self, mail):
        now = datetime.now()
        filename = str(now.date())+"_data.json"
        print(filename)
        df = self.load_dataframe_from_json(filename=filename)
        print(mail.sender_email)

        return df
