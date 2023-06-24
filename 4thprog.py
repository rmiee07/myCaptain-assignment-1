lost=[]
fo=[]
c=0
N=int(input("The no.of elements in a list-"))
for i in range (0,N):
    ELE= int(input("the no.="))
    lost.append(ELE)
print (lost)
for i in range (0,N):
    if (lost[i]>=0):
        fo.append(lost[i])
print (fo)
        

     
       
