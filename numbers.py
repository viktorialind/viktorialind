
for i in range(10,100): #vel allar 2 stafa tolur thar sem 100 er ekki tekid med
    if ((i//10)+(i%10))**2==i: 
        print (i)
for i in range (1,100):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1 # haekka breytuna count um 1 i gegnum hverja itrun
    if count==10: 
        print(i)