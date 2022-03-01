class Inventory:



    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items_dict = {}
        self.summed = self.__sum_quantity()
        


    def __sum_quantity(self):
        if self.items_dict:
            return sum(x[1] for x in self.items_dict.values())
        else:
            return 0
    
    @staticmethod
    def sum_quantity(dictionary):
        if dictionary:
            return sum(x[1] for x in dictionary.values())
        else:
            return 0


    def add_item(self, name, price, quantity):
        if name not in self.items_dict:
            dict_copy = self.items_dict.copy()
            dict_copy.update({name: (price, quantity)})
            if self.sum_quantity(dict_copy) <= self.max_capacity:
                self.items_dict = dict_copy
                return True
            else:
                return False 
        else:
            return False 

    def delete_item(self, name):
        if name in self.items_dict:
            self.items_dict.pop(name)
            return True
        else:
            return False 

    def get_items_in_price_range(self, min_price, max_price):
        return list({key:(values[0], values[1]) for key, values in self.items_dict.items() if min_price <= values[0] <= max_price})

    def get_most_stocked_item(self):
        if self.items_dict:
            sort_by_quantity = lambda x: self.items_dict[x][1]
            most_stocked = sorted(self.items_dict, key=sort_by_quantity)[-1]
            return most_stocked
        else:
            return None

        

i1 = Inventory(6)
print(i1.add_item('coca',4,1))
print(i1.add_item('coca',4,2))
print(i1.add_item('guara',3,5))
print(i1.get_most_stocked_item())
print(i1.get_items_in_price_range(2,3))
print(i1.summed)

