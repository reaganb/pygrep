import os.path as op
import configparser
import argparse
import glob
import re


class Grep:
    """
    The Grep class consist of a function for the listing of file(s)
    in a certain path, recursively or not. In these file(s),
    a searching of a regex pattern will occur and try to
    find and print those lines matching the pattern.
    """

    def __init__(self, regex, file_pattern, path, recursive=False,
                 ignore_case=False, invert=False, count=False,
                 number=False, ):
        """The init function consists of the main properties such are the regex
        pattern, file pattern, and the source directory path. It has the flags
        for the function to work.

        Positional arguments:
        regex -- the regex pattern
        file_pattern -- the glob file pattern
        path -- the directory path to look for
        Keyword arguments:
        recursive -- enable recursive search
        ignore_case -- ignore case while searching for pattern
        invert -- print non-matching lines
        count -- print the match count of lines for each file.
        number -- print the line together with its line number
        """

        self.regex = regex
        self.file_pattern = file_pattern
        self.path = op.abspath(path)

        self.invert_match = invert
        self.line_count = count
        self.line_number = number
        self.re_flags = 0

        # Check if the path exist
        if not op.exists(self.path):
            print('Error: Path does not exist!')
            exit()
        # Check if only a path, not a file is given as the argument
        elif not op.isdir(self.path):
            print('Error: Path are only allowed as the argument')
            exit()

        if ignore_case:
            self.re_flags = re.IGNORECASE

        if recursive:
            glob_pattern = f'{self.path}/**/{self.file_pattern}'
        else:
            glob_pattern = f'{self.path}/{self.file_pattern}'

        self.list_files = glob.iglob(glob_pattern, recursive=recursive)

    def print_output(self):
        """Print the output depending on the flags of the script execution"""

        # Iterate through the files
        for file_name in self.list_files:
            with open(file_name) as file:
                match_line = ''  # the string for output and will be printed later on.
                count = 0  # number of lines with match

                # Iterate through each line of the file
                for n, line in enumerate(file):
                    # Check if the invert match flag is on.
                    # If on, it will check the line if it does not have the pattern.
                    if self.invert_match:
                        condition = not re.search(fr'{self.regex}', line, flags=self.re_flags)
                    else:
                        condition = re.search(fr'{self.regex}', line, flags=self.re_flags)

                    # Code for adding lines to the output string
                    if condition:
                        # Check if the line number flag is on
                        if self.line_number:
                            match_line += f'{n + 1} {line}'
                            count += 1
                        else:
                            match_line += f'{line}'
                            count += 1

                # Check if the print line count flag is on
                if self.line_count:
                    print(file_name, ':', count)
                # Check if the file has a match of the regex pattern
                elif match_line != '':
                    print(file_name)
                    print(match_line)


if __name__ == "__main__":
    # The starting point of the script.
    # The code for the command line arguments and
    # grep object initialization.
    parser = argparse.ArgumentParser()
    config = configparser.ConfigParser()
    config.read(op.join(op.dirname(op.abspath(__file__)), 'config.ini'))

    parser.add_argument('regex',
                        help="the regular expression argument")
    parser.add_argument('pattern',
                        help="the file pattern argument")
    parser.add_argument('path',
                        help="the directory path to look for")
    parser.add_argument('-n', '--line_number', dest='line_number', action='store_true',
                        help='also print the line number')
    parser.add_argument('-r', '--recursive', dest='recursive', action='store_true',
                        help='enable recursive search')
    parser.add_argument('-i', '--ignore_case', dest='ignore_case', action='store_true',
                        help='enable ignore case search')
    parser.add_argument('-v', '--invert_match', dest='invert', action='store_true',
                        help='enable invert case search')
    parser.add_argument('-c', '--count', dest='count', action='store_true',
                        help='print the count of selected lines per file')

    args = parser.parse_args()

    # Initialize the grep object together with its arguments
    grep = Grep(args.regex, args.pattern, args.path,
                recursive=args.recursive,
                ignore_case=args.ignore_case,
                invert=args.invert,
                count=args.count,
                number=args.line_number,
                )

    # Running the method of the object
    grep.print_output()
