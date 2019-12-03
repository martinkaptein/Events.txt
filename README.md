# Events.txt
Org-mode replacement

# Format

File has predefined months, which can be "generated" using a script (such as gen.py), but it's not required.

The Events.txt file generally looks like this:

```
.
.
.
29/04/2022 Fri | 
30/04/2022 Sat | 2300 stuff


May
01/05/2022 Sun |
02/05/2022 Mon |
03/05/2022 Tue |
04/05/2022 Wed | 1200 May the force be with you
  1300 May the force stay with you
  1800 Hopefully it is still there
05/05/2022 Thu |
06/05/2022 Fri | 0600 Is the force there?
.
.
.
etc.
```

To make your own Event.txt from scratch:

```
touch Events.txt
python3 gen.py >> Events.txt
```

Open, view and edit with any text editor, on any device, using the convention above.
