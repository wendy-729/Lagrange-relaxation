# 逆向计算
def backward(su,duration, lftn, actNo, mandatory):
    # activities = len(duration)
    lst = [lftn-duration[i] for i in range(actNo)]

    lft = [lftn]*actNo
    for i in range(actNo-2, -1, -1):
        if i in mandatory:
            # 活动i的紧后活动
            for j in su[i]:
                if j in mandatory:
                    if lst[j] < lft[i]:
                        lft[i] = lst[j]
            lst[i] = lft[i]-duration[i]
    return lst, lft


# update逆向计算，所有活动都执行,只考虑必须执行的紧后活动
def backward_update(su, duration, lftn, actNo, mandatory):
    lst = [lftn - duration[i] for i in range(actNo)]
    lft = [lftn] * actNo
    for i in range(actNo - 2, -1, -1):
          # 活动i的紧后活动
        for j in su[i]:
            if j in mandatory:
                # 紧后活动的最晚开始时间<活动i的最晚完成时间
                if lst[j] < lft[i]:
                    lft[i] = lst[j]
        lst[i] = lft[i] - duration[i]

    return lst, lft

'''
所有活动都执行的最晚开始时间
'''
def backwordPass(su,duration, lftn, actNo, mandatory):
    lst = [lftn - duration[i] for i in range(actNo)]
    lft = [0] * actNo
    lft[actNo-1] = lftn
    for i in range(actNo - 2, -1, -1):
        # 第一个紧后活动
        lft[i] = lst[su[i][0]]
        if len(su[i]) > 1:
            # 紧后活动
            for j in range(1, len(su[i])):
                if lft[i] > lst[su[i][j]]:
                    lft[i] = lst[su[i][j]]
        lst[i] = lft[i]-duration[i]

    return lst, lft
