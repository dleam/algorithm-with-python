import numpy as np
import random

num = int(input('please input the num of number in the list: '))
randomList = []
value_index = {}
bucket = [[] for i in range(num-1)]

for i in range(num):#(0,10)
    randomList.append(random.randint(0,100)/10)
#randomList = np.random.uniform(0,10,size=10)
print (randomList)

maxx,minn = float("-inf"), float("inf")

for value in randomList:
    if value >maxx: maxx =value
    if value <minn: minn =value
print ('max = %s, min = %s'%(maxx,minn) )
randomList.remove(maxx)
randomList.remove(minn)
print('after remove: %s' %randomList)

def get_max(listt):
    maxx = float("-inf")
    for value in listt:
        if value >maxx: maxx =value

    return maxx

def get_min(listt):
    minn = float("inf")
    for value in listt:
        if value <minn: minn =value

    return minn

bucket[0].append(minn)
bucket[num-2].append(maxx)

max_min_range = maxx - minn
bucket_size =max_min_range/(num-1)
print ('bucket size is %.1f' %bucket_size )

for value in randomList:

    bucket_index = int((value-minn)/bucket_size)
    bucket[bucket_index].append(value)

print (bucket)


nul_index = []
count = 0
for bt in bucket:
    if bt == []:

        nul_index.append(count)
    count+=1

print (nul_index)

if nul_index !=[]:
    temp =0
    for i in nul_index:
        while(bucket[i]==[]):
            i-=1
        left_max=get_max(bucket[i])
        i+=1
        while(bucket[i]==[]):
            i+=1
        right_min=get_min(bucket[i])
        if right_min-left_max > temp:
            temp = right_min-left_max
    print ('max gap of the list is : %.1f' %temp)#保留1位浮点小数

else:
    temp = 0
    if get_min(bucket[1])-get_max(bucket[0]) > get_min(bucket[num-2])-get_max(bucket[num-3]):
        temp = get_min(bucket[1])-get_max(bucket[0])
    else:
        temp = get_min(bucket[num-2])-get_max(bucket[num-3])
    print ('max gap of the list is : %.1f' %temp)#保留1位浮点小数
