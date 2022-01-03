import numpy as np
def objValue(implement,schedule,actNo,resNo,duration,req,deadline,c):

    u=np.zeros((resNo,deadline))
    u_kt2=0
    for i in range(actNo):
        if implement[i]==1:
            for k in range(resNo):
                for t in range(schedule[i],schedule[i]+duration[i]):
                    u[k][t]+=req[i][k]

    all_u = np.multiply(u, u)
    for k in range(resNo):
        temp = all_u[k]
        u_kt2 += c[k]*np.sum(temp)
        # for t in range(deadline):
        #     u_kt2 += c[k]*u[k][t]*u[k][t]
    return u_kt2, u