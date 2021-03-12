from TikTokApi import TikTokApi
from helper import *

# api = TikTokApi.get_instance()
# If playwright doesn't work for you try to use selenium
api = TikTokApi.get_instance(use_selenium=True)
results = 20
# Since TikTok changed their API you need to use the custom_verifyFp option.
# In your web browser you will need to go to TikTok, Log in and get the s_v_web_id value.
#trending = api.trending(count=results, custom_verifyFp="verify_kllm1c0a_4c9EuLXw_u1ZP_4d6c_BLLo_wlpjV1ZiRnF4")

user_list = api.getSuggestedUsersbyIDCrawler(count=results)
print_all_data( user_list )
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

#seed_ids = []  #Empty seeds, gather second gen ids
#usernames = []
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
