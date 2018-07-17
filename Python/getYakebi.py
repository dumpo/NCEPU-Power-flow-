import global_variables as gb
import numpy as np

def caculate_ab():
    gb.a.clear()
    gb.b.clear()
    for i in range(1,gb.nBus):
        S=complex(gb.P[i-1],gb.Q[i-1])
        U=complex(gb.sBus[i].e,gb.sBus[i].f)
        # print(S)
        # print(U)
        gb.a.append((S/U).real)
        gb.b.append((S/U).imag)
    # print(gb.a)
    # print(gb.b)


def caculate_yakebi_H():
    for i in range(1,gb.nBus):
        temp=[]
        for j in range(1,gb.nBus):
            if i !=j:
                temp.append(gb.YG[i][j]*gb.sBus[i].f-gb.YB[i][j]*gb.sBus[i].e)
            else:
                temp.append(gb.YG[i][i]*gb.sBus[i].f-gb.YB[i][i]*gb.sBus[i].e+gb.b[i-1])
        gb.H.append(temp.copy())
        
def caculate_yakebi_N():
    for i in range(1,gb.nBus):
        temp=[]
        for j in range(1,gb.nBus):
            if i !=j:
                temp.append(gb.YG[i][j]*gb.sBus[i].e + gb.YB[i][j]*gb.sBus[i].f)
            else:
                temp.append(gb.YG[i][i]*gb.sBus[i].e + gb.YB[i][i]*gb.sBus[i].f+gb.a[i-1])
        gb.N.append(temp.copy())
        
        
def caculate_yakebi_J():
    for i in range(1,gb.nBus):
        temp=[]
        for j in range(1,gb.nBus):
            if i !=j:
                temp.append(-1*gb.YB[i][j]*gb.sBus[i].f-gb.YG[i][j]*gb.sBus[i].e)
            else:
                temp.append(-1*gb.YB[i][i]*gb.sBus[i].f-gb.YG[i][i]*gb.sBus[i].e+gb.a[i-1])
        gb.J.append(temp.copy())
        
def caculate_yakebi_L():
    for i in range(1,gb.nBus):
        temp=[]
        for j in range(1,gb.nBus):
            if i !=j:
                temp.append(gb.YG[i][j]*gb.sBus[i].f-gb.YB[i][j]*gb.sBus[i].e)
            else:
                temp.append(gb.YG[i][i]*gb.sBus[i].f-gb.YB[i][i]*gb.sBus[i].e-gb.b[i-1])
        gb.L.append(temp.copy())

def caculate_yakebi_R():
    for i in range(1,gb.nBus):
        temp=[]
        for j in range(1,gb.nBus):
            if i !=j:
                temp.append(0)
            else:
                temp.append(2*gb.sBus[i].f)
        gb.R.append(temp.copy())
        
def caculate_yakebi_S():
    for i in range(1,gb.nBus):
        temp=[]
        for j in range(1,gb.nBus):
            if i !=j:
                temp.append(0)
            else:
                temp.append(2*gb.sBus[i].e)
        gb.S.append(temp.copy())

def get_yakebi():
    caculate_ab()
    gb.H.clear()
    gb.N.clear()
    gb.J.clear()
    gb.L.clear()
    gb.R.clear()
    gb.S.clear()
    YAKEBI=[[0]*(2*(gb.nBus-1)) for i in range(2*(gb.nBus-1))]
    caculate_yakebi_H()
    caculate_yakebi_N()
    caculate_yakebi_J()
    caculate_yakebi_L()
    caculate_yakebi_R()
    caculate_yakebi_S()
    # for i in range(gb.num_PQ):
    #     for j in range(gb.num_PQ):
    #         YAKEBI[2*i][2*j]=gb.H[i][j]
    #         YAKEBI[2*i][2*j+1]=gb.N[i][j]
    #         YAKEBI[2*i+1][2*j]=gb.J[i][j]
    #         YAKEBI[2*i+1][2*j+1]=gb.L[i][j]    

    # for i in range(gb.num_PQ):
    #     for j in range(gb.num_PV):
    #         YAKEBI[2*i][2*gb.num_PQ+2*j]=gb.H[i][j+gb.num_PQ]
    #         YAKEBI[2*i][2*gb.num_PQ+2*j+1]=gb.N[i][j+gb.num_PQ]
    #         YAKEBI[2*i+1][2*gb.num_PQ+2*j]=gb.J[i][j+gb.num_PQ]
    #         YAKEBI[2*i+1][2*gb.num_PQ+2*j+1]=gb.L[i][j+gb.num_PQ]
            
    # for i in range(gb.num_PV):
    #     for j in range(gb.num_PQ):
    #         YAKEBI[2*gb.num_PQ+2*i][2*j]=gb.H[i+gb.num_PQ][j]
    #         YAKEBI[2*gb.num_PQ+2*i+1][2*j]=gb.N[i+gb.num_PQ][j]
    #         YAKEBI[2*gb.num_PQ+2*i][2*j+1]=gb.R[i+gb.num_PQ][j]
    #         YAKEBI[2*gb.num_PQ+2*i+1][2*j+1]=gb.S[i+gb.num_PQ][j]        
    
    # for i in range(gb.num_PV):
    #     for j in range(gb.num_PV):
    #         YAKEBI[2*gb.num_PQ+2*i][2*gb.num_PQ+2*j]=gb.H[i+gb.num_PQ][j+gb.num_PQ]
    #         YAKEBI[2*gb.num_PQ+2*i+1][2*gb.num_PQ+2*j]=gb.N[i+gb.num_PQ][j+gb.num_PQ]
    #         YAKEBI[2*gb.num_PQ+2*i][2*gb.num_PQ+2*j+1]=gb.R[i+gb.num_PQ][j+gb.num_PQ]
    #         YAKEBI[2*gb.num_PQ+2*i+1][2*gb.num_PQ+2*j+1]=gb.S[i+gb.num_PQ][j+gb.num_PQ]    
    for i in range(gb.nBus-1):
        for j in  range(gb.nBus-1):
            YAKEBI[2*i][2*j]=gb.H[i][j]
            YAKEBI[2*i][2*j+1]=gb.N[i][j]
            if (gb.sBus[i + 1].Type == 0):
                YAKEBI[2*i+1][2*j]=gb.J[i][j]
                YAKEBI[2*i+1][2*j+1]=gb.L[i][j]
            if (gb.sBus[i + 1].Type == 1):
                YAKEBI[2*i+1][2*j]=gb.R[i][j]
                YAKEBI[2*i+1][2*j+1]=gb.S[i][j]
    return YAKEBI

                
    
if __name__=="__main__":
    from getYMatrix import get_Y_matrix
    from getUnbalance import caculate_unbalance,set_bus_init_value,get_num_of_bus_type
    get_Y_matrix()
    get_num_of_bus_type()
    set_bus_init_value()
    caculate_unbalance()
    print(np.mat(get_yakebi()))
