#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2023-03-21 00:42:28 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#
from random import randint
from pyzotero import zotero
import requests
import subprocess
import time
import os, sys

# Replace YOUR_API_KEY with your Zotero API key
api_key = os.getenv('ZOTERO_KEY')

library_id = os.getenv('ZOTERO_ID')
library_type = 'user'

from summarize_text import summarize
from pdf_to_text import pdf_to_text

from tools import progressBar

def summarize_zotero():
    zot = zotero.Zotero(library_id, library_type, api_key)
    collections = zot.collections_top() # Returns a library’s top-level collections.

    for collection in collections:
        if "Must Read" in collection['data']['name']:
            collection_key = collection['data']['key']
            print(f'''
    [{collection['data']['name']}]
            ''')
            collection_items = zot.collection_items(collection_key) # Returns items from the specified collection. This does not include items in collections
            
            if collection_items:
                rand_num = randint(0, len(collection_items)-1)
                for i, item in enumerate(collection_items):
                    progressBar(i, len(collection_items), bar_length=25)
                    if "attachment" in item['data']['itemType']:

                        # Pick random article
                        if i == rand_num:
                            print(f"{i}:{rand_num} {item['data']['filename']}")
                            while True:
                                try:
                                    item_key = item['data']['key']
                                    url = item['data']['url']
                                    filename = item['data']['filename']

                                    if ".pdf" in filename:

                                        newfilename = "".join(filename.replace("'","").replace(".-","-").split())

                                        # Download file
                                        response = requests.get(url, stream=True)

                                        with open(os.path.expanduser("text_files/"+newfilename), 'wb') as f:
                                            for chunk in response.iter_content(chunk_size=1024):
                                                if chunk:
                                                    f.write(chunk)

                                        print(f'\n\nDownloaded file: {newfilename}')

                                        quick_summary = summarize("text_files/"+pdf_to_text(newfilename), item_key, collection_key, zot)

                                        return [filename, quick_summary, url]

                                    else:
                                        url = item['data']['url']
                                        filename = item['data']['filename']
                                        return [filename, None, url]

                                except subprocess.CalledProcessError as e:
                                    print(f"\n\n'{e.cmd}' failed, trying again...\n\n")
                                    print(url)
                                    time.sleep(20)
                                    
                                except requests.exceptions.MissingSchema as e:
                                    url = item['data']['url']
                                    filename = item['data']['filename']
                                    return [filename, None, url]

                        if item['data']['url']:
                            url = item['data']['url']
                            return [item['data']['title'], None, url]
