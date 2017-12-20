#!/usr/bin/env python3
import twitter
import os
import time
import creds

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
    s = api.GetStatus(imgId)
    cr = s.created_at_in_seconds
    score = s.favorite_count + s.retweet_count
    timeUp = (time.time() - cr) / 3600 # Hours up
    return score/timeUp

# Get the filenames of the two most popular tweets
def getMostPopularTweets():
    tids = []

    for x in os.listdir(FLAME_DIR):
        if x.endswith(".flam3"):
            tids.append(x[:-len(".flam3")])

    a, b = sorted(tids, key=getImageScore, reverse=True)[:2]

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
