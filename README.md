# Events.txt
Org-mode replacement

# Format

File has predefined months, which can be "generated" using a script (such as gen.py), but it's not required.

The Events.txt file generally looks like this:

```
:2019.Jan:
:2019.Feb:
24 at 1200, Birthday (sample Event)
:2019.March:
:2019.Apr:

etc.
```

To make your own Event.txt from scratch:

```
touch Events.txt
python3 gen.py >> Events.txt
```

Open and edit with any text editor, on any device, using the convention above.
