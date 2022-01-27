try:
    user_input_a = int(input("정수 입력> "))
    print("원의 반지름: ", user_input_a)
    print("원의 둘레: ", 2 * 3.14 * user_input_a)
    print("원의 넓이: ", 3.14 * user_input_a * user_input_a)

except Exception as exception:
    print("type(exceprion): ", type(exception))
    print("exception: ", exception)