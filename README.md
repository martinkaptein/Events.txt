# Events.txt

Org-mode replacement, full-featured calendar in a plain-text file, without emacs. With all the benefits.

# Format

File has predefined months, which can be "generated" using a script (such as make.py), but it's not required.

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
#repeatingYearly
04/05 - May the force (this event repeats each year)

#oob
14/05/2040 - This is just an event, which is very far away in the future and hasn't found its place in Events.txt yet.
```

Inspired by [this amazing post on the internet](https://danlucraft.com/blog/2008/04/plain-text-organizer/).

Search for `#oob (out-of-bounds)` to add events outside of the file scope (as defined in generator script).

Every Events starts with a `+` character, in order to quickly scan through all events just using search.

WORK IN PROGRESS

Repeating events should be added below `#repeatingYearly` and start with a dash (`-`). The script `maintain.py` adds these events automatically, whilst "filling" the Events.txt file up with additional days (can be defined in script).

Note: Until now, #repeatingYearly assumes, that those events repeat each year. The script expects only day/month format.

The recommended practise is to always keep repeating events inside #repeatingYearly. This way, they wont get "lost" after a few years.

The maintain.py script does not get rid of past days. It is up to the user, what to do with past events.

Myself, usually I just delete each day the previous day, symbolising the passing of each day in a philosophical sense. In some cases, it would be smart, however, to maintain a record of all previous events. 

Hence, this is functionality which might also be added later.


To make your own Event.txt from scratch:

```
touch Events.txt
python3 make.py >> Events.txt
```

This generates an empty Events.txt.

Open, view and edit with any text editor, on any device, using the convention above.

# Additional notes

Until now, you will have to manually insert #oob events into the correct date inside Event.txt. However, this functionality is definitely planned, and will be added in a future release.

 
