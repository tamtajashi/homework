def get_min_value(dictionary):
    if not dictionary:
        return None  # Return None for an empty dictionary
    
    min_value = min(dictionary.values())
    
    return min_value

# My dictionary:
my_dict = {'tamta': 500, 'jashi': -4, 'pen': 20, 'g': 0}
result = get_min_value(my_dict)
print(f"The minimum value in the dictionary is: {result}")
