import json

# 1. json - dump, load <--- file [책에 있음: 다음 수요일에 할 예정]
# 2. json - dumps, loads <--- fast API, Flask [오늘. 일반적인 상황]

data = {"name" : "Kim", "age" : 23}

print(data["name"], type(data), json.dumps(data), type(json.dumps(data)))
res_data = json.dumps(data)
print(json.loads(res_data), type(json.loads(res_data)))