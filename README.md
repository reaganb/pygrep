# Machine Problem: grep

#### Requirements: 

You are going to implement the grep command. The purpose of grep is to search for text patterns in ﬁles using regular expressions.

The syntax is: python grep.py <regular expression> <file pattern> <path to search in>

For example, if I want to search for the word “help” in the files of the books directory, I'll do this:
```
    python grep.py help *.rst c:\books
```
The program should output the line which contains the string in stdout.

Bonus points if you can implement a command line argument for doing a recursive search in the path to search in.

Commit your code to a repository named "pygrep" and submit the link here for checking.

## The grep.py python script

The python script has the functionality to recursively read the files of a directory path using globbing file pattern search. These files files will then be used in a regex pattern search line by line.

### Prerequisites
1. Windows/Linux OS
2. Python 3

### Usage
The script will work as long as there is Python 3 installed on the system.
Check if it is installed by executing the following command on the terminal.
```
$ python --version
```

### Flags

**-n** - Print the the matching lines together with its line number

**-r** - Recursively read the file(s) from the given directory path.

**-i** - Ignore case sensitivity for the regex pattern search.

**-v** - Print the lines that does NOT have a match from the regex pattern.

**-c** - Only print the line count for each file.

#### Examples:
```
$ python grep.py is *.txt .
C:\Users\TEU_USER\TrendProjects\pygrep\Zen.txt
Beautiful is better than ugly.
```
The basic usage of the script by providing the needed arguments. The regex pattern search for the word "is", using "*.txt" for the glob pattern, and the current directory dot (.) for the directory path.

```
$ python grep.py is *.txt . -r 
C:\Users\TEU_USER\TrendProjects\pygrep\Zen.txt
Beautiful is better than ugly.

C:\Users\TEU_USER\TrendProjects\pygrep\lvl1\1.txt
Beautiful is better than ugly.
```
Providing the recursive flag ***-r***

```
$ python grep.py is *.txt . -r -n
C:\Users\TEU_USER\TrendProjects\pygrep\Zen.txt
1 Beautiful is better than ugly.
2 Explicit is better than implicit.

C:\Users\TEU_USER\TrendProjects\pygrep\lvl1\1.txt
1 Beautiful is better than ugly.
2 Explicit is better than implicit.
``` 
Adding the line number flag ***-n***

```
$ python grep.py IS *.txt . -r -n -i
C:\Users\TEU_USER\TrendProjects\pygrep\Zen.txt
1 Beautiful is better than ugly.
2 Explicit is better than implicit.

C:\Users\TEU_USER\TrendProjects\pygrep\lvl1\1.txt
1 Beautiful is better than ugly.
2 Explicit is better than implicit.
```
Adding the ignore case flag ***-i***. Notice that the regex pattern is changed from ***is*** to ***IS***. Without the flag, it will not find any match.

```
$ python grep.py IS *.txt . -r -n -i -v
C:\Users\TEU_USER\TrendProjects\pygrep\Zen.txt
7 Readability counts.
8 Special cases aren't special enough to break the rules.

C:\Users\TEU_USER\TrendProjects\pygrep\lvl1\1.txt
7 Readability counts.
8 Special cases aren't special enough to break the rules.
```
Adding the invert match flag ***-v***. Notice that the output line for each file does not have any match from the regex pattern.

```
$ python grep.py IS *.txt . -rnivc
(base) C:\Users\TEU_USER\TrendProjects\pygrep>python grep.py IS *.txt . -rnivc
C:\Users\TEU_USER\TrendProjects\pygrep\Zen.txt : 9
C:\Users\TEU_USER\TrendProjects\pygrep\lvl1\1.txt : 9
```
Adding the line count flag ***-c***. It only outputs the unmatched line from the regex pattern. Removing the ***-v*** option will return the other way around.


Note: The outputs from this README are trimmed.
