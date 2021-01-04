smallpp='Hello World'
bigpp=''
f=0
for i in smallpp:
    while f==0:
        print("Enter",i,' : ',end='')
        temp=input()
        if temp!=i:
            print("U SMALLPP PERSON... TRY AGAIN...")
            continue
        f=1
        bigpp+=temp
    f=0
l1=[]
l2=[]
for i in bigpp:
    l1.append(i)
for i in l1:
    l2.append(ord(i))
d={}
for i in l2:
    d[chr(i)]= d.get(chr(i),0) + 1
D={}
T=[]
D2={}
indr=0
indn=0
for i,j in d.items():
    if j>1:
        for k in l2:
            if(chr(k)==i):
                T.append(indr)
            indr+=1
        indr=0
        D[i]=T
        T=[]
    if j==1:
        for k in l2:
            if(chr(k)==i):
                T.append(indn)
            indn+=1
        indn=0
        D2[i]=T
        T=[]
bruh=[]
for i in range(len(l2)):
    bruh.append('')
c=0
Bla=[]
dummy=0
for i in D.values():
    for j in i:
        Bla.append(j)
for i in d.keys():
    if i in D.keys():
        for j in D[i]:
            bruh[j]=i
for i in d.keys():
    if i in D2.keys():
        for j in D2[i]:
            bruh[j]=i
for i in bruh:
    print(i,end='')
        
    
        
         
    
        
    
    
    


        
            
    
    
    
