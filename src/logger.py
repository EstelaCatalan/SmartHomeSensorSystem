import os 
import logging
log_dir = "data"
#create dir data/ if it doesn't exists
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
	filename="data/app.log",
	filemode="a", #append
	format="%(asctime)s - %(levelname)s - %(message)s", #Format: date,level,message
	level =logging.DEBUG #min level
)
 
