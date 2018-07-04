"""Some tools for working with ipython or jupyter."""

import os
import pickle
from stat import S_IEXEC as OWNER_EXECUTABLE
import subprocess
from typing import Any


def pickle_sh(thing: Any, fname: str, generator: str = None) -> None:
    """Pickle something and optionally create a generator script too."""
    if generator is not None:
        gen_script = fname + '.sh'
        with open(gen_script, 'w') as generator_script:
            generator_script.writelines([
                '#!/usr/bin/env sh\n',
                'cd "$(dirname "$0")"\n',
                'jupyter nbconvert --stdout --execute "{}" > /dev/null\n'.format(generator)
                ])
        os.chmod(gen_script, os.stat(gen_script).st_mode | OWNER_EXECUTABLE)
    with open(fname, 'wb') as pickle_file:
        pickle.dump(thing, pickle_file)


def unpickle_sh(file_name: str) -> Any:
    """Unpickle `base_name`.pkl if present or run `base_name`.pkl.sh first. """
    if not os.path.isfile(file_name):
        subprocess.call([file_name + '.sh'])
    with open(file_name, 'rb') as file:
        return pickle.load(file)
