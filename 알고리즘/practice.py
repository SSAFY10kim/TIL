# hw_6_4.py

# 아래 함수를 수정하시오.
def add_item_to_dict(dict, key, value):
    new_dict = dict.copy()
    new_dict[key] = value
    return new_dict

my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
