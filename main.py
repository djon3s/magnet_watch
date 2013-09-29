import os
import mechanize
import difflib
import subprocess
from bs4 import BeautifulSoup

import settings

def is_magnet_link(link):
    if link[0:7] == 'magnet:':
        return True

def write_new_seen(links, seen_links_loc):
    for link in links:
        with open(seen_links_loc, 'a') as seen:
            seen.write(link + '\n')

def check():
    mech = mechanize.Browser()
    url = settings.watch_url
    soup = BeautifulSoup(mech.open(url).read())
    links = [x['href'] for x in soup.findAll('a')]
    links = filter(is_magnet_link, links)
    seen_links_loc = '%s/seen.list' % settings.working_dir

    if os.path.exists(seen_links_loc):
        with open(seen_links_loc, 'r') as seen:
            seen_links = [x.strip() for x in seen.readlines()]
        diff = difflib.context_diff(seen_links, links)
        if links != seen_links:
            for d in diff:
                if d[0:1] == '+':
                    magnet_link = d[2:]
                    print("adding new magnet link: " + magnet_link)
                    subprocess.call(
                            [
                            'bash',
                            '%s/convert.sh' % settings.working_dir,
                            settings.torrent_watch_dir,
                            magnet_link])
            write_new_seen(links, seen_links_loc)
    else:
        write_new_seen(links, seen_links_loc)

if __name__ == '__main__':
    check()

