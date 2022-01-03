# 逆向计算
def backwardPass(su,duration,lftn):
    activities = len(duration)
    lst = [0]*activities
    lft = [0]*activities
    # s设定最后一个活动的最晚开始时间和最晚完成时间
    lst[activities-1] = lftn
    lft[activities-1] = lftn

    for i in range(activities-2, -1, -1):
        j = su[i][0]-1

        lft[i] = lst[j]
        if len(su[i])>1:
               for x in range(1,len(su[i])):
                # y 为紧后活动
                    y = su[i][x]-1
                    if lft[i]>lst[y]:
                        lft[i] = lst[y]
        lst[i] = lft[i] - duration[i]
    # print("活动的最晚开始时间",lst)
    # print("活动的最晚结束时间",lft)
    return lst, lft