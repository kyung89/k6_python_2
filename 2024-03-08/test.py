# [1]
from pathlib import Path
import os

top = Path('aaa')

for root, dirs, files in os.walk(top, topdown=False): # 체크 필요
    for name in files:
        os.unlink(root +"/"+ name)
    for name in dirs:
        os.rmdir(root +"/"+ name)

# [2]
import json

data = json.loads('{"a": 1, "b": 2}')
type(data) # json
print(data["a"]) # 1
print(data["b"]) # 2