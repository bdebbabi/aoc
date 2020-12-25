from datetime import datetime
from shutil import copyfile
from os import path
import requests

day = datetime.today().day
code_file = f"code/day{day}.py"
if not path.exists(code_file):
    copyfile('template.py', code_file)

session = requests.Session()
url = f"https://adventofcode.com/2020/day/{day}/input"
sessionID = "53616c7465645f5f56ff780d84fcf3382cc3077b0f3de6d806446708d1ffddf3fc426b7811eb7505725a05ae2c125d5a"
input  = session.get(url, headers = {"Cookie":f"session={sessionID}"}).text

with open(f"data/day{day}_input.csv", "w") as f:
    f.write(input)
