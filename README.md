# term-database
Distributed dictionary protocol using proof of work for prioritization.

## Format
One entry per line (4 parts separated by ascii space)

`term definition nonce hash`
- term: 16 chars (ascii 32-126)
- definition: 64 chars (ascii 32-126)
- nonce: 16 chars (ascii 32-126)
- hash: SHA-3 of `term definition nonce` (hexadecimal)

## Rules
- Importance is determined by difficulty (starting of hash with most zero bits)
- Max 16 entries per term
- Min 8 zero bits at start of hash

## Contributing
I will update this instance according to my knowledge.

A good way of adding valid entries is creating a pull request.

## Copying
This is information, not property.
