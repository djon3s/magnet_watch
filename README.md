magnet_watch
============

watch pages for new magnet links.

example: if you have a page full of magnet links ordered chronologically by
upload date and want to a new one when it appears, you can run this script.

this is a very specific script, and is duct-taped together. it currently
runs a bash script to convert the magnet link into a .torrent file

prereqs
-------
pip install mechanize beautifulsoup4

instructions
------------
1. take the settings.py.example file and rename to settings.py
2. edit settings.py to include the to watch, the that will be watched by a
   torrent client, and your working directory
3. run from crontab
