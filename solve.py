import numpy as np
import global_variables as gb
from getYMatrix import get_Y_matrix
from getUnbalance import get_unbalance
from getYakebi import get_yakebi

def update_ef(delta_e,delta_f):
    for i in range(1,gb.nBus):
        gb.sBus[i].e=delta_e[i-1]
        gb.sBus[i].f=delta_f[i-1]


def solve():
    get_Y_matrix()
    while True:
        unbalabce=np.mat(get_unbalance()).T #??
        print(unbalabce)
        YAKEBI=np.mat(get_yakebi()).I #???
        print(YAKEBI)
        delta=YAKEBI*unbalabce 
        print(delta)
        update_ef(delta[0:gb.nBus-1],delta[gb.nBus-1:2*gb.nBus-2])
        if max(delta[0:gb.nBus-1])<=0.00001 and max(delta[gb.nBus-1:2*gb.nBus-2])<=0.00001 :
            break
    
if __name__=="__main__":
    solve()