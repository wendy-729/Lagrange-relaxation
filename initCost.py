def initCost(file):
    data=[]
    with open(file, 'r') as f:
        for line in f.readlines():
            temp = line.strip('\n')
            nums = temp.split(",")
            nums = [int(x) for x in nums]
            data.append(nums)
            # nums = list(filter(not_empty, data))
            # nums = [int(x) for x in nums]
            # data.append(nums)
    # print('原始数据', data)
    return data