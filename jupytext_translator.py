import os
import jupytext

if __name__ == "__main__":
    current_directory = os.getcwd()

    for dirpath, dirnames, filenames in os.walk(current_directory):
        for filename in filenames:
            if filename.endswith(".ipynb"):
                notebook_path = os.path.join(dirpath, filename)
                notebook = jupytext.read(notebook_path)
                py_path = notebook_path.replace('.ipynb', '.py')
                jupytext.write(notebook, py_path, fmt='py:percent')