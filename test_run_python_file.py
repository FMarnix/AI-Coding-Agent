from functions.run_python import run_python_file


def main():
    working_dir = "calculator"
    root_contents = run_python_file(working_dir, "main.py")
    print(root_contents)
    pkg_contents = run_python_file(working_dir, "main.py", ["3 + 5"])
    print(pkg_contents)
    pkg_contents = run_python_file(working_dir, "tests.py")
    print(pkg_contents)
    pkg_contents = run_python_file(working_dir, "../main.py")
    print(pkg_contents)
    pkg_contents = run_python_file(working_dir, "pkg/nonexistent.py")
    print(pkg_contents)
    pkg_contents = run_python_file(working_dir, "lorem.txt")
    print(pkg_contents)


if __name__ == '__main__':
    main()