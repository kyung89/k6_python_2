# 2750  수 정렬하기
# 2587  대표값
# 25305 커트라인

# 2908  상수
# 7785  회사에 있는 사람 : 딕셔너리를 사용해야 함!

import json

data = '{"name":"Kim", "age":29}'
member = {"name":"Kim", "age":29}

with open('member.json', 'w') as w_file:
    json.dump(data, w_file)

with open('member.json', 'r') as r_file:
    d = json.load(r_file)
    print(d, type(d))

d2 = json.dumps(member)
print(d2, type(d2))

d3 = json.loads(d2)
print(d3, type(d3), d3["name"])

# 리스트 등을 저장할 때는 아래를 쓴다
import pickle

data = [1,2,3,4,5]
with open('dump_member.pk', 'wb') as w_file:
    pickle.dump(data, w_file)

with open('dump_member.pk', 'rb') as r_file:
    data2 = pickle.load(r_file)
print(data2)


# p.285 리펙토링

# F2: 이름 변경
# refactor 사용해 함수로 분리

