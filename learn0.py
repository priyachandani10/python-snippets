# data = 10
# print(data)

"""
Understanding filter() in python
"""
def func(variable):
    print("variable", variable)
    vowels = ['a','e','i','o','u']
    if variable in vowels:
        print("True condition", variable)
        return True
    else:
        print("False Condition", variable)
        return False
    
sequences = ['r', 'i', 'j', 'o']
filtered_data = filter(func, sequences)
print(type(filtered_data)) #returns class 'filter'
for i in filtered_data:
    print("element from filtered data", i)