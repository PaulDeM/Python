__author__ = 'Pawel Mordasiewicz'


first = raw_input("Wprowadz pierwszy kod pocztowy: ")
end = raw_input("Wprowadz drugi kod pocztowy: ")
# Globalny start i stop

start = int(first[0:2:1])
stop = int(end[0:2:1])

# Czesci kodu pocztowego

first_part_code_start = start
first_part_code_stop = stop
second_part_code_start = int(first[3:7:1])
second_part_code_stop = int(end[3:7:1])

# sprawdzenie czy kody nie sa wpisane odwrotnie

if first_part_code_stop < first_part_code_start:
    print ('Kody sa wpisane odwrotnie')
elif first_part_code_start == first_part_code_stop and second_part_code_stop < second_part_code_start:
    print('Kody sa wpisane odwrotnie')
else:
    # wypisywanie kodow
    while first_part_code_start <= first_part_code_stop:

        if first_part_code_start == start:
            count = second_part_code_start
        else:
            count = 1

        while count <= 999:
            print('{:02}'.format(first_part_code_start) + "-" + '{:03}'.format(count))

            if first_part_code_start == first_part_code_stop and count == second_part_code_stop:
                break
            count += 1
        first_part_code_start += 1



