# CodeLineCounter

**CodeLineCounter** is a simple application designed to count lines of code in selected Python files (.py).
With an intuitive interface and straightforward functionality, it helps developers quickly assess the size of their Python projects and analyze code across multiple .py files.

## Features

- Count total lines of code in selected files.
- Support for selecting multiple files or entire directories.
- Display results in a clear and concise manner.
- Option to filter files by extensions (`.py`, more in future).
- User-friendly interface using PyQt6.

## Installation
**Tested only on Windows (IDE: VS Code, PyCharm)**
1. Clone the repository:
    ```
    git clone https://github.com/Jin-Mach/CodeLineCounter.git
    ```

2. Navigate to the project directory:
    ```
    cd CodeLineCounter
    ```

3. Create a virtual environment:
    ```
    python -m venv .venv
    ```

4. Activate the virtual environment:

   - On Windows (Command Prompt):
     ```
     .venv\Scripts\activate
     ```
   - On Windows (PowerShell):
     ```
     .venv\Scripts\activate.ps1
     ```
   - On macOS/Linux:
     ```
     source .venv/bin/activate
     ```

5. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

## Usage
To run the application, execute the following command:
    ```
    python CodeLineCounter.py
    ```

## License
This project is licensed under the MIT License.

## Contact
For any questions or feedback, feel free to reach out via my GitHub profile: [Jin-Mach](https://github.com/Jin-Mach).