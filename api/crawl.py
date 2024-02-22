from datetime import datetime
from api.to_json import TOJSON

class CRAWL():
    def __init__(self):
        pass

    def crawl(self, df):
        tojson = TOJSON()
        now = datetime.now()
        for i in range(3):
            df.loc[i+1] = ['name'+str(i)+str(now.time()),'role'+str(i),'dept'+str(i),'contact'+str(i)]

        filename = f"{now.date()}_{now.time().strftime('%H%M%S')}_data.json"
        print(filename)

        tojson.save_dataframe_to_json(df=df, filename=filename)
        
        return df