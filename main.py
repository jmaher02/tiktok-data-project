'''
Obtain Unique TikTok Users

In this attempt, we utilize getSuggestedUsersbyIDCrawler
through several iterations to expand our list of users to compare.

FINDINGS:  After the first generation of getSuggestedUsersbyIDCrawler,
  even using the lowest users on the list will result in the same list
  of users.

UNIQUENESS: Only the initial ___ calls to getSuggestedUsersbyIDCrawler
  seems produce unique users. After ___ calls, the list is unchanged
'''

'''
Steps in console for preparing virtual environment
\ virtualenv env
\ cd env/Scripts
\ activate
\ cd ..
\ cd ..
\ pip install TikTokApi
\ python -m playwright install

'''

from TikTokApi import TikTokApi
from helper import *

api = TikTokApi.get_instance()
# If playwright doesn't work for you try to use selenium
# api = TikTokApi.get_instance(use_selenium=True)
results = 20
# Since TikTok changed their API you need to use the custom_verifyFp option.
# In your web browser you will need to go to TikTok, Log in and get the s_v_web_id value.
#   -- Need new cookie at least every two hours
verifyFp="verify_kmzi469d_KoCJiB2v_ISOW_47pr_9rDc_liZykxBl4BqL"

trending = api.trending(count=results, custom_verifyFp=verifyFp)

user_list = api.getSuggestedUsersbyIDCrawler(count=results)
print_user_data( user_list )
print('Done')


#=========  FIRST ATTEMPT, Collect users from tiktok =============
# Generate more users, set seed with IDCrawler users
'''
seed_ids = []
for user in user_list:
    seed_ids.append(user['extraInfo']['userId'])
suggested = [api.getSuggestedUsersbyID(count=100, startingId=s_id) for s_id in seed_ids]

i=0
for seed in suggested:
    print('===========USER '+ str(i) + '===============')
    i+= 1
    for user in seed:
        print(user['title'])
    print('==========================')
print('Done')
'''

#=========  SECOND ATTEMPT, Collect from bottom of list ==============
# Generate users from second generation list
seed_ids = get_seeds(user_list)

suggested = [api.getSuggestedUsersbyID(count=30, startingId=s_id) for s_id in seed_ids]

seed_ids = []  #Empty seeds, gather second gen ids
usernames = []
for seed in suggested:
    for user in seed:
        #print(user['title'])
        id = user['extraInfo']['userId']
        if is_unique(seed_ids, id):
            seed_ids.append(id)
            usernames.append(user['title'])
print('Done')

print('Unique Seeds after Second Generation: ' + str(len(seed_ids)))

for i in range( len(seed_ids)):
    print(usernames[i] + "  ID: " + str(seed_ids[i]))

#=============== THIRD ATTEMPT ==========================
#pull bottom 5 and try again
new_seeds = []
for i in range(5):
    index = len(seed_ids) - (i+1)
    new_seeds.append(seed_ids[index])
print('Bottom Five Seeds')
for seed in new_seeds:
    print( seed )
suggested = [api.getSuggestedUsersbyID(count=30, startingId=s_id) for s_id in new_seeds]

seed_ids = []  #Empty seeds, gather second gen ids
usernames = []
for seed in suggested:
    for user in seed:
        #print(user['title'])
        id = user['extraInfo']['userId']
        if is_unique(seed_ids, id):
            seed_ids.append(id)
            usernames.append(user['title'])
    print('================================')
print('Done')

print('Unique Seeds after Third Generation: ' + str(len(seed_ids)))

for i in range( len(seed_ids)):
    print(usernames[i] + "  ID: " + str(seed_ids[i]))
