

class DataBollocks:
    def __init__(self, atty_one, atty_two):
        self.atty_one = atty_one
        self.atty_two = atty_two

    def __str__(self):
        return self.atty_one + str(self.atty_two)

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.atty_one == other.atty_one and self.atty_two == other.atty_two



def get_ones_to_create(exists, new):
    return list(set(new).difference(exists))

def get_ones_to_delete(exists, new):
    return list(set(exists) - set(new))


exists = [1, 3, 4, 77, 34, 466]
news = [1, 4, 7, 77, 35, 999, 34, 346]

to_delete = get_ones_to_delete(exists, news)
print(f"deleting {to_delete}")
# [3, 466]

to_create = get_ones_to_create(exists, news)
print(f"creating {to_create}")
# [7, 35, 999, 346]


at = DataBollocks("to_delete", 1)
at_2 = DataBollocks("not_appear", 0)
at_3 = DataBollocks("not_appear", 0)
at_4 = DataBollocks("to_create", 1)
at_5 = DataBollocks("to_also_create", 2)
at_6 = DataBollocks("to_create", 3)

exists = [at, at_2, at_3]
news = [at_3, at_4, at_5, at_6]

to_delete = get_ones_to_delete(exists, news)
print(f"deleting...")
for item in to_delete:
    print(f"{item.atty_one}, {item.atty_two}")
# deletes at and at_3

to_create = get_ones_to_create(exists, news)
print(f"creating...")
for item in to_create:
    print(f"{item.atty_one}, {item.atty_two}")
# creates all but at_2



"""

1. Have both the existing and new data converted to a data_class

2. Set the comparison of the class using the __eq__ and __hash__ bollocks

3. Use the set Subtraction to identify the ones to create and delete

4. Do the bulk create and delete, the editing actually happens as a delete and then create cause it is technically a different type of holiday

"""
