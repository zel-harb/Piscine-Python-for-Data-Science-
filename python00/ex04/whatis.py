import sys

def what_is_it(num: int):
    if num % 2 == 0:
        return "I'm Even"
    else:
        return "I'm Odd"

def main(argv):
    try:
        if len(argv) < 2:
            exit(1)
        if len(argv) != 2:
            print("AssertionError: more than one argument is provided")
            exit(1)
        if len(argv) > 1:
            if not argv[1].isdigit() and not (argv[1][0] == '-' and argv[1][1:].isdigit()):
                print("AssertionError: argument is not an integer")
                exit(1)
            else:
                num = int(argv[1])
                # print(f"number is {num}")
                print(what_is_it(num))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)

if __name__ == "__main__":
    main(sys.argv)


