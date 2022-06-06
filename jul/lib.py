from unicodedata import name

from isort import code


def try_me(name):
  code = f"hello {name}"
  return code

print(try_me('julien'))
