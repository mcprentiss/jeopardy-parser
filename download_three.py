#!/usr/bin/env python3 -O3
''' Download the jeopardy archive '''
# -*- coding: utf-8 -*-

import itertools
import os
import urllib.request
import urllib.error
import urllib.parse
import time

CURRENT_WORKING_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_FOLDER = os.path.join(CURRENT_WORKING_DIRECTORY, "j-archive")
SECONDS_BETWEEN_REQUESTS = 1
ERROR_MSG = "ERROR: No game"


def main():
    """ main function """
    create_archive_dir()
    print("Downloading game files")
    download_pages()


def create_archive_dir():
    """ create archive """
    if not os.path.isdir(ARCHIVE_FOLDER):
        print("Making %s" % ARCHIVE_FOLDER)
        os.mkdir(ARCHIVE_FOLDER)


def download_pages():
    """ download pagesss """
    for page in itertools.count(1):
        new_file_name = "%s.html" % page
        destination_file_path = os.path.join(ARCHIVE_FOLDER, new_file_name)
        if not os.path.exists(destination_file_path):
            html = download_page(page)
            if ERROR_MSG in str(html):
                print("Finished downloading. Now parse.")
                break
            if html:
                save_file(html, destination_file_path)
                time.sleep(SECONDS_BETWEEN_REQUESTS)  # be kind to the server
        else:
            print("Already downloaded %s" % destination_file_path)


def download_page(page):
    """ download pagesss """
    url = 'http://j-archive.com/showgame.php?game_id=%s' % page
    html = None
    try:
        response = urllib.request.urlopen(url)
        if response.code == 200:
            print("Downloading %s" % url)
            html = response.read()
        else:
            print("Invalid URL: %s" % url)
    except urllib.error.HTTPError:
        print("failed to open %s" % url)
    return html


def save_file(html, filename):
    '''encoding (ISO-8859-1) Errors were encountered with UTF-8 '''
    try:
        with open(filename, 'w') as FFF:
            FFF.write(html.decode(encoding='ISO-8859-1'))
    except IOError:
        print("Couldn't write to file %s" % filename)

if __name__ == "__main__":
    main()
