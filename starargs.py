#accept any num of args

def sum(*args):
    total=0
    for num in args:
        total+=num
    return total


value_result=sum(1,34,34)  
print(value_result)  
