# imgtagchecker

Python script to add `alt` and/or `title` attribute(s) to HTML `img` tags, based on the name of the image file.

For example, if it finds this tag:

```html
<img src="static/img/bart-simpson.jpg"/>
```

It will replace it with:

```html
<img alt"Bart Simpson" src="static/img/bart-simpson.jpg" title="Bart Simpson"/>
```

The script creates a copy of the original file  with the changes.

If the name of your file is `index.html`, the script will create another one, in the same directory, named `index.html.new`

### Requirements

Python 3.10.x
BeaultifulSoup 4.10.x

### Setup

1. Clone this repository.
2. Navigate into the folder and create a Python virtual environment:
```bash
python -m venv venv
```
3. Activate the virtual environment:
```bash
source venv/bin/activate
```
4. Install the requirements:
```bash
pip install -r requirements.txt
```

### Usage

- Check only one file:
```bash
python path/to/imgtagchecker.py path/to/file.html
```
- Check all files within a directory:
```bash
python path/to/imgtagchecker.py path/to/directory/*
```

### TODO

- Make a backup of the original files before replacing them.
- BeautifulSoup formats HTML with 1 space, find a way to use 4 spaces.
- Add setup instructions for Windows
