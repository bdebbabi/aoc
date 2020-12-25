from datetime import date
from shutil import copyfile
import pyperclip
import os 
today = (date.today()-date(2020,12,1)).days+1

def read(day=today, ret_type=None):
    input_file = f'data/day{day}_input'
    if ret_type =='str':
        txt = f'{input_file}.txt'
        if not os.path.isfile(txt):
            copyfile(f'{input_file}.csv', txt)
        with open(txt, 'r') as f:
            content = f.read()
        os.remove(txt)
        yield content.strip()
        
    else:
        for line in open(f'{input_file}.csv'):
            if ret_type == 'int':
                yield int(line.rstrip())
            elif ret_type == 'float':
                yield float(line.rstrip())
            else:
                yield line.rstrip()

def ret(value=''):
    print(value)
    pyperclip.copy(value)
    return value
