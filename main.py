num = int(input("자연수를 입력하세요:"))
initial_value = 0

for q in range(1,num+1):
    if num%q == 0:
        initial_value = initial_value +1
        print(q,end=",")
print()
if initial_value == 2:
    print(str(num)+"는 소수")
else:
    print(str(num)+"는 소수가 아님")