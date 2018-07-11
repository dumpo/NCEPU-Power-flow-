import numpy as np
import gobal_variables as gb
from getYMatrix import get_Y_matrix
from get_unbalance import get_unbalance
from getYakebi import get_yakebi

def update_ef(e,f):
	for i in range(1,gb,nBus-1):
		

def solve():
	get_Y_matrix()
	get_num_of_bus_type()
	
	while True:
		YAKEBI=np.mat(get_yakebi())#.求逆
		unbalabce=np.mat(get_unbalance())#.翻转
		delta=YAKEBI*unbalabce
		
		if max(delta[0:gb.nBus-1])<=0.00001 and max(delta[gb.nBus-1:2*gb.nBus-2])<=0.00001 :
			break
if __name=="__main__":
	solve()