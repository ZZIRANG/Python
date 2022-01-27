list_b = [0, 1, 2, 3, 4, 5, 6]
del list_b[3:6]

print("# 인덱스로 리스트의 요소 여러 개 제거하기")
print("del list_b[3:6]: ", list_b)
print()

list_c = [0, 1, 2, 3, 4, 5, 6]
list_d = [0, 1, 2, 3, 4, 5, 6]
del list_c[:3]
del list_d[3:]

print("# 인덱스로 리스트의 요소 한쪽 전부 제거하기")
print("del list_c[:3]: ", list_c)
print("del list_d[3:]: ", list_d)