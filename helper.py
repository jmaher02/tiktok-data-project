

# method to format the list of users
#   prints user's title, fan count, likes, and userID
def print_user_data( user_list ):
    i = 0
    for user in user_list:
        print(str(i) + ': ' + user['title'] + " FANS:" + str(user['extraInfo']['fans']) + " LIKES:" + str(
            user['extraInfo']['likes']) + " ID:" + str(user['extraInfo']['userId']))
        i += 1

#   print user data from the hashtag list
def print_user_objects( user_list):
    i = 0
    for user in user_list:
        print(user['userInfo']['user']['nickname'] + " FOLLOWERS:" + str(user['userInfo']['stats']['followerCount']) +
          " LIKES:" + str(user['userInfo']['stats']['heart']) + " ID:" + str(user['userInfo']['user']['id']))
        i += 1

#   gather average, max, and min number of followers from list of users
def hashtag_user_stats( users ):
    sum = 0
    min = 0
    max = 0
    for i in range(len(users)):
        user=users[i]
        follow = user['userInfo']['stats']['followerCount']
        sum = sum + follow
        if i == 0:
            min = follow
            max = follow
        elif follow < min:
            min = follow
        elif follow > max:
            max = follow

    avg = sum / len(users)
    return [avg, max, min]



#   prints the hashtag data, title and number of views
def print_hashtag( tag_list ):
    for tag in tag_list:
        print( tag['cardItem']['title'] + ' VIEWS: ' + str( tag['cardItem']['extraInfo']['views']))

#   prints the dictionary of TikToks. All data output
def print_tiktoks( tiktok_list):
    for tiktok in tiktok_list:
        print(tiktok)

#   prints the TikTok found, formatted
def print_tiktoks_format( tiktok_list, api):
    for tiktok in tiktok_list:
        username = tiktok['author']['uniqueId']

        print(username + '  UserID: ' + str(tiktok['author']['id']))
        user = api.get_user( username )
        print(user)

#   from a given list of tiktoks, return all user objects
def get_userobj_from_list( tiktok_list, api ):
    users = []
    for tiktok in tiktok_list:
        username = tiktok['author']['uniqueId']
        user = api.get_user( username )
        users.append(user)
    return users

# Collect userIDs from a list of TikTok users
def get_seeds( user_list ):
    seed_ids = []
    for user in user_list:
        seed_ids.append(user['extraInfo']['userId'])
    return seed_ids



# Check for unique elements
def is_unique( seed_list, item ):
    for value in seed_list:
        if item == value:
            return False
    return True

