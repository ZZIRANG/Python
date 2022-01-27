# 리스트를 선언
array = [1, 2, 3]

# 리스트 뒤에 요소 추가하기
print("*리스트 뒤에 요소 추가하기*")
array.append(4)
array.append(5)
print(array)
print()

# 리스트 중간에 요소 추가하기
print("*리스트 중간에 요소 추가하기*")
array.insert(0,10)
print(array)
print()

# 리스트를 선언
list_a = [1,2,3]
list_a.extend([4, 5, 6])
print("[1, 2, 3].extend([4, 5, 6])", list_a)