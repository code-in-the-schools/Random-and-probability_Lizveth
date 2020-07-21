import random 
#list for 10,100. and 1000

listTen= []
listHundred= []
listHunThousand= []
listData= [0, 0, 0, 0, 0, 0]

#Idk whats going on
nums= [1,2,3,4,5,6]
nums2= [1,2,3,4,5,6]
nums3= [1,2,3,4,5,6]
#list and count variales 

######_____Num Gen 10
for i in range(10):
  listTen.append(random.randint(1,6))
  nums[listTen[i]-1]+=1

for i in range(len(nums)):
  print(str(i+1), "| ", "{:.2%}".format(nums[i]/10))
print()


#####______Num Gen 100
for i in range(100):
  listHundred.append(random.randint(1,6))
  nums[listHundred[i]-1]+=1

for i in range(len(nums)):
  print(str(i+1), "| ", "{:.2%}".format(nums[i]/100))
print()


#####___Num Gen 100000

for i in range(100000):
  listHunThousand.append(random.randint(1,6))
  nums[listHunThousand[i]-1]+=1

for i in range(len(nums)):
  print(str(i+1), "| ", "{:.2%}".format(nums[i]/100000))
print()

