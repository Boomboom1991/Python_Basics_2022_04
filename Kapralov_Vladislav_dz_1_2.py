
cub_lst = [x ** 3 for x in range(1,1001) if x % 2 != 0]


def get_num(i):
    temp_lst = []
    result =  0
    while i > 0:
        temp_lst.append(i % 10)
        i //= 10
    for i in temp_lst:
        result += i
    #result = int(''.join(map(str,temp_lst)))
    return result

def devine_by_seven(cub_lst):
    result_sum = 0
    for i in cub_lst:
        a = get_num(i)
        if a % 7 != 0:
            result_sum += a
    return result_sum

print(cub_lst)
print(type(cub_lst[0]))
print(devine_by_seven(cub_lst)) # result = 14654
cub_lst = [x + 17 for x in range(1,1001)]
print(cub_lst)
print(devine_by_seven(cub_lst)) #result = 11628