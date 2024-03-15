try:
    with open('notexist.csv') as f:
        for line in f:
            print(line)
except Exception as e:
    print(e)
    pass
    