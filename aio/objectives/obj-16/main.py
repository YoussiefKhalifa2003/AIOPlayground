#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(description="Hello helper script")
    parser.add_argument("name", nargs="?", default="world", help="Name to greet")
    args = parser.parse_args()
    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
