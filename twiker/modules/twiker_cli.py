# -*- coding: utf-8 -*-
"""

MIT License
Copyright (c) 2021 The Knight All rights reserved.
==========================

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""
import argparse
import configparser

from twiker.modules.engine import Engine


class CLI:
    """
    @author : Twiker team aka TheKnight
    This is the cli client for the Twitter bot you can manually run it to test the bot
    This will required the arguments:
        -config: the config file to use
        -tweet: the tweet to send
        -reply: the reply to send
        -follow: the user to follow
        -unfollow: the user to unfollow
        -like: the tweet to like
        -unlike: the tweet to unlike
        -retweet: the tweet to retweet

    You can control the bot with this cli version or you can use it as api to your bot

    This is the command line version



    """

    def __init__(self, engine):

        self.config = configparser.ConfigParser()
        engines = Engine("config.ini", verbose=False)
         
        self.bot = engines

        # # take arguments from the command line

        # """
        # Initializes the bot

        # Returns the arguments from the command line
        # - return None




        # """

        # self.parser = argparse.ArgumentParser(description="A cli client for managing twitter action and a Twitter Bot")

        # self.parser.add_argument("-t",
        #                          help="tweet a msg required -m", action="store_true")
        # self.parser.add_argument("-n", "--name",

        #                          help="name of the user", type=str, dest="name")
        # self.parser.add_argument("-m", "--message",

        #                          help="message to be used for dm,reply,tweet", type=str,
        #                          dest="message")
        # self.parser.add_argument("-i", "--image",

        #                          help="media link or path to be attached", type=str, dest="image")
        # self.parser.add_argument("-p", "--profile",

        #                          help="profile to be attached", type=str)
        # self.parser.add_argument("-c", "--config",

        #                          help="set config file or new config file", action="store_true")
        # self.parser.add_argument("-d", "--dm",

        #                          help="send a dm to a user", action="store_true")
        # # show tweet on console latest tweet
        # self.parser.add_argument("-s", "--show",

        #                          help="show latest tweet on console", action="store_true")
        # # list followers
        # self.parser.add_argument("-l", "--list",

        #                          help="list followers,following", type=str, dest="list")
        # # user
        # self.parser.add_argument("-u", "--user",
        #                          help="user for other action that required user", type=str, dest="user")
        # # show tweet on hash tag
        # self.parser.add_argument("-hg", "--hashtag",

        #                          help="show latest tweet on hash tag", type=str, dest="hashtag")
        # # like or retweet on a hash tag
        # self.parser.add_argument("-lk", "--like",

        #                          help="like a tweet", action="store_true")
        # self.parser.add_argument("-rt", "--retweet",
        #                          help="retweet a tweet", action="store_true")
        # self.parser.add_argument("-f", "--follow",
        #                          help="follow a user", action="store_true")
        # self.parser.add_argument("-uf", "--unfollow",
        #                          help="unfollow a user", action="store_true")
        # self.parser.add_argument("-r", "--search",
        #                          help="search for a user", type=str, dest="search")
        # self.parser.add_argument("-ra", "--retweet_all",
        #                          help="retweet all tweet on a hashtag or of a user required "
        #                               "hashtag or user",
        #                          action="store_true")
        # self.parser.add_argument("-la", "--like_all",
        #                          help="like all tweets on a hashtag or of a user required user or hashtag",
        #                          action="store_true")

        # args = self.parser.parse_args()
        # msg = args.message
        # name = args.name
        # list_type = args.list
        # image = args.image
        # profile = args.profile
        # hashtag = args.hashtag
        # user_search = args.search
        # user = args.user

        # if args.config:
        #     """
        #     if the -c flag is used, the config file is set to the new file
        #     else the config file will be read from the default location that is config.ini


        #     """
        #     # ask for consumer key
        #     c_key = input("Consumer Key: ")
        #     # ask for consumer secret
        #     c_secret = input("Consumer Secret: ")
        #     # ask for access token
        #     a_token = input("Access Token: ")
        #     # ask for access token secret
        #     a_secret = input("Access Token Secret: ")
        #     # ask for the name of the user
        #     name = input("Name of the user: ")

        #     self.config.add_section('Twitter')
        #     self.config.set('twitter', 'consumer_key', str(c_key))
        #     self.config.set('twitter', 'consumer_secret', str(c_secret))
        #     self.config.set('twitter', 'access_token', str(a_token))
        #     self.config.set('twitter', 'access_token_secret', str(a_secret))

        #     with open('config.ini', 'w') as configfile:
        #         self.config.write(configfile)
        #     exit()

        # elif args.tweet:
        #     """
        #     tweet a message


        #     """
        #     if not msg:
        #         msg = input("Message: ")
        #     try:
        #         self.bot.tweet(msg, media=image)
        #     except Exception as e:
        #         print(e)
        #     exit()


        # elif args.dm:
        #     """
        #     send a dm to a user

        #     """
        #     if not user and not msg:
        #         user = input("User: ")
        #         msg = input("Message: ")
        #     self.bot.send_dm(user, msg)
        #     exit()


        # elif list_type:
        #     """
        #     list followers,following



        #     """
        #     if list_type == "followers":
        #         self.bot.get_followers()
        #     elif list_type == "following":
        #         self.bot.get_following()
        #     else:
        #         print("Invalid list type")
        #     exit()

        # elif args.show:
        #     """
        #     show latest tweet on console

        #     """
        #     if hashtag:
        #         self.bot.get_hashtag_tweets(hashtag)
            
        #     self.bot.get_tweets(count=1000)
        #     exit()

        # elif args.like_all:
        #     """
        #     like a tweet

        #     """
        #     if hashtag:
        #         self.bot.like_all_tweets_on_hashtag(hashtag)
        #     elif user:
        #         self.bot.like_all_tweets(user)
        #     else:
        #         print("Invalid user or hashtag")
        #     self.bot.like_hashtag(hashtag)
        #     exit()


        # elif args.retweet:
        #     """
        #     retweet a tweet

        #     """
        #     if hashtag:
        #         self.bot.retweet_all_tweets(hashtag)
        #     elif user:
        #         self.bot.retweet_all_tweets(user)
        #     else:
        #         print("Invalid user or hashtag")
        #     exit()

        # elif args.follow:
        #     """
        #     follow a user

        #     """
        #     if hashtag:
        #         self.bot.follow_all_users(hashtag)
        #     self.bot.follow(name)
        #     exit()

        # elif args.unfollow:
        #     """
        #     unfollow a user

        #     """
        #     self.bot.unfollow(name)
        #     exit()


        # elif user_search:

        #     """
        #     search for a user

        #     """
        #     try:
        #         try:
        #             self.bot.get_user__(user_search)
        #         except Exception as e:

        #             self.bot.search_user(user_search)

        #         print("User found")

        #     except Exception as e:
        #         print(e)

        #     exit()

        # elif args.retweet_all:
        #     """
        #     retweet all tweet on a hashtag or of a user required hashtag or user

        #     """
        #     if hashtag:
        #         self.bot.retweet_on_hashtag(hashtag)
        #     elif user:
        #         self.bot.retweet_all(username=user)
        #     else:
        #         print("Invalid arguments")
        #     exit()

        # elif args.like_all:
        #     """
        #     like all tweets on a hashtag or of a user required user or hashtag

        #     """
        #     if hashtag:
        #         self.bot.like_hashtag(hashtag)
        #     elif user:
        #         self.bot.like_all(username=user)
        #     else:
        #         print("Invalid arguments")
        #     exit()

    def init__cli(self):
        """
        init the client

        """
        self.parser = argparse.ArgumentParser(description="A cli client for managing twitter action and a Twitter Bot")

        self.parser.add_argument("-t","--tweet",
                                 help="tweet a msg required -m", action="store_true")
        self.parser.add_argument("-n", "--name",

                                 help="name of the user", type=str, dest="name")
        self.parser.add_argument("-m", "--message",

                                 help="message to be used for dm,reply,tweet", type=str,
                                 dest="message")
        self.parser.add_argument("-i", "--image",

                                 help="media link or path to be attached", type=str, dest="image")
        self.parser.add_argument("-p", "--profile",

                                 help="profile to be attached", type=str)
        self.parser.add_argument("-c", "--config",

                                 help="set config file or new config file", action="store_true")
        self.parser.add_argument("-d", "--dm",

                                 help="send a dm to a user", action="store_true")
        # show tweet on console latest tweet
        self.parser.add_argument("-s", "--show",

                                 help="show latest tweet on console", action="store_true")
        # list followers
        self.parser.add_argument("-l", "--list",

                                 help="list followers,following", type=str, dest="list")
        # user
        self.parser.add_argument("-u", "--user",
                                 help="user for other action that required user", type=str, dest="user")
        # show tweet on hash tag
        self.parser.add_argument("-hg", "--hashtag",

                                 help="show latest tweet on hash tag", type=str, dest="hashtag")
        # like or retweet on a hash tag
        self.parser.add_argument("-lk", "--like",

                                 help="like a tweet", action="store_true")
        self.parser.add_argument("-rt", "--retweet",
                                 help="retweet a tweet", action="store_true")
        self.parser.add_argument("-f", "--follow",
                                 help="follow a user", action="store_true")
        self.parser.add_argument("-uf", "--unfollow",
                                 help="unfollow a user", action="store_true")
        self.parser.add_argument("-r", "--search",
                                 help="search for a user", type=str, dest="search")
        self.parser.add_argument("-ra", "--retweet_all",
                                 help="retweet all tweet on a hashtag or of a user required "
                                      "hashtag or user",
                                 action="store_true")
        self.parser.add_argument("-la", "--like_all",
                                 help="like all tweets on a hashtag or of a user required user or hashtag",
                                 action="store_true")

        args = self.parser.parse_args()
        msg = args.message
        name = args.name
        list_type = args.list
        image = args.image
        profile = args.profile
        hashtag = args.hashtag
        user_search = args.search
        user = args.user

        if args.config:
            """
            if the -c flag is used, the config file is set to the new file
            else the config file will be read from the default location that is config.ini


            """
            # ask for consumer key
            c_key = input("Consumer Key: ")
            # ask for consumer secret
            c_secret = input("Consumer Secret: ")
            # ask for access token
            a_token = input("Access Token: ")
            # ask for access token secret
            a_secret = input("Access Token Secret: ")
            # ask for the name of the user
            name = input("Name of the user: ")

            self.config.add_section('Twitter')
            self.config.set('twitter', 'consumer_key', str(c_key))
            self.config.set('twitter', 'consumer_secret', str(c_secret))
            self.config.set('twitter', 'access_token', str(a_token))
            self.config.set('twitter', 'access_token_secret', str(a_secret))

            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
            exit()

        elif args.tweet:
            """
            tweet a message


            """
            if not msg:
                msg = input("Message: ")
            try:
                self.bot.tweet(msg, media=image)
            except Exception as e:
                print(e)
            exit()


        elif args.dm:
            """
            send a dm to a user

            """
            if not user and not msg:
                user = input("User: ")
                msg = input("Message: ")
            self.bot.send_dm(user, msg)
            exit()


        elif list_type:
            """
            list followers,following



            """
            if list_type == "followers":
                self.bot.get_followers()
            elif list_type == "following":
                self.bot.get_following()
            else:
                print("Invalid list type")
            exit()

        elif args.show:
            """
            show latest tweet on console

            """
            if hashtag:
                self.bot.get_hashtag_tweets(hashtag)
            
            self.bot.get_tweets(count=1000)
            exit()

        elif args.like_all:
            """
            like a tweet

            """
            if hashtag:
                self.bot.like_all_tweets_on_hashtag(hashtag)
            elif user:
                self.bot.like_all_tweets(user)
            else:
                print("Invalid user or hashtag")
            self.bot.like_hashtag(hashtag)
            exit()


        elif args.retweet:
            """
            retweet a tweet

            """
            if hashtag:
                self.bot.retweet_all_tweets(hashtag)
            elif user:
                self.bot.retweet_all_tweets(user)
            else:
                print("Invalid user or hashtag")
            exit()

        elif args.follow:
            """
            follow a user

            """
            if hashtag:
                self.bot.follow_all_users(hashtag)
            self.bot.follow(name)
            exit()

        elif args.unfollow:
            """
            unfollow a user

            """
            self.bot.unfollow(name)
            exit()


        elif user_search:

            """
            search for a user

            """
            try:
                try:
                    self.bot.get_user__(user_search)
                except Exception as e:

                    self.bot.search_user(user_search)

                print("User found")

            except Exception as e:
                print(e)

            exit()

        elif args.retweet_all:
            """
            retweet all tweet on a hashtag or of a user required hashtag or user

            """
            if hashtag:
                self.bot.retweet_on_hashtag(hashtag)
            elif user:
                self.bot.retweet_all(username=user)
            else:
                print("Invalid arguments")
            exit()

        elif args.like_all:
            """
            like all tweets on a hashtag or of a user required user or hashtag

            """
            if hashtag:
                self.bot.like_hashtag(hashtag)
            elif user:
                self.bot.like_all(username=user)
            else:
                print("Invalid arguments")
            exit()



# write to the config file


# get_args()

# c = read_config('config.ini',Section='Twitter',Content='__CONSUMER_KEY__')
# print(c)
