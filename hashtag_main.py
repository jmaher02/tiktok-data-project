from TikTokApi import TikTokApi
from helper import *

# api = TikTokApi.get_instance()
# If playwright doesn't work for you try to use selenium
api = TikTokApi.get_instance(use_selenium=True)
results = 20

