
def calculate_es(nrsu, su, actNo, implement, duration):
    est = [0]*actNo
    eft = [0]*actNo
    # 设置第一个活动的紧后活动的est和lst
    for i in range(nrsu[0]):
        jinhou = su[0][i]
        if implement[jinhou]==1:
            eft[jinhou] = est[0]+duration[jinhou]
    for i in range(1,actNo):
        if implement[i]==1:
            for j in range(nrsu[i]):
                jinhou = su[i][j]
                if implement[jinhou] ==1:
                    if eft[i]>est[jinhou]:
                        est[jinhou] = eft[i]
                        eft[jinhou] = est[jinhou]+duration[jinhou]

    return est, eft

def calculate_ls(nrsu, su, actNo, implement, duration, lftn):
    lst = [0]*actNo
    lft = [0]*actNo
    lst[actNo-1] = lftn
    lft[actNo-1] = lftn
    for i in range(actNo - 2, -1, -1):
        if implement[i] == 1:
            for j in range(nrsu[i]):
                jinhou = su[i][j]
                if implement[jinhou] ==1:
                    lft[i] = lst[jinhou]
                    break
            if nrsu[i] > 1:
                for j in range(nrsu[i]):
                    jinhou = su[i][j]
                    if implement[jinhou]==1:
                        if lft[i] > lst[jinhou]:
                            lft[i] = lst[jinhou]
            lst[i] = lft[i]-duration[i]
    return lst, lft



