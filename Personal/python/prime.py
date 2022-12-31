prime = input("Please enter a number: ")

print(prime)

def is_prime(prime):
    int_prime = int(prime)
    if int_prime < 3:
        return "Not prime"
    for i in range(3,int_prime):
        if int_prime%i==0:
            word = 'It is divisible by: '
            send = f'{word}{i}'
            return ["Not prime", send]
        
    return "Is prime"

print(is_prime(prime))


