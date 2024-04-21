
def Solution(int):
    my_str = str(int)
    arr_char = []
    for ch in my_str:
        arr_char.append(ch)
    print (arr_char)
    print(arr_char[::-1])
    if arr_char == arr_char[::-1]:
        return True
    else:
        return False
print(Solution(131))
