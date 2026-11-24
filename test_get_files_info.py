from functions.get_files_info import get_files_info

def main():
    cases =[
        ("calculator", "."),
        ("calculator", "/bin"),
        ("calculator", "../"),
        ("calculator", "main.py"),
    ]

    for working_dir, directory in cases:
        result = get_files_info(working_dir, directory)
        print(f'get_files_info("{working_dir}", "{directory}") -> {result}')

if __name__ == "__main__":
    main()
