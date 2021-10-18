list=[]

for i in range(0,1000+1):
        if i%3==0 or i%5==0:
            list.append(i)

print("The Total is " + str(sum(list)))

