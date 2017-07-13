# main_list = [i+0.5 for i in range(5)]
# print main_list


# gen_list = [x+0.5 for x in [1.5 , 2,2.5, 3,3.5, 4,4.5, 5]]

# gen_list = [x+0.5 for x in range(2,5)]

'''def count(start, step):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step


print count(2, 0.5)'''

n = 2.0
while n <= 5.5:
    print n
    n += 0.5