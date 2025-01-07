import os
import nbformat
from nbconvert.preprocessors import ClearOutputPreprocessor

def clear_outputs_in_directory(directory="."):
    print(f"Clearing outputs in {directory}")
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        if full_path.endswith(".ipynb"):
            with open(full_path, "r") as f:
                notebook = nbformat.read(f, as_version=nbformat.NO_CONVERT)
            preprocessor = ClearOutputPreprocessor()
            notebook, _ = preprocessor.preprocess(notebook, {})
            with open(full_path, "w") as f:
                nbformat.write(notebook, f)
            print(f"Cleared outputs in {full_path}")

        # check if file is a directory, if yes recursively call the function
        elif os.path.isdir(full_path):
            clear_outputs_in_directory(full_path)

clear_outputs_in_directory()