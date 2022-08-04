# meaning-database
Distributed dictionary protocol using proof of work for prioritization.

## Format
One entry per line (separated by ascii space)

`term description nonce hash`
- term: 16 chars (ascii 32-126)
- description: 64 chars (ascii 32-126)
- nonce: 16 chars (ascii 32-126)
- hash: SHA-3 of the concatenation of the other 3 parts (hexadecimal)

## Rules
- Order of importance is defined by difficulty (starting of hash with most zero bits)
- Max 16 entries per term
- Needs at least 8 zero bits at start of hash

## Contributing
I will update this instance according to my knowledge.

A good way of informing me of new valid entries is creating a pull request.

## Copying
This is information, not property.
