binary = input('Enter a Binary number: ')
decimal = 0

#length of binary input
l = len(binary)

#loop through each digit of binary
for x in binary:
    l = l-1                        #decrease l by 1
    decimal += pow(2,l) * int(x)   #multiply

print("Decimal of {p} is {q} ".format(p=binary, q=decimal))
