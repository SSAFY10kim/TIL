# ws_5_3.py

# 아래 함수를 수정하시오.
def sort_tuple(unsorted_tuple):
    for i in range(unsorted_tuple):
        k = len(unsorted_tuple) - i
        for j in range(1,k):
            if unsorted_tuple[j-1] >= unsorted_tuple[j]:
                temp = unsorted_tuple[j-1]
                unsorted_tuple[j-1] = unsorted_tuple[j]
                unsorted_tuple[j] = temp 
    
    return unsorted_tuple

result = sort_tuple([5, 2, 8, 1, 3])
print(result)
