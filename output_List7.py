list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

# 제거방법[1] - del
del list_a[1]
print("del list[1]: ", list_a)
print()

# 제거방법[2] = pop()
list_a.pop(2)
print("pop(2): ", list_a)
print()