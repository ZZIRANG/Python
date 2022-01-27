list_number = [52, 273, 32, 72, 100]

try:
    number_input_a = int(input("정수 입력> "))
    print("{}번째 요소: {}".format(number_input_a, list_number[number_input_a]))

except ValueError:
    print("정수를 입력해주세요!")

except IndexError:
    print("리스트의 인데스를 벗어났어요!")