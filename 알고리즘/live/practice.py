def change(my_str):
    result = ''
    for char in my_str:
        result = char + result
    return result

out = change("hello")
print(out)