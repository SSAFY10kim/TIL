numbers = [1,3,5,6,7,9,10,11]
found_even = False

for num in numbers:
    print(num)
    if num % 2 == 0:
        print('첫 번째 짝수를 찾았습니다.:',num)
        found_even = True
        break

if not found_even:
    print('짝수를 찾지 못했습니다.')
elif found_even:
    print("짝수를 찾았습니다.")