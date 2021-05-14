
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

'''
# View first 20 tiktoks from each of the top trending hashtags

hashtags = api.discoverHashtags()
print_hashtag( hashtags )

for i in range(len(hashtags)):
    # View first 20 tiktoks of the top trending hashtag
    tag = hashtags[i]['cardItem']['title']
    print('\nShowing ' + str(results) + ' TikToks for #' + tag)

    tag_tiktoks = api.byHashtag(tag, results,custom_verifyfp=verifyFp )
    users = get_userobj_from_list(tag_tiktoks, api)
    print_user_objects(users)
    data = hashtag_user_stats(users)
    print("Average: " + str(data[0]) )
    print("Max Followers: " + str(data[1]))
    print("Min Followers: " + str(data[2]))
    '''

#follower data for given user id's

#user_ids=[24335671, 6806701653161624581, 6631043057540825094, 6678709915819262982, 28383115]
#### springvibes users ##
#users = ['thelauracroft', 'aniisaalamx', 'prosperityroom', 'toddytoddytoddy',
#         'fashiongilly', 'allie.provost', 'dancemovesjoe', 'macearrrwindu',
#        'cluelessbushcraft', 'thtblasiangirl', 'motherinthemoon', 'shelbysfood',
#         'raidropcats', 'faceandyjenna', 'hope.cee', 'bob_herzog', 'fashionwith.anwen',
#         'fashionbyally', 'style', 'jociebasmr']

#### learnwithme users ##
'''users = ['glia', 'bigweirdworld', 'planetmoney', 'pbsnature', 'colethesciencedude',
        'historyfordummies', 'probemsolved', 'alexisnikole', 'songpsych', 'dailypaws',
        'mamitax5', 'sewprettystitcheshtx', 'marissadawnpleiness', 'sophiasmithgaler',
        'gsusserranomua', 'anisabenitez', 'rubytoblue', 'criiispateee', 'exploreorg',
        'hbrascend'] '''

#### happyeaster users ##
'''users = ['celenakinsey', 'mrsblinks', 'theyeeetbaby', 'wren.eleanor', '_hannahweir_',
         'happiedaze', 'jackiesfooddiary', 'madisyn_davis22', 'naptimecook'
         'whatisnewyorkofficial', 'colorcat.lettering', 'sulheejessica',
         'basic_indie_babe', 'brunchwithbabs', 'cartersmama24', 'vt', 'reannanblackmore',
         'jadenbarba', 'race_red_annie', 'zozoroe']
         '''

#### blankkiss users ##
'''users = ['caseycustoms', 'kcole0903', 'jayteedior', 'soul.xo', 'kernelthegreat',
         'bossman_._', 'valentina.mami', 'samantha.kitrell', 'melody00007',
         'magnuships', 'pjtenev', 'simplekillz', 'badasslashus', 'awakenedqueen',
         'ashleyelizabeth1989', 'princessprissypants82', 'dalenix13', 'aniyaraee']

'''

#practice trending users
'''users = ['Benny the Bull', 'Dude Perfect', 'Ryan Garcia', 'Logan Paul',
         'KingBach', 'TheProfessor', 'FallonTonight', 'Guinness World Records',
         'Ridiculousness', 'Cole Walliser', 'The Late Late Show', '6ix9ine',
         'Anwar Jibawi', 'gronk', 'Zach King', 'Ellen', 'AustReptilePark',
         'Kylie Cosmetics', 'Liza Koshy', 'JeremyLynch']
'''
#attempt 1 trending users
'''users = ['Shay Mitchell', 'Ryan Garcia', 'KingBach', 'Logan Paul', 'MTV', 'Guinness World Records',
         'Skai Jackson', 'Kylie Jenner', 'Benny the Bull', 'Anwar Jibawi', 'Liza Koshy', 'Kylie Cosmetics',
         'DAVID DOBRIK', 'Dunkin', 'Bradley Martyn', 'Gabriel Iglesias', 'James Charles', 'Zach King',
         'bretmanrock', 'Jordan Fisher']
'''

#attempt 3 trending users
users = ['Ivan', 'lala', 'Monkey keer', 'Lizastian' 'COSMO GUY', 'Madeyewlook',
         'stassiebaby', 'LISA+POPE', 'JOKES. NOT ADVICE 🤗', 'Eliana Ghen',
         'lil nas x', 'addison rae', 'Bella Poarch', 'The Rock', 'Savannah LaBrant',
         'AbbieHerbert', 'noah beck', 'Chupapi Muñañyo', 'Kylie Jenner', 'ESPN']

#attempt 2 trending users
'''users = ['Dude Perfect','Shay Mitchell', 'Ryan Garcia', 'KingBach', 'Logan Paul',
          'MTV', 'Guiness World Records', 'Skai Jackson', 'Anwar Jibawi', 'Kylie Jenner', 'Liza Koshy',
         'Kylie Cosmetics', 'Benny the Bull', 'DAVID DOBRIK', 'Dunkin',
         'James Charles', 'Bradley Martyn', 'bretmanrock', 'Zach King',
         'animalsdoingthings']
'''


#attempt 4 trending users
'''users = ['Dude Perfect', 'MTV', 'Ryan Garcia', 'KingBach', 'Logan Paul',
         'Shay Mitchell', 'Anwar Jibawi', 'Kylie Jenner', 'Liza Koshy',
         'Kylie Cosmetics', 'Benny the Bull', 'DAVID DOBRIK', 'Dunkin',
         'James Charles', 'Bradley Martyn', 'bretmanrock', 'Zach King',
         'The Wingrove’s', 'Jordan Fisher', 'Kira Kosarin']
'''

sum=0
min=0
max=0
for i in range(len(users)):
    user=api.search_for_users(users[i], count=1)[0]
    follow = user['stats']['followerCount']
    print(user['user']['uniqueId'] + " FOLLOWERS: " + str(follow))
    sum=sum+follow
    if i==0:
        min=follow
        max=follow
    elif follow < min:
        min=follow
    elif follow > max:
        max=follow

avg = sum / len(users)
print("Average fan: " + str(avg))
print("Max followers: " + str(max))
print("Min followers: " + str(min))

