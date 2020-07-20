import random 

one= 0 
two= 0
three= 0
four= 0
five= 0
six= 0

nums= ("1","2","3","4","5","6")
numGen1 = random.randint(1,6)
timesGen= 0

while(timesGen!=10):
  numGen1 = random.randint(1,6)

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

