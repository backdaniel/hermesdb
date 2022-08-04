import random, string, hashlib

term = 'example'
definition = 'a thing characteristic of its kind or illustrating a general rule'
difficulty = 16

term = term.ljust(16, ' ')[:16]
definition = definition.ljust(128, ' ')[:128]

while True:
	nonce = ''.join(random.choices(string.printable[:95], k=32))
	entry = term + ' ' + definition + ' ' + nonce
	result = hashlib.sha3_256(entry.encode()).hexdigest()
	binary = str(bin(int(result, 16)))[2:].rjust(256, '0')
	print(binary[:difficulty])
	if not '1' in binary[:difficulty]:
		print(entry)
		break
