# its is the hash set method  n
num=[1,7,11,15]
traget=22
hash_set={}

for index,value in enumerate(num):
    # print(index,value)
    diff=traget-value
    # print(diff)
    if(diff in hash_set):
        print(hash_set[diff],index)

    hash_set [value]=index