def back_order(s):
    size = len(s)
    for i in range(size // 2):
        temp = s[i]
        s[i] = s[size - 1 - i]
        s[size - 1 - i] = temp

def top(a, b):
    return a if a > b else b

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        sys.exit(1)
    
    file_b = open(sys.argv[1], "r")
    if not file_b:
        sys.exit(1)
    
    while True:
        line = file_b.readline()
        if not line:
            break
        decimal, bits = map(int, line.split())
        binary = ""
        n = decimal
        while n > 0:
            binary += str(n % 2)
            n //= 2
        if decimal == 0:
            binary = '0'
        binary = list(binary)
        back_order(binary)
        rep = "000000000000000000000000"
        print(rep[:top(0, bits - len(binary))] + "".join(binary[top(0, len(binary) - bits):]))
    
    file_b.close()
