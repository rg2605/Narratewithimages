import time  
import sys  
import os
import argparse
from urllib.request import Request, urlopen
from urllib.request import URLError, HTTPError
import random


                
class downloader(object):
    
    def download_page(self , url):
        import urllib.request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers=headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    

    def _images_get_next_item(self , s):
        start_line = s.find('rg_di')
        if start_line == -1: 
            end_quote = 0
            link = "no_links"
            return link, end_quote
        else:
            start_line = s.find('"class="rg_meta"')
            start_content = s.find('"ou"', start_line + 1)
            end_content = s.find(',"ow"', start_content + 1)
            content_raw = str(s[start_content + 6:end_content - 1])
            return content_raw, end_content

    def _images_get_all_items(self , page):
        items = []
        mn = 0
        while mn<2:
            item, end_content = self._images_get_next_item(page)
            if item == "no_links":
                break
            else:
                items.append(item)
                time.sleep(0.1) 
                page = page[end_content:]
                mn = mn + 1
        return items

    def download(self ,keywords):
        itemis = []
        for keyword in keywords:
            items = []
            search_term = keyword
            search = search_term.replace(' ', '%20')
            url = 'https://www.google.com/search?q=' + search + '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch'
            raw_html = (self.download_page(url))
            time.sleep(0.1)
            items = items + (self._images_get_all_items(raw_html))
            itemi= items[1]
            itemis.append(itemi)
        return itemis
    def get_images(self, items, dir_name):
        for item in items:
            try:
                req = Request(item, headers={
                    "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"})
                response = urlopen(req, None, 15)
                image_name = str(item[(item.rfind('/'))+1:])
                if '?' in image_name:
                    image_name = image_name[:image_name.find('?')]
                if ".jpg" in image_name or ".png" in image_name or ".jpeg" in image_name or ".svg" in image_name:
                    output_file = open(dir_name + "/" + str(1) + ". " + image_name, 'wb')
                else:
                    output_file = open(dir_name + "/" + str(k + 1) + ". " + image_name + ".jpg", 'wb')
                    image_name = image_name + ".jpg"
                data = response.read()
                output_file.write(data)
                response.close()
            except IOError:
                print("IOError on image ")

            except HTTPError as e:  # If there is any HTTPError
                print("HTTPError")
            
            except URLError as e:
                print("URLError ")
 
