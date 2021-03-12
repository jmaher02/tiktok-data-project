'''
Testing the various hashtag methods,

Particularly observing the similar data among TikToks with the same hashtag
'''

from TikTokApi import TikTokApi
from helper import *

# api = TikTokApi.get_instance()
# If playwright doesn't work for you try to use selenium
api = TikTokApi.get_instance(use_selenium=True)
results = 20

hashtags = api.discoverHashtags()
print_hashtag( hashtags )


# View first 20 tiktoks of the top trending hashtag
tag_title = hashtags[0]['cardItem']['title'][1:]
print('Showing ' + str(results) + ' TikToks for #' + tag_title)

tag_tiktoks = api.byHashtag(tag_title, results)
print_tiktoks(tag_tiktoks)

