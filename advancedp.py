class Range:
    def __init__(self, start, stop, step):
        self.start= start
        self.stop= stop
        self.step = step 
        self.counter = 0
        self.range_list = list(range(self.start, self.stop, self.step))

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter == len(self.range_list):
            raise StopIteration
        self.counter += 1
        return self.range_list[self.counter - 1]
        

r1 = Range(5,10,1)
for x in r1:
    print(x)