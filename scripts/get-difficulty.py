import hashlib

entry = 'example          a thing characteristic of its kind or illustrating a general rule                                            6%{0AFH@g7e1RA~WeU!xJ-wNwZ)"9r*5'

result = hashlib.sha3_512(entry.encode()).hexdigest()
binary = str(bin(int(result, 16)))[2:].rjust(512, '0')
difficulty = len(binary.split('1', 1)[0])
print(difficulty)
