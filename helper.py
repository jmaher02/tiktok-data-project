

# method to format the list of users
#   prints user's title, fan count, likes, and userID
def print_all_data( user_list ):
    i = 0
    for user in user_list:
        print(str(i) + ': ' + user['title'] + " FANS:" + str(user['extraInfo']['fans']) + " LIKES:" + str(
            user['extraInfo']['likes']) + " ID:" + str(user['extraInfo']['userId']))
        i += 1


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
