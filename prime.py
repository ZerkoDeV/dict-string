def is_prime(num):
    if num == 2:
            return True
    for i in range(2,num):
        if(num % i == 0):
            return False
    return True

def get_prime(num):
    counter = 0
    number = 2
    while(counter < num):
        if(is_prime(number)):
            counter+=1
        number+=1
    return number-1

for i in range(1,100):
    print(get_prime(i))