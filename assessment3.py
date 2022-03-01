def generate_string(string, frequency):
    counter = 0 
    while counter < len(string):
        yield string[counter]*frequency
        counter += 1
    
    
    


class GenerateString:
    def __init__(self, string, frequency):
        self.string = string 
        self.frequency = frequency 
        
    def __iter__(self):
        self.counter = 0
        return self


    def __next__(self):
        if self.counter < len(self.string):
            self.counter += 1
            return self.string[self.counter - 1]*self.frequency 
            
        else:
            raise StopIteration






gs = GenerateString('ola',5)
for x in gs:
    print(x)
