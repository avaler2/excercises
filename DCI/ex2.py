def fizzbuzz(maximum_value):
    maximum_value +=1
    for n in range(maximum_value):
        if n % 5 == 0 and n % 3 == 0:
            print('FizzBuzz')
        elif n % 3 == 0:
            print('Fizz')
        elif n % 5 == 0:
            print('Buzz')
        else:
            print(n)

fizzbuzz(15)