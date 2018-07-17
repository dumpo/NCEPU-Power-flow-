import global_variables as gb

class Line(object):
    def __init__(self,Num=0,NumI=0,NumJ=0,R=0,X=0,B=0,K=0):
        self.Num=Num
        self.NumI=NumI
        self.NumJ=NumJ
        self.R=R
        self.X=X
        self.B=B
        self.K=K

class Bus(object):
    def __init__(self,Num=0,Volt=0,Phase=0,GenP=0,GenQ=0,LoadP=0,LoadQ=0,Type=0):
        self.Num=Num
        self.Volt=Volt
        self.Phase=Phase
        self.GenP=GenP
        self.GenQ=GenQ
        self.LoadP=LoadP
        self.LoadQ=LoadQ
        self.Type=Type

def get_Y_matrix():

    f=open("E:\\coding\\潮流上机\\Python\\in.txt","r")
    line=''.join(f.readline()).rstrip("\n").split(",")
    gb.nBus=int(line[0])
    gb.nL=int(line[1])
    gb.nSH=int(line[2])
    f.close
    for i in range(gb.nBus):
        line="".join(f.readline()).rstrip("\n").split(",")
        # print(line)
        i1=int(line[0])
        d1=float(line[1])
        d2=float(line[2])
        d3=float(line[3])
        d4=float(line[4])
        d5=float(line[5])
        d6=float(line[6])
        i2=int(line[7])
        gb.sBus.append(Bus(i1,d1,d2,d3,d4,d5,d6,i2))
        

    for i in range(gb.nL):
        line="".join(f.readline()).split()
        line=' '.join(line).split(",")
        i1=int(line[0])
        i2=int(line[1])
        i3=int(line[2])
        d1=float(line[3])
        d2=float(line[4])
        d3=float(line[5])
        d4=float(line[6])
        gb.sLine.append(Line(i1,i2,i3,d1,d2,d3,d4))

    # print(line)

    for i in range(gb.nSH):
        line="".join(f.readline())
        # print(line)
        pass

    #make Y Matrix
    for i in range(gb.nBus):
        temp=[]
        for j in range(gb.nBus):
            temp.append(0)
            # print(temp)
        gb.YB.append(temp.copy())
        gb.YG.append(temp.copy())

    for l in range(gb.nL):
        i=gb.sLine[l].NumI-1
        j=gb.sLine[l].NumJ-1
        r=gb.sLine[l].R
        x=gb.sLine[l].X
        d1=r*r+x*x
        g=r/d1
        b=-1*x/d1
        m=gb.sLine[l].K
    #普通支路
        if(gb.sLine[l].K==0):
            gb.YG[i][i]=gb.YG[i][i]+g
            gb.YG[j][j]=gb.YG[j][j]+g
            gb.YB[i][i]=gb.YB[i][i]+b+gb.sLine[l].B
            gb.YB[j][j]=gb.YB[j][j]+b+gb.sLine[l].B
            gb.YG[i][j]=gb.YG[i][j]-g
            gb.YG[j][i]=gb.YG[j][i]-g
            gb.YB[i][j]=gb.YB[i][j]-b
            gb.YB[j][i]=gb.YB[j][i]-b
        else:
            gb.YG[i][i]=gb.YG[i][i]+g/m+g*(m-1)/m
            gb.YG[j][j]=gb.YG[j][j]+g/m+g*(1-m)/m/m
            gb.YB[i][i]=gb.YB[i][i]+b/m+b*(m-1)/m
            gb.YB[j][j]=gb.YB[j][j]+b/m+b*(1-m)/m/m
            gb.YG[i][j]=gb.YG[i][j]-g/m
            gb.YG[j][i]=gb.YG[j][i]-g/m
            gb.YB[i][j]=gb.YB[i][j]-b/m
            gb.YB[j][i]=gb.YB[j][i]-b/m
            # g1=g/gb.sLine[i].K
            # b1=b/gb.sLine[i].K
            # g2=g*(gb.sLine[i].K-1)/gb.sLine[i].K
            # b2=b*(gb.sLine[i].K-1)/gb.sLine[i].K
            # g3=g*(1-gb.sLine[i].K)/(gb.sLine[i].K*gb.sLine[i].K)
            # b3=b*(1-gb.sLine[i].K)/(gb.sLine[i].K*gb.sLine[i].K)

            # gb.YG[i][i]=gb.YG[i][i]+g1+g2
            # gb.YG[j][j]=gb.YG[j][j]+g1+g3
            # gb.YG[i][j]=gb.YG[i][j]-g1
            # gb.YG[j][i]=gb.YG[j][i]-g1
            # gb.YB[i][i]=gb.YB[i][i]+b1+b2
            # gb.YB[j][j]=gb.YB[j][j]+b1+b3
            # gb.YB[i][j]=gb.YB[i][j]-b1
            # gb.YB[j][i]=gb.YB[j][i]-b1

    #check Y matrix
    f=open("E:\\coding\\潮流上机\\python\\GGBB.txt","w")
    f.write("---Y Matrix---\n")
    for i in range(gb.nBus):
        for j in range(gb.nBus):
            if(abs(gb.YB[i][j])>0.00001):
                f.write("Y(%3d,%-3d)=(%10.5f,%10.5f)\n"%(i+1,j+1,gb.YG[i][j],gb.YB[i][j]))
    f.close()
    
if __name__=="__main__":
    get_Y_matrix()