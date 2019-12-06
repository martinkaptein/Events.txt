# Events.txt

Org-mode replacement, full-featured calendar in a plain-text file, without emacs. With all the benefits.

# Format

File has predefined months, which can be "generated" using a script (such as gen.py), but it's not required.

For this you are free to use the script provided.

The Events.txt file generally looks like this:

```
___Events (dot) txt___
__@username__
.
.
.
29/04/2022 Fri | 
30/04/2022 Sat | + 2300 stuff #randomHashtag


May
01/05/2022 Sun |
______
02/05/2022 Mon |
03/05/2022 Tue |
04/05/2022 Wed | + 1200 May the force be with you #maytheforce
+ 1300 May the force stay with you
+ 1800 Hopefully it is still there
05/05/2022 Thu |
06/05/2022 Fri | + 0600 Is the force there? #maytheforce
.
.
.
etc.
#oob
```

Inspired by [this amazing post on the internet](https://danlucraft.com/blog/2008/04/plain-text-organizer/).

Search for `#oob (out-of-bounds)` to add events outside of the file scope (as defined in generator script).

Every Events starts with a `+` character, in order to quickly scan through all events just using search.

To make your own Event.txt from scratch:

```
touch Events.txt
python3 gen.py >> Events.txt
```

Open, view and edit with any text editor, on any device, using the convention above.
