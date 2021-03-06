Perfume
===

Perfume aims at making Flask-apps more Object-Oriented friendly
by providing a base class to create them.

It's BSD licensed.

Usage:
- inherit from Perfume
- decorate your methods with route(path)

Perfume is Easy
---


```python
import os
from flask import render_template

from perfume import Perfume, route

class Hello(Perfume):

    @route('/')
    def hello(self):
        return "Hello World !"

if __name__ == "__main__":
    Hello(__name__,
          template_folder=os.path.join(os.getcwd(), 'templates'),
          ).run(debug=True)
```

And Easy to Setup
---

```bash
$ pip install Perfume
$ python hello.py
 * Running on http://localhost:5000/
```
