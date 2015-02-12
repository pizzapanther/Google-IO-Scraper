#!/usr/bin/env python

import json
import urlparse

def dump_page (images, page):
  fw = open('json/data{}.json'.format(page), 'w')
  fw.write(json.dumps({'images': images}))
  fw.close()
  
def run ():
  fh = open('images.json', 'r')
  count = 1
  page = 1
  used = []
  images = []
  while 1:
    line = fh.readline()
    if line:
      line = line[:-1]
      if line.startswith('['):
        line = line[1:]
        
      if line.endswith((',', ']')):
        line = line[:-1]
        
      try:
        data = json.loads(line)
      except:
        print line
        
      for img in data['image_urls']:
        if img.startswith(('http://', 'https://')):
          url = img
          
        else:
          url = urlparse.urljoin(data['url'], img)
          
        if url not in used:
          used.append(url)
          images.append(url)
          
          count += 1
          
          if count % 300 == 0:
            print count
            dump_page(images, page)
            images = []
            page += 1
            
    else:
      page += 1
      dump_page(images, page)
      break
      
if __name__ == "__main__":
  run()
  
