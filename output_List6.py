list_a = [1, 2, 3]

output = list_a + list_a
print("원본 리스트", list_a)
print("연산 결과", output)
print()

output = list_a.extend([1, 2, 3])
print("원본 리스트: ", list_a)
print("연산 결과: ", output)