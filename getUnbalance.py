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
        
            

# def caculate_unbalance(caculate_type,i):
#     if gb.sBus[i].Type==2:
#         #result=0
#         return
#     else:
#         if caculate_type=='P'and gb.sBus[i].Type==0:
#             for j in range(gb.nBus):
#                 gb.P[i-1]=gb.P[i-1]+(gb.sBus[i].e*(gb.YG[i][j]*gb.sBus[j].e-gb.YB[i][j]*gb.sBus[j].f)+gb.sBus[i].f*(gb.YG[i][j]*gb.sBus[j].f+gb.YB[i][j]*gb.sBus[j].e))
#             result=gb.sBus[i].GenP-gb.sBus[i].LoadP-gb.P[i-1]
#             return result
#         if caculate_type=='Q' and gb.sBus[i].Type==0:
#             for j in range(gb.nBus):
#                 gb.Q[i-1]=gb.Q[i-1]+(gb.sBus[i].f*(gb.YG[i][j]*gb.sBus[j].e-gb.YB[i][j]*gb.sBus[j].f)-gb.sBus[i].e*(gb.YG[i][j]*gb.sBus[j].f+gb.YB[i][j]*gb.sBus[j].e))
#             result=gb.sBus[i].GenQ-gb.sBus[i].LoadQ-gb.Q[i-1]
#             return result
#         if caculate_type=='U' and gb.sBus[i].Type==1:
#             result=gb.sBus[i].Volt * gb.sBus[i].Volt - (gb.sBus[i].e * gb.sBus[i].e + gb.sBus[i].f * gb.sBus[i].f)
#             return result
    

# def get_unbalance():
#     dP_list=[]
#     dQ_list=[]
#     temp=[]
#     for i in range(gb.num_PQ):
#         dP_list.append(caculate_unbalance('P',i+1))
#         dQ_list.append(caculate_unbalance('Q',i+1))

#     for i in range(gb.num_PQ):
#         temp.append(dP_list[i])
#         temp.append(dQ_list[i])
    
#     dP_list=[]
#     dU_list=[]

#     for i in range(gb.num_PQ,gb.nBus-1):
#         dP_list.append(caculate_unbalance('P',i+1))
#         dU_list.append(caculate_unbalance('U',i+1))

#     for i in range(gb.num_PQ,gb.nBus-1):
#         temp.append(dP_list[i])
#         temp.append(dU_list[i])
    
#     return temp
    
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

    for i in range(gb.num_PQ,gb.nBus-1):
        for j in range(gb.nBus):
            gb.P[i-1]=gb.P[i-1]+(gb.sBus[i].e*(gb.YG[i][j]*gb.sBus[j].e-gb.YB[i][j]*gb.sBus[j].f)+gb.sBus[i].f*(gb.YG[i][j]*gb.sBus[j].f+gb.YB[i][j]*gb.sBus[j].e))
        result=gb.sBus[i].GenP-gb.sBus[i].LoadP-gb.P[i-1]
        dP_list.append(result)

        for j in range(gb.nBus):
            result=gb.sBus[i].Volt * gb.sBus[i].Volt - (gb.sBus[i].e * gb.sBus[i].e + gb.sBus[i].f * gb.sBus[i].f)
        dU_list.append(result)

    for i in range(gb.num_PV):
        temp.append(dP_list[i])
        temp.append(dU_list[i])
    return temp

def caculate_unbalance():
    temp=caculate_unbalance_PQ()
    temp.extend(caculate_unbalance_PV())
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

    gb.sBus[1].e=1.04296
    gb.sBus[1].f=-0.04729
    gb.sBus[2].e=1.01539
    gb.sBus[2].f=-0.08629
    gb.sBus[3].e=1.0141
    gb.sBus[3].f=-0.09223
    gb.sBus[4].e=1.00934
    gb.sBus[4].f=-0.10761

    print(caculate_unbalance())