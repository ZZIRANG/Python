number = 20
welcome = '환영합니다'
base = '{} 번 손님'

#아래 3개의 print는 같은 값을 출력
print(number,'번 손님',welcome)
print(base.format(number,welcome))
print('{} 번 손님 {}'.format(number,welcome))
#=>20 번 손님 환영합니다
print(base.format(number))