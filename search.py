#!/usr/bin/python2

# HSU

from apiclient.discovery import build
import argparse
import urllib, cv2
from skimage import io
import numpy as np

def cse_search(query,engineId,apiKey,start=1,total=1,searchImage=True):
    service = build('customsearch', 'v1', developerKey=apiKey)
    cnt=0
    resList = []
    while cnt < total:
        num = min(10,total-cnt)
        # image search
        if searchImage: 
            res = service.cse().list(
                q=query,
                cx=engineId,
                searchType='image',
                imgColorType='color',
                start= start,
                num=num
                ).execute()
        # web search
        else: 
            res = service.cse().list(
                q=query,
                cx=engineId,
                start= start,
                num=num
                ).execute()
        start = start + num
        cnt = cnt + num
        #print res
        for i in range(len(res[u'items'])):
            resList.append(res[u'items'][i][u'link'])
    return resList
    
def main(query):
    engineId = ''
    apiKey = ''
    
    # api call
    results = cse_search(query=query, 
        #total=args.n, 
        searchImage=True, 
        engineId=engineId,apiKey=apiKey)

    # display results
    for url in results:
        print(url)
        img = io.imread(url)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        cv2.imshow('URL Image', img)
        cv2.waitKey()
        wait = cv2.waitKey(1) & 0xFF
 
    # if the `q` key is pressed, break from the lop
        if wait == ord("n"):
            break
        #file = cStringIO.StringIO(urllib.urlopen(url).read())
        #img = Image.open(file)



if __name__ == '__main__':
  main(query)
