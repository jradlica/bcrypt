### Overview

A lightweight Docker container for generating and verifying bcrypt hashes.

Repository: https://github.com/jradlica/bcrypt

Registry: https://hub.docker.com/repository/docker/jradlica/bcrypt

### Options

```
-p, --password: Plain-text password to hash or verify.
-s, --strength: Specify hashing strength (number of rounds). Default is 12.
-v, --verify: Bcrypt hash to verify against the password.
```

### Usage
Generate a bcrypt hash with default strength:
```bash
docker run --rm jradlica/bcrypt:latest -p 'mySecurePassword'
```

Generate a bcrypt hash with custom strength:
```bash
docker run --rm jradlica/bcrypt:latest -p 'mySecurePassword' -s 10
```

Verify a password against a bcrypt hash:
```bash
docker run --rm jradlica/bcrypt:latest -p 'mySecurePassword' -v '$2b$12$9c4.k9GvuiM8y6RVl6Z6OevSO/9osbZwhVWxdFE1NduYV2q6Vsq8y'
```
