# Typograf Service

The project prepare your russian text to publish in web-page.

Now script can this:

- delete two or more spaces
- change `(c)` to &copy;
- delete double words
- add comma before conjuction
- add hyphen before postfix
- add hyphen after postfix
- delete double symbols
- change hyphen to &mdash;
- delete spaces before punctuation
- add space after punctuation
- delete spaces before percent
- add and delete spaces before and after brackets
- change quotes to &laquo; and &raquo;
- bind small word (1-3 characters) to next word
- change hyphen to &ndash; in telephone number
- bind digit to next word

# Requirements

- Python 3.6
- Flask
- Virtualenv(optional)

# How to install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
$ pip install -r requirements.txt # alternatively try pip3
```
Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# How to launch

1. Export flask environment variable:
```bash
$ export FLASK_APP=server.py
```

2. Optional enable flask debug mode:
```bash
$ export FLASK_DEBUG=1
```

3. Run application
```
$ flask run
```

4. Application will be run on http://127.0.0.1:5000/ 

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
