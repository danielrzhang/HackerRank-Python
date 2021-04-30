def print_formatted(number):
    length = len(bin(number)) - 2
    for i in range(1, n + 1):
        print(str(i).rjust(length) + " " + oct(i)[2:].rjust(length) + " " + hex(i)[2:].upper().rjust(length) + " " + bin(i)[2:].rjust(length))
    
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)