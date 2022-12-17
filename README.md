# hermesdb

The "most sucessful" memes will exert their influence in the real world, compete with each other and use any means necessary to be included in this database. Follow the rules below when maintaining your instance, update it according to the information available.

## Idea

Respects the memetic nature of language, incentivizes bottom-up emergence and competition.

Proof of work solves priority allocation, thus enforcing consensus by rules.

Distributed instances provide censorship resistence, syncronization is not critical, every instance ends up converging on the same data.

Easy to understand, simple to maintain, open standard, human friendly.

## Rules
- One entry per line (no identical entries), composed of exactly 80 chars from `ascii 32-126` (inclusive)
- The database has `max 10_000` entries separated by `newline` (attempts to increase capacity are by default backwards compatible)
- Order follows difficulty (number of consecutive `0` bits at start when hashing the entry) (descending), then `ascii` (ascending)
- Hashing algorithm is `SHA-3 512` (fork rules and change algorithm if necessary)

## Contributing
When creating an entry, use the last characters as `nonce` to find a good hash (convention).

I will update this instance according to the data available, let me know.

## Copying
This is information, not property.
