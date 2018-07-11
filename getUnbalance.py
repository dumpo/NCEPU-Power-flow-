import gobal_variables as gb

def coordinate_tranform(Volt,Phase):
	e=Volt*cos(Phase)
	f=Volt*sin(Phase)
	return e,f
	
def set_bus_init_value():
	for i in range(gb.nBus):
		if sBus[i].Type==1:
			sBus[i].e,sBus[i].f=coordinate_tranform(sBus[i].Volt,sBus[i].Phase)
		if sBus[i].Type==0:
			sBus[i].e=1
			sBus[i].f=0
			

def caculate_unbalance(caculate_type):
	for i in range(n):
		result_list=[]
		result=0
			if sBus[i].Type==2:
				#result=0
				pass
			else:
				if caculate_type=='P':
					for j in range(n):
						result=result+sBus[i].e*(YG[i][j]*sBus[i].e-YB[i][j]*sBus[i].f)+sBus[i].f*(YG[i][j]*sBus[i].f+YB[i][j]*sBus[i].e)
					if(sBus[i].Type==0):
						result=sBus[i].GenP-sBus[i].LoadP-result
					elif(sBus[i].Type==1):
						result=result-sBus[i].LoadP
				if caculate_type=='Q':
					for j in range(n):
						result=result+sBus[i].f*(YG[i][j]*sBus[i].e-YB[i][j]*sBus[i].f)-sBus[i].e*(YG[i][j]*sBus[i].f+YB[i][j]*sBus[i].e)
					if(sBus[i].Type==0):
						result=sBus[i].GenP-sBus[i].LoadP-result
					elif(sBus[i].Type==1):
						result=result-sBus[i].LoadQ
				if caculate_type=='U':
					result=sBus[i].Volt * sBus[i].Volt - (sBus[i].e * sBus[i].e + sBus[i].f * sBus[i].f)
			result_list.append(result)
	return result_list
def get_unbalance():
	dP_list=caculate_unbalance('P')
	dQ_list=caculate_unbalance('Q')
	dU_list=caculate_unbalance('U')
	return dP_list+dP_list+dP_list
	
def get_num_of_bus_type():
	for i in range(gb.nBus):
		if sBus[i].Type==0:
			gb.num_PQ=gb.num_PQ+1
			#gb.PQ_list.append(sBus[i].Num)

		if sBus[i].Type==1:
			gb.num_PV=gb.num_PV+1
			#gb.PV_list.append(sBus[i].Num)

if __name=="__main__":
	pass