def read_data(file):
    data=[]
    with open(file, 'r') as f:
        for line in f.readlines():
            temp = line.strip('\n').split(' ')
            # print(temp)
            if temp[3] == '1':
                data.append(int(temp[0]))
            # nums = [int(x) for x in temp]
            # print(nums)
            # data.append(nums)
            # nums = list(filter(not_empty, data))
            # nums = [int(x) for x in nums]
            # data.append(nums)
    # print('原始数据', data)
    return data

def read_data_ga(file):
    data=[]
    with open(file, 'r') as f:
        for line in f.readlines():
            temp = line.strip('\n').split('\t')
            # print(temp[1])
            data.append(int(float(temp[1])))
            # nums = [int(x) for x in temp]
            # print(nums)
            # data.append(nums)
            # nums = list(filter(not_empty, data))
            # nums = [int(x) for x in nums]
            # data.append(nums)
    # print('原始数据', data)
    return data