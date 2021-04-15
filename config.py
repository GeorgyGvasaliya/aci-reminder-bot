from datetime import datetime
import os

token = os.getenv('TOKEN')
chat_id = int(os.getenv('CHAT_ID'))
designers_url = os.getenv('DESIGN_URL')
qa_url = os.getenv('QA_URL')

DESIGN_EARLY = datetime(datetime.today().year, datetime.today().month,
                        datetime.today().day, hour=14, minute=45).strftime('%H:%M')
DESIGN_LATE = datetime(datetime.today().year, datetime.today().month,
                       datetime.today().day, hour=14, minute=55).strftime('%H:%M')

QA_EARLY = datetime(datetime.today().year, datetime.today().month,
                    datetime.today().day, hour=11, minute=45).strftime('%H:%M')
QA_LATE = datetime(datetime.today().year, datetime.today().month,
                   datetime.today().day, hour=11, minute=55).strftime('%H:%M')
