from matplotlib import pyplot as plt
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

name = ['홍길동', '이순신', '강감찬']
kor = [50, 70, 20] # 국어
eng = [30, 50, 70] # 영어


fig, ax = plt.subplots()
ax.plot(name, eng, label="영어", color="red")
ax.plot(name, kor, label="국어", color="black")
ax.scatter(name, eng, color="red")
ax.scatter(name, kor, color="black")

ax.legend()

plt.show()