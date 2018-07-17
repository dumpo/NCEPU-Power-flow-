import numpy as np
import global_variables as gb
from getYMatrix import get_Y_matrix
from getUnbalance import *
from getYakebi import get_yakebi

def update_ef(delta):
    # print(delta)
    delta_e=delta[1:2*gb.num_PQ:2]
    delta_f=delta[0:2*gb.num_PQ-1:2]
    for i in range(gb.num_PQ):
        gb.sBus[1+i].e=gb.sBus[1+i].e+delta_e[i]
        gb.sBus[1+i].f=gb.sBus[1+i].f+delta_f[i]
    # print(delta_e)
    # print(delta_f)
    delta_e=delta[2*gb.num_PQ+1:2*gb.nBus-2:2]
    delta_f=delta[2*gb.num_PQ:2*gb.nBus-1:2]
    for i in range(gb.num_PV):
        gb.sBus[gb.num_PQ+i].e=gb.sBus[gb.num_PQ+i].e+delta_e[i]
        gb.sBus[gb.num_PQ+i].f=gb.sBus[gb.num_PQ+i].f+delta_f[i]
        # gb.sBus[gb.num_PQ+i].Volt=gb.sBus[gb.num_PQ+i].e*gb.sBus[gb.num_PQ+i].e+
    # print(delta_e)
    # print(delta_f)


def solve():
    get_Y_matrix()
    set_bus_init_value()
    get_num_of_bus_type()

    # unbalabce=np.mat(caculate_unbalance()).T
    unbalabce=np.mat(caculate_unbalance()).T
    YAKEBI=np.mat(get_yakebi())
    J=YAKEBI.I
    delta=J*unbalabce 
    delta=delta.tolist()
    for i in range(len(delta)):
        delta[i]=delta[i][0]
    update_ef(delta)
    
    count=1
    print("第%d次迭代："%count)
    print("不平衡量")
    print(unbalabce)
    # print("雅可比矩阵")
    # print(YAKEBI)
    # print("雅可比矩阵逆矩阵")
    # print(J)
    print("电压修正量")
    print(delta)
    print("各节点电压")
    for i in range(1,gb.nBus):
        print(gb.sBus[i].e)
        print(gb.sBus[i].f)
    
    while True:
        unbalabce=np.mat(caculate_unbalance()).T
        YAKEBI=np.mat(get_yakebi())
        J=YAKEBI.I
        delta=J*unbalabce 
        delta=delta.tolist()
        for i in range(len(delta)):
            delta[i]=delta[i][0]
        update_ef(delta)

        count=count+1
        print("第%d次迭代："%count)
        print("不平衡量")
        print(unbalabce)
        # print("雅可比矩阵")
        # print(YAKEBI)
        # print("雅可比矩阵逆矩阵")
        # print(J)
        print("电压修正量")
        print(delta)
        print("各节点电压")
        for i in range(1,gb.nBus):
            print(gb.sBus[i].e)
            print(gb.sBus[i].f)

        if max(delta[0:2*gb.nBus-2:2])<=0.0001 and max(delta[1:2*gb.nBus-3:2])<=0.0001 :
            break

    print("收敛时各节点电压")
    for i in range(1,gb.nBus):
        print(gb.sBus[i].e)
        print(gb.sBus[i].f)
if __name__=="__main__":
    solve()
