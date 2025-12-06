def odd_nums(x):
    for i in range(x):
        if i % 2 != 0:
            yield i

gen = odd_nums(10)

for i in gen:
    print("returned :", i)

def show_list_elements(list,d1,d2):
    for i in list:
        if i > d1 and i < d2:
            continue
        else:
            yield list[i]

list = [0,1,2,3,4,5,6,7,8,9]

list_gen = show_list_elements(list,4,8)

for i in list_gen:
    print("List element : ", i)