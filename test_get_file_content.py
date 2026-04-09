from functions.get_file_content import get_file_content

def main():
    working_dir = "calculator"
    root_contents = get_file_content(working_dir, "lorem.txt")
    print(root_contents)
    pkg_contents = get_file_content(working_dir, "main.py")
    print(pkg_contents)
    pkg_contents = get_file_content(working_dir, "pkg/calculator.py")
    print(pkg_contents)
    pkg_contents = get_file_content(working_dir, "/bin/cat")
    print(pkg_contents)
    pkg_contents = get_file_content(working_dir, "pkg/does_not_exist.py")
    print(pkg_contents)


if __name__ == '__main__':
    main()