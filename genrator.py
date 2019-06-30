#iterator

def seq_num(nums):
    result=[]
    for i in nums:
        result.append(i*i)
    return result


seq=[1,2,3,4,5]
sqd_values=seq_num(seq)
print(sqd_values)


#generator

def seq_num(nums):
    for i in nums:
        yield(i*i)

seq=[1,2,3,4,5]
sqd_values=seq_num(seq)
print(type(sqd_values))
for i in range(0, len(seq)):
    print(next(sqd_values),end=',')
