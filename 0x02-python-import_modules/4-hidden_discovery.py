#!/usr/bin/python3

if __name__ == "__main__":
    import py_compile
    import imp

    pyc_file = './hidden_4.pyc'
    py_compile.compile(pyc_file)

    hidden = imp.load_compiled('hidden', pyc_file)

    names = [name for name in dir(hidden) if not name.startswith('__')]

    for name in sorted(names):
        print(name)
