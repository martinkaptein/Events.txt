# Events.txt

Full featured calendar solution in plain text format.

## Format

The Events.txt plain text calendar file has the following format (example):


```
.
.
.
May
01/05/2022 Sun | + Event
______
02/05/2022 Mon |
03/05/2022 Tue |
04/05/2022 Wed | + 1200 May the force be with you
+ 1230 More events added on new lines to improve readability
+ 1300 May the force stay with you
+ 1800 Hopefully it is still there
05/05/2022 Thu |
06/05/2022 Fri | + 0600 Is the force there?
.
.
.
etc.
#repeatingYearly
04/05 - 1200 May the force be with you (this is an event (like a birthday) which repeats every year)
```

This concept has been inspired by [this amazing post on the internet](https://danlucraft.com/blog/2008/04/plain-text-organizer/).
Feel free to change the format as you please.

Every Events starts with a `+` character, in order to quickly scan through all events just using search.

Repeating events should be added below `#repeatingYearly` and start with a dash (`-`). The script `maintain.py` adds these events automatically, whilst "filling" the Events.txt file up with additional days (can be defined in script).

Note: Until now, #repeatingYearly assumes, that those events repeat each year. The script expects only day/month format.
The recommended practise is to always keep repeating events inside #repeatingYearly. This way, they wont get "lost" after a few years.

The maintain.py script does not get rid of past days. It is up to the user, what to do with past events.

## Script usage

To make your own Events.txt from scratch:

```
python3 make.py > Events.txt
```

This generates an empty Events.txt.
Open, view and edit with any text editor, on any device, using the convention above.

In order to maintain (=fillup with new days, take care of repeating events) your calendar run:

```
python3 maintain.py
```

It assumes that your file is called `Events.txt`.
