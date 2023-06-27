my_list = [6, 4, 2, 7, 1, 8]

def get_time(ls):
    time = 0
    for item in ls:
        for elem in ls:
            time += 1
    print(time)

get_time(my_list)