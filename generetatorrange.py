def new_range(start, stop, step):
    counter = start 
    while counter < stop:
        yield counter
        counter += step


x = new_range(2, 5, 1)

print(list(x))