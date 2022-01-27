try:
    user_input_a = int(input("정수 입력> "))

except:
    print("정수를 입력해달라고 했잖아용")

else:
    print("원의 반지름: ", user_input_a)
    print("원의 둘레: ", 2 * 3.14 * user_input_a)
    print("원의 넓이: ", 3.14 * user_input_a * user_input_a)