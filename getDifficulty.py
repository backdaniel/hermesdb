import hashlib, sys

result = hashlib.sha3_512(sys.argv[1].encode()).hexdigest()
binary = str(bin(int(result, 16)))[2:].rjust(512, '0')
print(binary)
difficulty = len(binary.split('1', 1)[0])
print(difficulty)
