import gobal_variables as gb
from get_unbalance import caculate_unbalance

def caculate_yakebi_H():
	for i in range(gb.nBus-1):
		temp=[]
		for j in range(gb.nBus-1):
			if i !=j:
				temp.append(YG[i][j]*gb.sBus[i].f-YB[i][j]*gb.sBus[i].e)
			else:
				
		gb.H.append(temp.copy())

	