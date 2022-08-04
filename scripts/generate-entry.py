import random, string, hashlib

term = 'example'
definition = 'a thing characteristic of its kind or illustrating a general rule'
difficulty = 18

term = term.ljust(16, ' ')[:16]
definition = definition.ljust(108, ' ')[:108]

while True:
	nonce = ''.join(random.choices(string.printable[:95], k=32))
	entry = term + ' ' + definition + ' ' + nonce
	result = hashlib.sha3_512(entry.encode()).hexdigest()
	binary = str(bin(int(result, 16)))[2:].rjust(512, '0')
	print(binary[:difficulty])
	if not '1' in binary[:difficulty]:
		print(entry)
		break
