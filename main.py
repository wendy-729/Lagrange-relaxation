'''
改了计算活动最晚开始时间的方法
'''
import numpy as np


from pandas import DataFrame
from time import *
from docplex.mp.model import Model

# 设置线程数量
# sem=threading.Semaphore(1)
from Dual_Problem import Main
# from Dual_Problem_Pr import Main_Pr
# from Dual_Problem_u_kt import Main_u_kt
# from Subproblem import consturct_lagrangian_relaxation
from backward import backward_update
from backwardPass import backwardPass
from forward import forwardManda
from forwardPass import forwardPass
from initChoice import initChoice
from initCost import initCost
from initData import initData
from initfile import initfile
# from newProjectData import newProjectData
# from newProjectData1 import newProjectData1
from read_data import read_data, read_data_ga

dtimes = [1]
noact = [38, 45, 51, 61, 93, 104, 112, 132, 157]
# 活动数量
act = [120]
M = 1e10
for dtime in dtimes:
    for actNumber in act:
        # 读取最优实例
        # filename_opt = r'D:\研究生资料\RLP-PS汇总\实验结果\CPLEX\J' + str(actNumber) + '\\' + 'sch_rlp_' + str(
        #     actNumber + 2) + '_dtime_' + str(dtime) + '.txt'
        # actSet = read_data(filename_opt)
        # 第几组数据
        for group in range(4, 5):
            # 第几个实例
            # for project in actSet:
            for project in range(25, 100):
                print('instance', project)
            # for project in range(1, 2):
            # 读取GA获得的目标函数值
                file_ga = r'D:\研究生资料\RLP-PS汇总\大修\大修实验结果final\GA1\J' + str(actNumber) + '\\' + str(
                    group) + '\\' + '5000sch_rlp_' + str(actNumber+2)+ '_dtime_' + str(dtime) + '.txt'
                upper_bound_data = read_data_ga(file_ga)
                upper_bound = upper_bound_data[project-1]
                # upper_bound = 1e10
                # print(upper_bound)

                begin_time = time()

                filename = r'C:\Users\ASUS\Desktop\拉格朗日松弛模型\J'+ str(actNumber)+'\\'+'lagranger_lower_ga_'+str(dtime)+'_'+'.txt'
                # 大修路径
                # filename = r'D:\研究生资料\RLP-PS汇总\第五次投稿-Annals of Operations Research\ANOR大修\CPLEX\J'+ str(actNumber) +'\\' + 'sch_rlp_vl_' + str(actNumber + 2) + '_dtime_' + str(dtime) + '.txt'

                with open(filename, 'a', newline='') as f:
                    file = r'D:\研究生资料\RLP-PS汇总\实验数据集\PSPLIB\j' + str(actNumber) + '\\J' + str(
                        actNumber) + '_' + str(project) + '.RCP'
                    # 初始化数据
                    res, duration, su, pred, req, activities, provide_res,nrpr, nrsu = initData(file)

                    # 处理紧前活动，从0开始编号
                    projPred = []
                    for i in range(1, len(pred)):
                        temp = pred[i]
                        temp = [i - 1 for i in temp]
                        projPred.append(temp)
                    projPred.insert(0, [])

                    # 紧后活动从0开始编号
                    proSu = []
                    for i in range(0, len(su)):
                        temp = su[i]
                        temp1 = [j - 1 for j in temp]
                        proSu.append(temp1)
                    # 柔性结构数据
                    datafile = r'D:\研究生资料\RLP-PS汇总\实验数据集\J'
                    # 必须执行的活动
                    fp_mandatory = datafile + str(actNumber) + '\\' + str(
                        group) + '\\mandatory\\J' + str(actNumber) + '_' + str(project) + '.txt'

                    mandatory = initfile(fp_mandatory)
                    # 可选集合
                    fp_choice = datafile + str(actNumber) + '\\' + str(
                        group) + '\\choice\\J' + str(actNumber) + '_' + str(project) + '.txt'
                    choice = initChoice(fp_choice)
                    choice = np.array(choice)

                    # 所有可选活动
                    fp_choiceList = datafile + str(actNumber) + '\\' + str(
                        group) + '\\choiceList\\J' + str(actNumber) + '_' + str(project) + '.txt'
                    choiceList = initfile(fp_choiceList)

                    # 依赖活动
                    fp_depend = datafile + str(actNumber) + '\\' + str(
                        group) + '\\dependent\\J' + str(actNumber) + '_' + str(project) + '.txt'
                    depend = initChoice(fp_depend)
                    depend = np.array(depend)

                    # 成本
                    fp_cost = r'D:\研究生资料\RLP-PS汇总\实验数据集\cost.txt'
                    Costs = initCost(fp_cost)
                    cost = Costs[project - 1]

                    # 触发活动
                    ae = []
                    for i in range(0, choice.shape[0]):
                        ae.append(choice[i][0])
                    # we 可选活动集合
                    we = []
                    for i in range(0, choice.shape[0]):
                        temp = choice[i][1:]
                        we.append(temp)

                    # 触发依赖活动的可选活动
                    be = []
                    for i in range(0, depend.shape[0]):
                        be.append(depend[i][0])

                    # 依赖活动
                    b = []
                    for i in range(0, depend.shape[0]):
                        temp = depend[i][1:]
                        b.append(temp)
                    # # 考虑更新网络结构中的优先关系
                    # proSu, projPred = newProjectData1(proSu, projPred, choiceList, activities, mandatory)

                    # 考虑了所有活动的最早开始
                    est_1, eft_1 = forwardPass(duration, su)
                    lftn = int(dtime * est_1[activities - 1])

                    # # 最晚开始时间  考虑了所有活动
                    lst_1, lft_1 = backwardPass(su, duration, lftn)
                    # est_s = [0]*activities
                    # lst_s = [lftn - duration[i] for i in range(activities)]

                    est_s, eft_s = forwardManda(duration, proSu, mandatory, activities, projPred)
                    # 所有活动都执行
                    lst_s, lft_s = backward_update(proSu, duration, lftn, activities, mandatory)

                    # 计算资源占用量  所有活动都执行
                    u_kt = np.zeros((res, lftn+1), dtype=int)
                    dur = list(map(lambda x: x[0] - x[1], zip(lft_1, est_1)))

                    for i in range(0, activities):
                        for k in range(0, res):
                            for t in range(est_1[i], est_1[i] + dur[i]):
                                u_kt[k][t] = u_kt[k][t] + req[i][k]
                    max_h = []
                    for i in range(0, res):
                        h = max(u_kt[i])
                        max_h.append(h)


                    # 最大资源占用量
                    max_H = max(max_h)
                    # 最大的迭代次数
                    max_iter = 300

                    # # 松弛优先关系约束
                    # mf = Main_Pr(res, lftn + 1, activities, max_H)
                    # best_lb, best_ub, gap = mf.solve_subgradient(max_iter, res, max_H, lftn, activities, cost, req,
                    #                                              est_s, lst_s, duration, mandatory, ae, we, be, b,
                    #                                              projPred, nrpr, nrsu, proSu, choiceList, res, u_kt)

                    # 松弛计算资源使用量约束
                    mf = Main(res, lftn + 1, activities, max_H,upper_bound)
                    best_lb, best_ub, gap = mf.solve_subgradient(max_iter, res, max_H, lftn, activities, cost, req, est_s, lst_s, duration, mandatory, ae, we, be, b,
                                          projPred, nrpr, nrsu, proSu, choiceList,res,u_kt)

                    # u_kt
                    # mf = Main_u_kt(res, lftn + 1, activities, max_H)
                    # best_lb, best_ub, gap = mf.solve_subgradient(max_iter, res, max_H, lftn, activities, cost, req,
                    #                                                       est_s, lst_s, duration, mandatory, ae, we, be, b,
                    #                                                       projPred, nrpr, nrsu, proSu, choiceList, res, u_kt)

                    end_time = time()
                    run_time = end_time-begin_time
                    results = str(project) + '\t' + format(best_lb,'.2f') + '\t' + format(best_ub,'.2f') + '\t' + format(gap,'.2f')+ '\t'+format(run_time,'.2f')+'\n'
                    print(results)
                    f.write(results)
                    print(project, 'is solved')
                    # print(end_time-begin_time)

                    # objvalue, opt_x_it, opt_y_kth = consturct_lagrangian_relaxation(mu_kt, res, max_H, lftn, activities, cost, req, est_s, lst_s,
                    #                                 duration, mandatory, ae, we, be, b, projPred, actNumber)

