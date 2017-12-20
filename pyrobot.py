#!/usr/bin/env python3
import twitter
import os
import time
import creds
import math
import random

FLAME_DIR = "flames"

api = twitter.Api(consumer_key=creds.consumer_key,
                  consumer_secret=creds.consumer_secret,
                  access_token_key=creds.access_token_key,
                  access_token_secret=creds.access_token_secret)

# Post an image and return the id
def postImage(img):
    return api.PostUpdate("", img).id

# Get the score of an image, given its tweet ID
def getImageScore(imgId):
    s = api.GetStatus(imdId)
    cr = s.created_at_in_seconds()
    score = s.favorite_count + s.retweet_count
    timeUp = math.ceil((time.time() - cr) / 386400) # Days up
    return score/timeUp

# Gets the filenames of the two most popular tweets
def getMostPopularTweets():
    tids = []

    for x in os.listdir(FLAME_DIR):
        if x.endswith(".flam3"):
            tids.append(x.rstrip(".flam3"))

    a, b = sorted(tids, key=getImageScore, reverse=True)[:2]
    
    apath = os.path.join(FLAME_DIR, a + ".flam3")
    bpath = os.path.join(FLAME_DIR, b + ".flam3")

    return apath, bpath


# Gets two Tweets to mutate and breed. 
def getTweetsMutate():
    tids = []

    for x in os.listdir(FLAME_DIR):
        if x.endswith(".flam3"):
            tids.append(x.rstrip(".flam3"))
    
    tids = sorted(tids, key=getImageScore, reverse=True)
    
    index = math.ceil(len(tids) / 2)
    a = tids[index]
    
    upper = math.ceil(len(tids) / 8)
    index = 0 - random.randint(1, upper)
    b = tids[index]
    
    apath = os.path.join(FLAME_DIR, a + ".flam3")
    bpath = os.path.join(FLAME_DIR, b + ".flam3")

    return apath, bpath

if __name__=='__main__':
    import sys
    ret = {
        "post": postImage,
        "popular": getMostPopularTweets,
    }[sys.argv[1]](*sys.argv[2:])
    if isinstance(ret, tuple):
        for x in ret: print(x)
    else:
        print(ret)
