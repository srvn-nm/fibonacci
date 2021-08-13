# author : Sarvin Nami
number = int(input('please enter the end of your range here : '))
x = 2
print('the 0th number is 0')
print('the 1th number is 1')
list1 = [0,1]
while x <= number :
    list1.append(list1[x - 1] + list1[x - 2])
    print(f'the {x}th number is ' + str(list1[x]))
    x+=1