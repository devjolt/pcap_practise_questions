import os
from random import randint

files = os.listdir()
while True:
    try:
        exec(f"import {files[randint(0, len(files)-1)]}")
    except BaseException:
        continue
        
