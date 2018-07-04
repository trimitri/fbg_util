"""Some tools for working with ipython or jupyter."""

import os
import pickle
import subprocess
from typing import Any

def unpickle_sh(file_name: str) -> Any:
    """Unpickle `base_name`.pkl if present or run `base_name`.pkl.sh first. """
    if not os.path.isfile(file_name):
        subprocess.call([file_name + '.sh'])
    with open(file_name, 'rb') as file:
        return pickle.load(file)
