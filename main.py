from fastapi import FastAPI
import pandas as pd
from api.crawl import CRAWL
from api.to_json import TOJSON
from models.mail import Mail
from api.mail_send import MAILSEND
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

app = FastAPI()
crawl = CRAWL()
mailsend = MAILSEND()

@app.get("/test")
def test():
    return 'test page'

@app.get("/scheduler")
def scheduler():
    df = pd.DataFrame(columns=['name','role','dept','contact'])
    return crawl.crawl(df)

@app.post("/mail")
async def get_mail(mail: Mail):
    return mailsend.user_matching(mail)
    # return {"sender_email": mail.sender_email, "receiver_email": mail.receiver_email}

def job_function():
    crawl_instance = CRAWL()
    df = crawl_instance.crawl(df=pd.DataFrame(columns=['Name', 'Role', 'Dept', 'Contact']))
    # global_df = pd.DataFrame(columns=['Name', 'Role', 'Dept', 'Contact'])
    df = crawl_instance.crawl(df=df)
    
    # df는 crawl 메소드에서 채워진 DataFrame입니다.

    # TOJSON 클래스의 인스턴스 생성
    tojson = TOJSON()

    # 현재 날짜를 기반으로 파일 이름 생성
    now = datetime.now()
    filename = str(now.date()) + "_data.json"

    # DataFrame을 JSON 파일로 저장
    tojson.save_dataframe_to_json(df=df, filename=filename)

    # TODO 여기서 테이블 조인

sched = BackgroundScheduler(timezone='Asia/Seoul') #백그라운드로 실행하기 위해 선언
sched.start() 

#테스트
sched.add_job(job_function, 'interval', seconds=60) # 수행할 함수를 job에 등록

#실제 오전 6시마다 실행
#sched.add_job(job_function, 'interval', days=1, start_date='2024-02-22 06:00:00')
