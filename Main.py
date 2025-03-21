import argparse

def main():
    parser = argparse.ArgumentParser(description="A terminal JPG to ASCII conversion program now with 100% more squirrels.")
    
    # Required argument
    parser.add_argument('name', type=str, help='Your name')
    
    # Optional argument for custom greeting
    parser.add_argument('--greeting', type=str, default='Hello', help='Greeting message')
    
    # Optional flag for a goodbye message
    parser.add_argument('--goodbye', action='store_true', help='Print a goodbye message')
    
    # Parse the arguments
    args = parser.parse_args()

    # Greet the user
    print(f"{args.greeting}, {args.name}!")
    
    # Goodbye message if the flag is set
    if args.goodbye:
        print(f"Goodbye, {args.name}!")

if __name__ == "__main__":
    main()
