import random 
#list for 10,100. and 1000
one= 0 
two= 0
three= 0
four= 0
five= 0
six= 0
#Idk whats going on
nums= ("1","2","3","4","5","6")
numGen1 = random.randint(1,6)
timesGen= 0
listTen= []
#list and count variales 

#while(timesGen!=10):
for i in range(10):
  listTen.append(numGen1)
  nums[listTen[i]-1]+=1


  numGen1 = random.randint(1,6)
  timesGen= timesGen+1

  one+= 1
  two+= 1
  three+= 1
  four+= 1
  five+= 1

print(one)
print(two)
print(three)
print(four)
print(five)

