def flatten_lists(func):
    def wrapper(*args):
        regular_arguments = list(filter(lambda x: type(x) != list, args))
        unwanted_list = list(filter(lambda x: type(x) == list, args))
        if unwanted_list:
            individual_list = [x for y in unwanted_list for x in y]
            official_list =  regular_arguments + individual_list
        else:
            official_list =  regular_arguments
        print(official_list)    #aqui 
        return func(*official_list)
    return wrapper
     

def convert_strings_to_ints(func):
    def wrapper(*args):
        integers = [x for x in args if (type(x) == int) or (type(x) == bool)]
        non_integer = [x for x in args if type(x) == str]
        now_integers = [int(x) for x in non_integer if x.isdigit()]
        final_argument = integers + now_integers
        print(final_argument)    #aqui 
        return func(*final_argument)
    return wrapper

def filter_integers(func):
    def wrapper(*args):
        lista = [x for x in args if (type(x) == int) or (type(x) == bool)]
        print(lista)    #aqui 
        return func(*lista)
    return wrapper 

@flatten_lists
@convert_strings_to_ints
@filter_integers
def integer_sum(*args):
    return sum(args)

lista_com_lista = [1,2,3,4, [1,2,3], [1, 2], '1','2']
print(integer_sum(*lista_com_lista))



args = [True, "1", "2", -0.9, 4, [5, "hi", "3"]]
print(integer_sum(*args))