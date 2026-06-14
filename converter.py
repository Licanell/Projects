def from_binary_to_ten(s):
    return int(s, 2)

def from_ten_to_binary(s):
    return str(bin(int(s)))[2:]

def converter(s):
    k = len(s) - 1
    result = 0
    for i in s:
        result += int(i) * 16 ** k
        k -= 1
    return result

def converter_from_ten(s, n=2):
    result = ""
    while s > 0:
        if s % n >= 10:
            result += chr(ord("A") + (s % n) - 10)
        else:
            result += str(s % n)
        s = s // n
    return result[::-1]

s = input()

print(from_ten_to_binary(s))
print(converter_from_ten(int(s), n = 8))
print(converter_from_ten(int(s), n = 16))

#bin() 2
#oct() 8
#hex() 16