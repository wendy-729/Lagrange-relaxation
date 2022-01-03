# 计算所有活动   正向计算
def forwardPass(duration, su):
    # 最早开始时间和最晚结束时间
    # su=su[mandatory]
    activities = len(duration)
    # print('activity',activities)
    est = [0] * len(duration)
    eft = [0] * len(duration)
    # 第一个活动的紧后活动的est.eft
    for i in su[0]:
        i = i-1
        eft[i] = est[i] + duration[i]
    # print(mandatory[2:])
    # 从第二个活动开始计算最早开始时间和最晚开始时间
    for i in range(2, activities):
        i = i-1
        # print(i)
        # print(su[i])
        for j in su[i]:
            j = j-1
            if eft[i] > est[j]:
                est[j] = eft[i]
                eft[j] = est[j] + duration[j]
    # print("活动的最晚开始时间", est)
    # print("活动的最晚结束时间", eft)
    return est, eft
