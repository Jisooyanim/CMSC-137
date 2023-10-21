def simpleParity(a, b):
    numberOfOnes = a.count('1')

    # Sender
    if numberOfOnes % 2 != 0:
        a += '1'
    else:
        a += '0'
    
    # Receiver:
    syndrome = b.count('1')

    if syndrome % 2 == 0:
        dataword = "Accepted"
    else:
        dataword = "Discarded"
    
    print(f"Codeword: {a}")
    print(f"Data word: {dataword}")

def twoDimensional(a):
    row = [a[i:i+9] for i in range(0, 45, 9)]
    column = [''.join(r[i] for r in row) for i in range(8)] 
    errors = 0

    for r in row:
        if r.count("1") % 2 != 0:
            errors += 1
    
    for c in column:
        if c.count("1") % 2 != 0:
            errors += 1
    
    print(f"Error count: {errors}")

def checksum(a):
    datawords = [a[i:i+8] for i in range(0, 32, 8)]
    cs = a[32:]

    one = datawords[0]
    two = datawords[1]
    three = datawords[2]
    four = datawords[3]
    
    res = check(add(check(add(check(add(check(add(one, two)), three)), four)), cs))

    if res == "11111111":
        print("Accept Data")
    else:
        print("Reject Data")

def add(a, b):
    result = []  
    carry = 0  

    for i in range(7, -1, -1):
        bitOne = int(a[i])
        bitTwo = int(b[i])

        add = bitOne + bitTwo + carry
        carry = add // 2
        result.insert(0, str(add % 2))

    if carry:
        result.insert(0, str(carry))

    return ''.join(result)

#Checks if 8 bits only
def check(binary):
    if len(binary) == 8:
        return binary
    else:
        excess = "0000000" + binary[0]
        binary = binary[1:]

        newBinary = add(binary, excess)
        return newBinary

def cyclic(a, b):
    compare = a[0] #dividend
    divLead = b[0] #divisor
    # quotient = ""
    currDiv = a[:4]
    bringDown = a[4:]
    
    while len(bringDown) != 0:
            if compare == "1" and divLead == "1":
                # quotient += "1"
                currDiv = divide(currDiv, b) + bringDown[0]

            elif compare == "0" and divLead == "1":
                # quotient += "0"
                tmp = "0000"
                currDiv = divide(currDiv, tmp) + bringDown[0]
            
            bringDown = bringDown[1:]
            compare = currDiv[0]
    
    if currDiv == "0000":
        # quotient += "0"
        print("Accept data")
    else:
        # quotient += "1"
        print("CRC error detected") 

    # return quotient

def divide(dividend, divisor):
    res = ""

    for bitA, bitB in zip(dividend, divisor):
        res += "1" if bitA != bitB else "0"
    res = res[1:]

    return res

def main():
    choice = int(input())

    if choice == 1:
        a = str(input())
        b = str(input())
        simpleParity(a, b)

    elif choice == 2:
        a = str(input())
        twoDimensional(a)

    elif choice == 3:
        a = str(input())
        checkSpace = a.split()
        
        if len(checkSpace) > 1:
            a = a.replace(" ", "")
        checksum(a)

    elif choice == 4:
        a = str(input())
        b = str(input())
        cyclic(a, b)

    else:
        print("Enk!")

if __name__ == '__main__':
    main()