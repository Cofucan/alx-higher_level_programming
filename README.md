<h1 align="center">ALX Higher-Level Programming</h1>
This repository contains my code submissions to tasks given while studying higher level programming in the ALX Software Engineering program. It contains Python, C and SQL code.

---

<p align="center">
<a target="_blank" href="https://www.alxafrica.com/"><img src="https://github.com/Cofucan/alx-low_level_programming/blob/main/alx.jpg?raw=true" width="350"></a>
<a target="_blank" href="https://www.holbertonschool.com/"><img src="https://github.com/Cofucan/alx-low_level_programming/blob/main/holby.jpg?raw=true" width="350"></a>
</p>

---

## Table of contents

- [Table of contents](#table-of-contents)
- [Technologies Used](#technologies-used)
- [Projects](#projects)
- [Usage](#usage)
- [Inspiration](#inspiration)

## Technologies Used

The Python scripts were tested with **Python 3.11.2** but are built using Python **3.8.X** in a virtual environment as instructed.

- [GCC](https://gcc.gnu.org/): Compiler for C/C++.
- [Make](https://www.gnu.org/software/make/manual/make.html): Utility tool that I use for running repetitive commands.
- [Valgrind](https://valgrind.org/): A programming tool for memory debugging, leak detection and profiling.
- [Betty](https://github.com/holbertonschool/Betty): Holberton-style C code checker written in Perl.
- [GDB](https://www.sourceware.org/gdb/): Command-line debugger that works with many low level languages including C/C++.
- [Oh-My-ZSH](https://ohmyz.sh/): A Unix shell, similar to Bash.
- [Neovim](https://neovim.io/): An upgraded version of the VIM code editor.
- [Lunarvim](https://www.lunarvim.org/): An IDE layer for Neovim with sane defaults. Completely free and community driven.
- [WSL](https://learn.microsoft.com/en-us/windows/wsl/install): Windows OS feature, by Microsoft, that enables Linux to be run natively on Windows.
- [PyCodeStyle](https://pypi.org/project/pycodestyle/): Python style guide checker.

Some scripts need more specific requirements, but these will be shown where they are needed.

## Projects

Here is the complete list of projects in this repository, each project has its description in its respective folder.

- [0x00. Python - Hello, World](https://github.com/Cofucan/alx-higher_level_programming/tree/main/0x00-python-hello_world)
- [0x01. Python - if/else, loops, functions](https://github.com/Cofucan/alx-higher_level_programming/tree/main/0x01-python-if_else_loops_functions)
- [0x02. Python - import & modules](https://github.com/Cofucan/alx-higher_level_programming/tree/main/0x02-python-import_modules)
- [0x03. Python - Data Structures: Lists, Tuples](https://github.com/Cofucan/alx-higher_level_programming/tree/main/0x03-python-data_structures)
- [0x04. Python - More Data Structures: Set, Dictionary](https://github.com/Cofucan/alx-higher_level_programming/tree/main/0x04-python-more_data_structures)

## Usage

Each project and task contains the instructions to compile the code and execute the results. The Python version required for this project is `3.8.5` but most Linux systems come with more recent versions of Python. So I made use of a virtual environment created with the latest version of Python `3.8.X` so that my default global Python still remains the latest version. Here is an outline of how to do that.

1. Install the latest version of Python 3.8.X on your Linux. Follow [this link](https://blog.ruanbekker.com/blog/2022/06/23/install-a-specific-python-version-on-ubuntu/) for a guide.
2. After its installed, you need to temporarily make it the default Python version. Follow [this link](https://www.baeldung.com/linux/default-python3) for a guide on how to go about it. When you get to the part about editing the bash aliases file using `sudo vi ~/.bash_aliases` file, after opening the file, comment out any alias that was set there before (don't delete). Then add the alias for the Python version you just installed. When you save it and activate the alias using `source ~/.bash_aliases`, the default Python version will be changed. You can check with `python3 --version`.
3. Now go to the root directory of this project and create a new virtual environment using `python3 -m venv venv`. This virtual environment will now be created using the default global Python version which we just set (version 3.8.X).
4. After this, go back and edit the bash aliases file by running `sudo vi ~/.bash_aliases` then comment out the new aliases you added and comment back the initial one that was there, if any. After saving, activate the alias again using `source ~/.bash_aliases` and the default Python version that was there before will be set.
5. Now you just need to activate the virtual environment in this project folder using `source venv/bin/activate` and install any requiremnets using `pip3 install -r requirements.txt`.

## Inspiration

The format for the Readme files in this project was heavily inspired by [Santiago Arboleda](https://github.com/monoprosito), a former student of Holberton School Software Engineering.
