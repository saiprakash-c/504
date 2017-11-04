# ETA Style Guide

ETA is implemented in Python, and we require all contributed code to adhere to
our style. Our priority is *consistency*, so that developers can quickly ingest
and understand the entire ETA codebase. When in doubt, follow the existing
style in the module you are contributing to.

Generally, we follow the [Google Python style](
https://google.github.io/styleguide/pyguide.html), so please review it before
contributing.

Here are some highlights of our Python style:

- Maximum line length is **79 characters**, with the exception of long URLs
that cannot be split

- Indent your code with **4 spaces**. That is, **no tabs**!

- Leave two blank lines between top-level definitions, and one blank line
between class method definitions

- Imports should always be on separate lines at the top of the file, just after
any module comments and doc strings. Imports should be grouped by type with
one space between each group, with the groups sorted in order of most generic
to least generic
    * future import block for Python 2/3 compatibility
    * standard library imports
    * third-party imports
    * application-specific imports

Within each group, imports should be sorted alphabetically by full package
path:

```python
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import *

import os
import sys

import cv2
import numpy as np

from eta.core import utils
from eta.core.serial import Serializable
import eta.core.video as vd
```

- Names should follow the conventions

```python
module_name, package_name, ClassName, method_name, ExceptionName,
function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name,
function_parameter_name, local_var_name
```

- Use `@todo` to mark todo items in the source

- If a class inherits from no other base classes, explicitly inherit from
  `object`

- Follow standard typographic rules for spaces around punctuation

```python
# YES!
spam(ham[1], {eggs: 2}, [])

def complex(real, imag=0.0):
    return magic(r=real, i=imag)

foo = 1000  # comment
long_name = 2  # comment that should not be aligned

dictionary = {
    'foo': 1,
    'long_name': 2,
}
```

```python
# NO!
spam( ham[ 1 ], { eggs: 2 }, [ ] )

def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

foo       = 1000  # comment
long_name = 2     # comment that should not be aligned

dictionary = {
    'foo'      : 1,
    'long_name': 2,
}
```

- All non-trivial public module/class methods should have docstrings describing
  their behavior, inputs, outputs, and exceptions (when appropriate)

```python
def parse_object(d, key, cls, default=None):
    '''Parses an object attribute.

    Args:
        d: a JSON dictionary
        key: the key to parse
        cls: the class of the d[key]
        default: default value if key is not present

    Returns:
        an instance of cls

    Raises:
        ConfigError: if no default value was provided and the key was
            not present in the dictionary.
  '''
  pass
```