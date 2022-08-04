import hashlib

entry = 'example          a thing characteristic of its kind or illustrating a general rule                                            c4CFw7 ]"g#$a)k.G\fB`:6KNi:aO\'O!'

result = hashlib.sha3_512(entry.encode()).hexdigest()
binary = str(bin(int(result, 16)))[2:].rjust(512, '0')
difficulty = len(binary.split('1', 1)[0])
print(difficulty)
