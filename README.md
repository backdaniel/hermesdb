# meaning-database
Distributed dictionary protocol using proof of work for prioritization.

## Format
One entry per line (3 parts separated by ascii space)

`term definition nonce`
- term: 16 chars (ascii 32-126)
- definition: 256 chars (ascii 32-126)
- nonce: 16 chars (ascii 32-126)

## Rules
- Max 16 entries per term
- Verification is done by hashing `term definition nonce`
- Importance is determined by difficulty (start of hash with most zero bits)
- Min 16 zero bits at start of hash
- Hashing algorithm: SHA-3 256

## Contributing
I will update this instance according to my knowledge.

A good way of adding valid entries is creating a pull request.

## Copying
This is information, not property.
