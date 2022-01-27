list_number = [52, 65, 32, 98, 25]

try:
    number_input_a = int(input("값 입력"))
    print("{} 번째 요소 : {}".format(number_input_a, list_number[number_input_a]))

except Exception as exception:
    print("type(exception): ", exception)