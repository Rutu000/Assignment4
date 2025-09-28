try:

    with open("sample.txt", "r") as file:
        print("Reading file content:\n")
        line_no = 1
        for line in file:
            print(f"Line {line_no}: {line.strip()}")
            line_no += 1

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")