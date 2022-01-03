import copy
def update_Relation(nrpr,nrsu,su,pred,choiceList,implementList,actNo):
    new_nrpr = copy.deepcopy(nrpr)
    new_nrsu = copy.deepcopy(nrsu)
    new_su = copy.deepcopy(su)
    new_pred = copy.deepcopy(pred)
    for i in choiceList:
        if implementList[i] == 0:
            # 不执行活动的紧前活动只有一个，在其紧后活动加actNo
            for j in range(new_nrpr[i]):
                jinqian = new_pred[i][j]
                if new_nrsu[jinqian] == 1:
                    new_nrsu[jinqian] += 1
                    new_su[jinqian].append(actNo-1)
                    # actNo的紧前活动添加jinqian
                    new_nrpr[actNo-1] += 1
                    new_pred[actNo-1].append(jinqian)

            # 不执行活动的紧后活动只有一个，在其紧后活动添加0
            for j in range(new_nrsu[i]):
                jinhou = new_su[i][j]
                if new_nrpr[jinhou] == 1:
                    new_nrpr[jinhou] +=1
                    new_pred[jinhou].append(0)
                    # 0的紧后活动添加jinhou
                    new_nrsu[0]+=1
                    new_su[0].append(jinhou)

    # 如果一个活动的所有紧后（紧前）活动都不执行
    for i in range(actNo):
        if implementList[i]==1:
            # 紧后
            count_s = 0
            for j in range(new_nrsu[i]):
                ss = new_su[i][j]
                # print(ss)
                if implementList[ss] == 0:
                    count_s += 1
            if count_s==new_nrsu[i]:
                new_nrsu[i]+=1
                new_su[i].append(actNo-1)
                new_nrpr[actNo-1] +=1
                new_pred[actNo-1].append(i)
            # 紧前
            count_p = 0
            for j in range(new_nrpr[i]):
                p = new_pred[i][j]
                if implementList[p]==0:
                    count_p += 1
            if count_p == new_nrpr[i]:
                new_nrpr[i]+=1
                new_pred[i].append(0)
                new_nrsu[0]+=1
                new_su[0].append(i)

    return new_nrpr, new_nrsu, new_pred, new_su




