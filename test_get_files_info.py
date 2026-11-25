from functions.get_files_info import get_files_info

def main():
    cases = [
        (".", "Result for current directory:"),
        ("pkg", "Result for 'pkg' directory:"),
        ("/bin", "Result for '/bin' directory:"),
        ("../", "Result for '../' directory:"),
    ]

    for directory, header in cases:
        result = get_files_info("calculator", directory)
        print(header)
        if result.startswith("Error:"):
            print(f"    {result}")
        else:
            for line in result.splitlines():
                print(f"  {line}")

if __name__ == "__main__":
    main()
