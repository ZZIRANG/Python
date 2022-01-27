# 딕셔너리를 선언합니다.
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

# 출력합니다.
if "존재하지 않는 키" in dictionary:
    print(dictionary["존재하지 않는 키"])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")