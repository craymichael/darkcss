# Dark CSS

Parses a CSS file and then prints to stdout the CSS in "dark mode":
low-saturation colors in CSS rules are inverted. If no CSS file is provided,
then input is assumed to come in from stdin.

## Installation

This repository only requires a single package: `tinycss2` (a lightweight CSS 
tokenizer with serialization capability). To install:

```shell script
git clone https://github.com/craymichael/darkcss.git
cd darkcss/
pip install -r requirements.txt
```

## Usage

```text
Usage: darken.py [file.css] [--help]

Example usages:
  darken.py mysite.css > from_file.css
  echo mysite.css | darken.py > from_stdin.css
  xclip -o | darken.py > from_clipboard.css
  xclip -o | darken.py | xclip -section c
```

On Linux `xclip` reads from and writes to the X session clipboard. A helpful
`alias` for the above example usage is shown below.  
```shell script
alias xclip='xclip -selection c'
# Read copied CSS from clipboard, write dark CSS back to clipboard
xclip -o | python darken.py | xclip
```
