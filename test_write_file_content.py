from functions.write_file_content import write_file


def main():
    working_dir = "calculator"
    root_contents = write_file(working_dir, "lorem.txt", "wait, this isn't lorem ipsum")
    print(root_contents)
    pkg_contents = write_file(working_dir, "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(pkg_contents)
    pkg_contents = write_file(working_dir, "/tmp/temp.txt", "this should not be allowed")
    print(pkg_contents)


if __name__ == '__main__':
    main()