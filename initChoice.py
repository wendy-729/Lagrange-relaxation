# 活动从0开始编号
def initChoice(file):
    data=[]
    with open(file, 'r') as f:
        for line in f.readlines():
            # temp=line.split()
            temp = line.strip('\n').split(",")
            temp = [int(x)-1 for x in temp]
            data.append(temp)
    # print('原始数据', data)
    return data