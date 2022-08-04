import hashlib

entry = 'example          a thing characteristic of its kind or illustrating a general rule                                                                KUSI3vXOGI(2sd R.Q!=IVPB0|cb (.L'
result = hashlib.sha3_256(entry.encode()).hexdigest()
binary = str(bin(int(result, 16)))[2:].rjust(256, '0')
difficulty = len(binary.split('1', 1)[0])
print(difficulty)
