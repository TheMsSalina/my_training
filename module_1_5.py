immutable_var = 1,3,5,7, True, 'sun'
print(immutable_var)
#immutable_var[0] = 0 - изменить элемент кортежа нельзя, т.к. кортеж - неизменяемая последовательность элементов
mutable_list = [2,4,6,8]
mutable_list [0] = 99 #списки же можно менять, как угодно, даже если они являются элементами кортежа
print(mutable_list)
