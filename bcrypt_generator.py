import bcrypt
import sys
import argparse

def generate_hash(password, strength):
    if not (4 <= strength <= 31):
        raise ValueError("Strength (rounds) must be between 4 and 31.")
    salt = bcrypt.gensalt(rounds=strength)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_hash(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))

def main():
    parser = argparse.ArgumentParser(description="Bcrypt Hash Generator and Verifier")
    parser.add_argument("-p", "--password", required=True, help="Password to hash or verify")
    parser.add_argument("-s", "--strength", type=int, default=12, help="Hashing strength (default: 12)")
    parser.add_argument("-v", "--verify", help="Hash to verify against the password")

    args = parser.parse_args()

    if args.verify:
        if verify_hash(args.password, args.verify):
            print("TRUE")
        else:
            print("FALSE")
    else:
        try:
            hashed_password = generate_hash(args.password, args.strength)
            print(f"{hashed_password}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
