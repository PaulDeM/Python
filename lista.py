__author__ = 'Pawe? Mordasiewicz'



dana_lista1 = [2, 3, 4, 7, 10]
n=10

'''def compere (dana_lista):
    main_list = [1, 2, 3, 4]
    miss_list=[]
    for element in range(len(dana_lista)):
        for element_1 in range(len(main_list)):
            if main_list[element] == dana_lista[element_1]:
                miss_list.append(main_list[element])
    return miss_list


print compere(dana_lista1)'''

'''def compare_lists (dana_lista):
    main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    miss_list=[]
    for x in main_list:
        if (x in dana_lista)== False:
            miss_list.append(x)
    return miss_list

print compare_lists(dana_lista1)'''



def compare_lists (dana_lista, size):
    main_list = [i+1 for i in range(size)]
    miss_list = []
    for x in main_list:
        if (x in dana_lista)== False:
            miss_list.append(x)
    return miss_list

print compare_lists(dana_lista1,n)