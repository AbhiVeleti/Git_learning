# Command-Line Utility

This project implements a basic command-line interface (CLI) that mimics common shell commands. It provides various file manipulation, system information, and date/time retrieval functionalities. It’s built in Python and designed to run in a terminal environment.

## Features

- **File Operations:**
  - `list`: List all files in the current directory.
  - `dirs`: List all directories in the current directory.
  - `cat <file>`: Display the contents of a file.
  - `head <file> <n>`: Display the first `n` lines of a file.
  - `tail <file> <n>`: Display the last `n` lines of a file.
  - `copy_file <src> <dst>`: Copy a file from source to destination.
  - `remove_file <file>`: Remove a file.
  - `empty_file <file>`: Empty the contents of a file.

- **System Information:**
  - `ipconfig`: Get the local machine's IP address.
  - `pwd`: Show the current working directory.
  - `date`: Get the current date.
  - `time`: Get the current time.
  - `time-hours`: Get the current hour.
  - `time-mins`: Get the current minute.
  - `time-secs`: Get the current second.
  
- **Utilities:**
  - `clear`: Clear the terminal screen.

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/command-line-utility.git
    ```

2. Navigate to the project directory:

    ```bash
    cd command-line-utility
    ```

3. Install dependencies (if any). For this particular project, no external dependencies are needed, just Python 3.x.

## Usage

Run the Python script to enter the CLI:

```bash
python3 cli.py
