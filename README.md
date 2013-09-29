magnet_watch
============

watch pages for new magnet links.

example: if you have a page full of magnet links ordered chronologically by
upload date and want to grab any new ones when they appear, you can run this
script.

this is a very specific script, and is duct-taped together. it currently
runs a bash script to convert the magnet link into a .torrent file

the first time it runs, it will create a list of magnet files in the working
dir. nothing is converted/downloaded. this is the initial state. it detects
a new magnet link by going to the page, gettings the magnet links, then diffing
the 'seen' set of links with the current set of links. that's my story and i'm
sticking to it

prereqs
-------
pip install mechanize beautifulsoup4

instructions
------------
1. take the settings.py.example file and rename to settings.py
2. edit settings.py to include the page to watch, the dir that will be watched
   by a torrent client, and your working directory
3. run from crontab
