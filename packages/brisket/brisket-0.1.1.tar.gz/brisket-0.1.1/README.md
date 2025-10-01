# brisket

Fast cython powered 1 hot encoding for DNA sequences

## Installation

```bash
$ pip install brisket
```

## Usage

```python
import numpy as np
from brisket import encode_seq

# Encode a DNA sequence to one-hot format
dna_sequence = "ATCG"
encoded = encode_seq(dna_sequence)

print(encoded)
# Output: 2D numpy array with shape (seq_length, 4)
# [[1 0 0 0]  # A
#  [0 0 0 1]  # T  
#  [0 1 0 0]  # C
#  [0 0 1 0]] # G

# The encoding maps: A=column 0, C=column 1, G=column 2, T=column 3
# Each row represents one nucleotide position
# Each column represents one of the four DNA bases (A, C, G, T)

# Invalid characters (not A, T, C, G) result in all-zero rows
encoded_with_n = encode_seq("ATCGN")  # Last row will be [0 0 0 0]

```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`brisket` was created by Natalie Gill and Sean Whalen. It is licensed under the terms of the MIT license.

## Credits

`brisket` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
