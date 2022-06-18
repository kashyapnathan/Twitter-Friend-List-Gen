import os
import tweepy
from os.path import join, dirname
from dotenv import load_dotenv
from tweepy import API, Cursor, OAuthHandler

# maximum amount of members you can add to a Twitter list according to Twitter's add_list_members() API call.
# See documentation here: https://developer.twitter.com/en/docs/twitter-api/v1/accounts-and-users/create-manage-lists/api-reference/post-lists-members-create_all
MAX_MEMBER_ADD = 100

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Welcome message
print("\nWelcome to the Twitter List Frinds Generation Script! In order to proceed, we need a few things from you.\n")

# Prompt user for their keys and retry if authentication invalid
while True:

    API_KEY = input("What's your API Key?\n\n")
    API_KEY_SECRET = input("\nWhat's your API Key Secret?\n\n")
    ACCESS_TOKEN = input("\nWhat's your Access Token?\n\n")
    ACCESS_SECRET_TOKEN = input("\nWhat's your Access Token Secret?\n\n")

    # Authenticate to Twitter
    auth = OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET_TOKEN)

    # See https://docs.tweepy.org/en/stable/api.html#api-reference for details on wait_on_rate_limit parameter
    api = API(auth, wait_on_rate_limit=True)

    # test authentication
    try:
        api.verify_credentials()
        print("\nAuthentication Success!\n")
        break
    except:
        print("\nError during authentication.\n")

try:
    # get friends of user (people who users follow)

    # get desired user
    screen_name = input("Which user would you like to get followers for?\n\n")

    # ask for mode
    while True:
        mode = input("\nWould you like to make this list public or private? Making your list public will notify the users you add.\n\n")

        if mode.lower() == "private":
            mode = mode.lower()
            break
        elif mode.lower() == "public":
            mode = mode.lower()
            break
        else:
            print("\nPlease enter a valid input: \'public\' or \'private\'.")
            continue

    # ask for description
    while True:
        description_checker = input("\nDo you have a description for this list? Please type \'yes\' or \'no\'.\n\n")

        if description_checker.lower() == "yes":
            description = input("Please enter your description here: ")
            break
        elif description_checker.lower() == "no":
            description = None
            break
        else:
            print("\nPlease enter a valid input: \'yes\' or \'no\'.")
            continue


    print("\nProcessing...\n")

    friend_ids = []
    for friend_id in Cursor(api.get_friend_ids, screen_name=screen_name).items():
        friend_ids.append(friend_id)

    # create twitter list
    twitter_list_name = screen_name + " Twitter List"

    # if a description exists, then add to to list along with its mode
    if description:
        twitter_list_object = api.create_list(name=twitter_list_name, mode=mode, description=description)
    else:
        twitter_list_object = api.create_list(name=twitter_list_name, mode=mode)

    twitter_list_id = twitter_list_object.id

    # add all friends to twitter list, by the 100s
    for i in range(0, len(friend_ids), MAX_MEMBER_ADD):
        list = api.add_list_members(list_id=twitter_list_id, user_id=friend_ids[i:i + MAX_MEMBER_ADD])

    # For logging
    print("Name of the list : " + twitter_list_object.name)
    print("Mode of the list : " + twitter_list_object.mode)
    print("ID of the List : " + str(twitter_list_object.id))
    print("Number of members in the list : " + str(api.get_list(list_id=twitter_list_id).member_count))

except Exception as e:
    print(e)
    print("\nInput invalid! Please try again.\n\n")

finally:
    pass

    # For debugging purposes — if you need to run the script multiple times, this destroys the list to avoid manual removal
    # api.destroy_list(list_id=twitter_list_id)