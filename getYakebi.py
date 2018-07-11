import gobal_variables as gb

def caculate_yakebi_H():
	for i in range(gb.nBus-1):
		temp=[]
		for j in range(gb.nBus-1):
			if i !=j:
				temp.append(YG[i][j]*gb.sBus[i].f-YB[i][j]*gb.sBus[i].e)
			else:
				t=0
				for k in range(gb.nBus):
					t=t - YG[i][k] * sBus[i].f + YB[i][k] * sBus[i].e
				t=t-YG[i][i] * sBus[i].f + YB[i][i] * sBus[i].e
				temp.append(t)
		gb.H.append(temp.copy())
        
def caculate_yakebi_N():
	for i in range(gb.nBus-1):
		temp=[]
		for j in range(gb.nBus-1):
			if i !=j:
				temp.append(YG[i][j]*gb.sBus[i].e + YB[i][j]*gb.sBus[i].f)
			else:
				t=0
				for k in range(gb.nBus):
					t=t - (YG[i][k] * sBus[i].e - YB[i][k] * sBus[i].f)
				t=t-YG[i][i] * sBus[i].e - YB[i][i] * sBus[i].f
				temp.append(t)
		gb.N.append(temp.copy())
        
        
def caculate_yakebi_J():
	for i in range(gb.nBus-1):
		temp=[]
		for j in range(gb.nBus-1):
			if i !=j:
				temp.append(-1*YB[i][j]*gb.sBus[i].f-YG[i][j]*gb.sBus[i].e)
			else:
				t=0
				for k in range(gb.nBus):
					t=t - (YG[i][k] * sBus[i].e - YB[i][k] * sBus[i].f)
				t=t+YG[i][i] * sBus[i].e + YB[i][i] * sBus[i].f
				temp.append(t)
		gb.J.append(temp.copy())
        
def caculate_yakebi_L():
	for i in range(gb.nBus-1):
		temp=[]
		for j in range(gb.nBus-1):
			if i !=j:
				temp.append(YG[i][j]*gb.sBus[i].f-YB[i][j]*gb.sBus[i].e)
			else:
				t=0
				for k in range(gb.nBus):
					t=t + YG[i][k] * sBus[i].f + YB[i][k] * sBus[i].e
				t=t-YG[i][i] * sBus[i].f + YB[i][i] * sBus[i].e
				temp.append(t)
                
		gb.L.append(temp.copy())

def caculate_yakebi_R():
	for i in range(gb.nBus-1):
		temp=[]
		for j in range(gb.nBus-1):
			if i !=j:
				temp.append(0)
			else:
				#TODO:
                temp.append(2*sBus[i].f)
		gb.R.append(temp.copy())
		
def caculate_yakebi_S():
	for i in range(gb.nBus-1):
		temp=[]
		for j in range(gb.nBus-1):
			if i !=j:
				temp.append(0)
			else:
				temp.append(2*sBus[i].f)
		gb.H.append(temp.copy())

def get_yakebi():
	YAKEBI=[[0]*(gb.nBus-1) for i in range(gb.nBus-1)]
	
	for i in range(gb.num_PQ):
		for j in range(gb.num_PQ):
			YAKEBI[2*i][2*j]=gb.H[i][j]
			YAKEBI[2*i+1][2*j]=gb.N[i][j]
			YAKEBI[2*i][2*j+1]=gb.J[i][j]
			YAKEBI[2*i+1][2*j+1]=gb.L[i][j]	

	for i in range(gb.num_PQ):
		for j in range(gb.num_PV):
			YAKEBI[2*gb.num_PQ-1+2*i][2*j]=gb.H[i][j+gb.num_PQ]
			YAKEBI[2*gb.num_PQ-1+2*i+1][2*j]=gb.N[i][j+gb.num_PQ]
			YAKEBI[2*gb.num_PQ-1+2*i][2*j+1]=gb.J[i][j+gb.num_PQ]
			YAKEBI[2*gb.num_PQ-1+2*i+1][2*j+1]=gb.L[i][j+gb.num_PQ]
			
	for i in range(gb.num_PV):
		for j in range(gb.num_PQ):
			YAKEBI[2*i][2*gb.num_PQ-1+2*j]=gb.H[i+gb.num_PQ][j]
			YAKEBI[2*i+1][2*gb.num_PQ-1+2*j]=gb.N[i+gb.num_PQ][j]
			YAKEBI[2*i][2*gb.num_PQ-1+2*j+1]=gb.R[i+gb.num_PQ][j]
			YAKEBI[2*i+1][2*gb.num_PQ-1+2*j+1]=gb.S[i+gb.num_PQ][j]		
	for i in range(gb.num_PV):
		for j in range(gb.num_PV):
			YAKEBI[2*gb.num_PQ-1+2*i][2*gb.num_PQ-1+2*j]=gb.H[i+gb.num_PQ][j+gb.num_PQ]
			YAKEBI[2*gb.num_PQ-1+2*i+1][2*gb.num_PQ-1+2*j]=gb.N[i+gb.num_PQ][j+gb.num_PQ]
			YAKEBI[2*gb.num_PQ-1+2*i][2*gb.num_PQ-1+2*j+1]=gb.R[i+gb.num_PQ][j+gb.num_PQ]
			YAKEBI[2*gb.num_PQ-1+2*i+1][2*gb.num_PQ-1+2*j+1]=gb.S[i+gb.num_PQ][j+gb.num_PQ]	
	return YAKEBI
				
	
if __name=="__main__":
	pass