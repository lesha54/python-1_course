import pandas as pd 
import datetime
import os
import getpass
import uuid
from functools import wraps

def log_call(log_file="logs.csv"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = datetime.datetime.now()
            log_entry = {
                "id": str(uuid.uuid4()),
                "pc_username": getpass.getuser(),
                "function_name": func.__name__,
                "Date": now.strftime("%d.%m.%Y"),
                "Time": now.strftime("%H:%M:%S")
            }

            if os.path.exists(log_file):
                df = pd.read_csv(log_file)
                df = pd.concat([df, pd.DataFrame([log_entry])], ignore_index=True)
            else:
                df = pd.DataFrame([log_entry])

            df.to_csv(log_file, index=False)

            return func(*args, **kwargs)
        return wrapper
    return decorator
