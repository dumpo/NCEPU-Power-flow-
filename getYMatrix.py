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
    # NBUS=5
    # NLINE=7
    # #global variables
    # X=[]
    # def_self=[]
    sBus=[]
    sLine=[]
    YG=[]
    YB=[]


    f=open("E:\\1151600307\\in.txt","r")
    line=''.join(f.readline()).rstrip("\n").split(",")
    nBus=int(line[0])
    nL=int(line[1])
    nSH=int(line[2])
    f.close

    for i in range(nBus):
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
        sBus.append(Bus(i1,d1,d2,d3,d4,d5,d6,i2))
        

    for i in range(nL):
        line="".join(f.readline()).split()
        line=' '.join(line).split(" ")
        i1=int(line[0])
        i2=int(line[1])
        i3=int(line[2])
        d1=float(line[3])
        d2=float(line[4])
        d3=float(line[5])
        d4=float(line[6])
        sLine.append(Line(i1,i2,i3,d1,d2,d3,d4))

    print(line)

    for i in range(nSH):
        line="".join(f.readline())
        print(line)
        pass

    #make Y Matrix
    for i in range(nBus):
        temp=[]
        for j in range(nBus):
            temp.append(0)
            # print(temp)
        YB.append(temp.copy())
        YG.append(temp.copy())

    for l in range(nL):
        i=sLine[l].NumI-1
        j=sLine[l].NumJ-1
        r=sLine[l].R
        x=sLine[l].X
        d1=r*r+x*x
        g=r/d1
        b=-1*x/d1
        m=sLine[1].K
    #普通支路
        if(abs(sLine[l].K-1)<0.00001):
            YG[i][i]=YG[i][i]+g
            YG[j][j]=YG[j][j]+g
            YB[i][i]=YB[i][i]+b+sLine[l].B
            YB[j][j]=YB[j][j]+b+sLine[l].B
            YG[i][j]=YG[i][j]-g
            YG[j][i]=YG[j][i]-g
            YB[i][j]=YB[i][j]-b
            YB[j][i]=YB[j][i]-b
        else:
            #TODO 变压器支路
            pass

    #check Y matrix
    f=open("E:\\1151600307\\GGBB.txt","w")
    f.write("---Y Matrix---\n")
    for i in range(nBus):
        for j in range(nBus):
            if(abs(YB[i][j])>0.00001):
                f.write("Y(%3d,%-3d)=(%10.5f,%10.5f)\n"%(i+1,j+1,YG[i][j],YB[i][j]))
    f.close()