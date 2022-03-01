def positive_even_squares(*args):
    unique_list_individually = [filter(lambda x: (x >0) and (x%2 == 0) , y) for y in args]
    result = [x for y in unique_list_individually for x in y]
    return list(map(lambda x: x**2, result))


x = positive_even_squares([-3,4,5], [-1,2,4])
print(x)