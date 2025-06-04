# Learning Python

## 2. Using the Python Interpreter

Python as an interpreter:
-->Python is an interpreted language, meaning code is executed line by line.You interact with the Python interpreter via the command line or a shell.
-->Interactive mode vs script mode:
        Interactive Mode:
            Enter python or python3 in the terminal.
            Type code directly, line-by-line. Immediate feedback.
            Great for testing and experimentation.
        
        Script Mode:
            Write code in .py files and run them using python script.py.
            Better for larger programs.

--> Invoking the Interpreter
    Command-line execution:
        You can run Python code using:
            A file: python hello.py
            Inline: python -c "print('Hello')"
            A module: python -m module_name
        Useful command-line flags:
            -i: Interactive mode after running a script.
            -m: Run a module as a script.

    Default encoding is UTF-8.
        You can use non-ASCII characters in identifiers and strings.

-->The Interactive Prompt:
    The primary prompt is >>>, and the continuation prompt is ....
    Automatically prints the result of expressions.
    Good for quick tests and explorations.

-->The Interpreter and Its Environment
    Standard Input/Output:
        input() reads user input.
        print() outputs text to the screen.
    Standard Error:
        Error messages are sent to stderr.
    Scripts receive command-line arguments via sys.argv:
        sys.argv[0] is the script name.
        sys.argv[1:] contains additional arguments.