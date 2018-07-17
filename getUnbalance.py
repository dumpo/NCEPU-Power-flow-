import global_variables as gb
from math import cos,sin
import numpy as np

def coordinate_tranform(Volt,Phase):
    e=Volt*cos(Phase)
    f=Volt*sin(Phase)
    return e,f
    
def set_bus_init_value():
    for i in range(gb.nBus):
        if gb.sBus[i].Type==1 or gb.sBus[i].Type==2:
            gb.sBus[i].e,gb.sBus[i].f=coordinate_tranform(gb.sBus[i].Volt,gb.sBus[i].Phase)
        if gb.sBus[i].Type==0:
            gb.sBus[i].e=1
            gb.sBus[i].f=0
        
            


    
def caculate_unbalance_PQ():
    dP_list=[]
    dQ_list=[]
    temp=[]
    gb.P=[0 for i in range(gb.nBus-1)]
    gb.Q=[0 for i in range(gb.nBus-1)]
    for i in range(1,gb.num_PQ+1):
        for j in range(gb.nBus):
            gb.P[i-1]=gb.P[i-1]+(gb.sBus[i].e*(gb.YG[i][j]*gb.sBus[j].e-gb.YB[i][j]*gb.sBus[j].f)+gb.sBus[i].f*(gb.YG[i][j]*gb.sBus[j].f+gb.YB[i][j]*gb.sBus[j].e))
        result=gb.sBus[i].GenP-gb.sBus[i].LoadP-gb.P[i-1]
        dP_list.append(result)

        for j in range(gb.nBus):
            gb.Q[i-1]=gb.Q[i-1]+(gb.sBus[i].f*(gb.YG[i][j]*gb.sBus[j].e-gb.YB[i][j]*gb.sBus[j].f)-gb.sBus[i].e*(gb.YG[i][j]*gb.sBus[j].f+gb.YB[i][j]*gb.sBus[j].e))
        result=gb.sBus[i].GenQ-gb.sBus[i].LoadQ-gb.Q[i-1]
        dQ_list.append(result)

    for i in range(gb.num_PQ):
        temp.append(dP_list[i])
        temp.append(dQ_list[i])
    return temp


def caculate_unbalance_PV():
    dP_list=[]
    dU_list=[]
    temp=[]
    gb.P=[0 for i in range(gb.nBus-1)]
    for i in range(gb.num_PQ,gb.num_PQ+gb.num_PV):
        for j in range(gb.nBus):
            gb.P[i-1]=gb.P[i-1]+(gb.sBus[i].e*(gb.YG[i][j]*gb.sBus[j].e-gb.YB[i][j]*gb.sBus[j].f)+gb.sBus[i].f*(gb.YG[i][j]*gb.sBus[j].f+gb.YB[i][j]*gb.sBus[j].e))
        result=gb.sBus[i].GenP-gb.sBus[i].LoadP-gb.P[i-1]
        dP_list.append(result)

        result=gb.sBus[i].Volt * gb.sBus[i].Volt - (gb.sBus[i].e * gb.sBus[i].e + gb.sBus[i].f * gb.sBus[i].f)
        dU_list.append(result)

    for i in range(gb.num_PV):
        temp.append(dP_list[i])
        temp.append(dU_list[i])
    return temp

def caculate_unbalance_old():
    temp=caculate_unbalance_PQ()
    temp.extend(caculate_unbalance_PV())
    return temp




def caculate_unbalance():
    temp=[]
    gb.P=[0 for i in range(gb.nBus-1)]
    gb.Q=[0 for i in range(gb.nBus-1)]
    for i in range(1,gb.nBus):
        for j in range(gb.nBus):
            gb.P[i-1]=gb.P[i-1]+(gb.sBus[i].e*(gb.YG[i][j]*gb.sBus[j].e-gb.YB[i][j]*gb.sBus[j].f)+gb.sBus[i].f*(gb.YG[i][j]*gb.sBus[j].f+gb.YB[i][j]*gb.sBus[j].e))
        result=gb.sBus[i].GenP-gb.sBus[i].LoadP-gb.P[i-1]
        # dP_list.append(result)
        temp.append(result)
        
        if(gb.sBus[i].Type==0):
            for j in range(gb.nBus):
                gb.Q[i-1]=gb.Q[i-1]+(gb.sBus[i].f*(gb.YG[i][j]*gb.sBus[j].e-gb.YB[i][j]*gb.sBus[j].f)-gb.sBus[i].e*(gb.YG[i][j]*gb.sBus[j].f+gb.YB[i][j]*gb.sBus[j].e))
            result=gb.sBus[i].GenQ-gb.sBus[i].LoadQ-gb.Q[i-1]
            temp.append(result)
            # dQ_list.append(result)
        
        if(gb.sBus[i].Type==1):
            result=gb.sBus[i].Volt * gb.sBus[i].Volt - (gb.sBus[i].e * gb.sBus[i].e + gb.sBus[i].f * gb.sBus[i].f)
            # dU_list.append(result)
            temp.append(result)
    return temp

def get_num_of_bus_type():
    for i in range(gb.nBus):
        if gb.sBus[i].Type==0:
            gb.num_PQ=gb.num_PQ+1
            #gb.PQ_list.append(gb.sBus[i].Num)

        if gb.sBus[i].Type==1:
            gb.num_PV=gb.num_PV+1
            #gb.PV_list.append(gb.sBus[i].Num)

if __name__=="__main__":
    from getYMatrix import get_Y_matrix
    get_Y_matrix()
    get_num_of_bus_type()
    set_bus_init_value()

    # gb.sBus[1].e=1.04296
    # gb.sBus[1].f=-0.04729
    # gb.sBus[2].e=1.01539
    # gb.sBus[2].f=-0.08629
    # gb.sBus[3].e=1.0141
    # gb.sBus[3].f=-0.09223
    # gb.sBus[4].e=1.00934
    # gb.sBus[4].f=-0.10761

    # gb.sBus[1].e=0.9583438241857334
    # gb.sBus[1].f=-0.11565421516431548
    # gb.sBus[2].e=0.9137820468041138
    # gb.sBus[2].f=-0.1908138259421677
    # gb.sBus[3].e=1.0052093756481688
    # gb.sBus[3].f=-0.10429823839958531
    # gb.sBus[4].e=1.0198410707965093
    # gb.sBus[4].f=-0.11002598559502107
    # gb.sBus[5].e=0.978276160905726
    # gb.sBus[5].f=-0.16710530644287236
    # gb.sBus[6].e=1.002185102344255
    # gb.sBus[6].f=-0.23430554974625123
    # gb.sBus[7].e=0.9882907003144221
    # gb.sBus[7].f=-0.11814667159072197
    # gb.sBus[8].e=1.025
    # gb.sBus[8].f=0.0
    print(caculate_unbalance())

    # print(len(caculate_unbalance()))