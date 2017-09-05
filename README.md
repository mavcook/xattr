# xattr
A script to add attributes to macOS files. Currently only works with the tags attribute.

# Use
## Requirements
macOS
Python 2.7 or greater

---
For an easy way to pass in the list of files, after entering the -f flag, enter in qoute, then drag a selection of files from Finder into the terminal, and close with another qoute.

Select your files in Finder, and drag

```
python xattr.py -a "coolpic;coolertag" -f "/Users/indy/lostarkpics/henry.jpg /Users/indu/lostarkpics/leapoffaith.png"
```

## Options
```
-o
overwrite a the existing attributes
```

# Troubleshooting
Currently does not work for filepaths with spaces in them.
