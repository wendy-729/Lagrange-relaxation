'''
求解子问题获得执行的活动和每个活动的开始时间
按开始时间升序排列得到活动列表
然后再根据每个活动的最早开始时间和最晚开始时间，调整活动，改进目标函数值
'''
from calculateES_LS import calculate_es, calculate_ls
# from change_implement import change_al, change_implement
from objValue import objValue


def local_search(schedule,nrsu, su, nrpr, pred, actNo, implement, duration, lftn, cost,resNo,req,ae, we, be, b):

    # 将进度计划转化为活动列表
    # al = [index for index,value in sorted(enumerate(schedule), key=lambda x:x[1])]


    # 交换活动的顺序
    # al = change_al(schedule, nrsu, su, nrpr, pred, actNo, implement, duration, lftn, cost, resNo, req)

    # 计算最早开始时间和最晚开始时间
    est, eft = calculate_es(nrsu, su, actNo, implement, duration)
    lst, lft = calculate_ls(nrsu, su, actNo, implement, duration, lftn)

    # 总时差
    tf = [0]*actNo
    for i in range(len(est)):
        tf[i] = lst[i]-est[i]
    al = [index for index, value in sorted(enumerate(tf), key=lambda x: x[1])]

    # 求解松弛子问题获得的进度计划对应的目标函数值
    obj, u_kt = objValue(implement,schedule, actNo, resNo, duration, req, lftn, cost)
    cb = obj
    # print(cb)
    # 资源均衡
    best_schedule = schedule
    change = 1
    while change == 1:
        change = 0
        for i in al:
            if implement[i] == 1:
                temp_schedule = best_schedule
                best_time = best_schedule[i]
                improvement = 0
                for j in range(nrpr[i]):
                    p = pred[i][j]
                    if implement[p] == 1:
                        est[i] = max(est[i], best_schedule[p]+duration[p])
                for j in range(nrsu[i]):
                    s = su[i][j]
                    if implement[s] == 1:
                        lst[i] = min(lst[i], best_schedule[s]-duration[i])
                for t in range(est[i], lst[i]+1):
                    temp_schedule[i] = t
                    pm, u_kt = objValue(implement, temp_schedule, actNo, resNo, duration, req, lftn, cost)
                    if pm < cb:
                        cb = pm
                        best_time = t
                        improvement = 1
                if improvement == 1:
                    best_schedule[i] = best_time
                    change = 1
    # print(cb)

    return best_schedule, cb
    # return est, cb
def local_search1(schedule,nrsu, su, nrpr, pred, actNo, implement, duration, lftn, cost,resNo,req,ae, we, be, b):
    # 计算最早开始时间和最晚开始时间
    est, eft = calculate_es(nrsu, su, actNo, implement, duration)
    lst, lft = calculate_ls(nrsu, su, actNo, implement, duration, lftn)

    # 总时差
    tf = [0] * actNo
    for i in range(len(est)):
        tf[i] = lst[i] - est[i]
    al = [index for index, value in sorted(enumerate(tf), key=lambda x: x[1])]

    # 求解松弛子问题获得的进度计划对应的目标函数值
    obj, u_kt = objValue(implement, schedule, actNo, resNo, duration, req, lftn, cost)
    cb = obj
    # print(cb)
    # 资源均衡
    best_schedule = schedule
    for i in al:
        if implement[i] == 1:
            temp_schedule = best_schedule
            best_time = best_schedule[i]
            improvement = 0
            for j in range(nrpr[i]):
                p = pred[i][j]
                if implement[p] == 1:
                    est[i] = max(est[i], best_schedule[p] + duration[p])
            for j in range(nrsu[i]):
                s = su[i][j]
                if implement[s] == 1:
                    lst[i] = min(lst[i], best_schedule[s] - duration[i])
            for t in range(est[i], lst[i] + 1):
                temp_schedule[i] = t
                pm, u_kt = objValue(implement, temp_schedule, actNo, resNo, duration, req, lftn, cost)
                if pm < cb:
                    cb = pm
                    best_time = t
                    improvement = 1
            if improvement == 1:
                best_schedule[i] = best_time
                # change = 1
    # print(cb)

    return best_schedule, cb




