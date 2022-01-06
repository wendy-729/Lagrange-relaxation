# 郑淋文
# 时间: 2022/1/5 17:11
'''
考虑进一步提升松弛模型得到的下界
'''
def lower_bound(al, req,deadline,resNo,duration,c):
    lower_bound_require = 0
    mean_res = [0]*resNo
    for k in range(resNo):
        all_require_res = 0
        for i in al:
            all_require_res += req[i][k]*duration[i]
        mean_res[k] = all_require_res/deadline
    for k in range(resNo):
        for t in range(deadline):
            lower_bound_require += c[k]*mean_res[k]*mean_res[k]
    return lower_bound_require
