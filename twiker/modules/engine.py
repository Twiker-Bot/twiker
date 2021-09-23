"""
MIT License
Copyright (c) 2021 The Knight All rights reserved.
==========================
	twiker Engine

    
	This file is part of the Twiker Bot library.
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
from __future__ import unicode_literals

import datetime
import logging
import os

import tweepy as tp

from twiker.modules.tauth import Auth


class Engine(object):
    """
        The main engine class for the Twiker Bot.This class includes all the api methods

        Copyright (c) 2021 The Knight All rights reserved.


        """

    def __init__(self, config, verbose=False):
        auth = Auth(config)
        # configure logging
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        # every log file will be named with the current date and would be name differently
        date = str(datetime.datetime.now().strftime("%Y-%m-%d"))
        time = str(datetime.datetime.now().strftime("%H-%M-%S"))
        log_file = os.path.join(log_dir, "twiker_bot_" + date + "_" + time + ".log")
        if auth.file_exists(log_file):
            log_file = os.path.join(log_dir, "twiker_bot_" + date + "_" + time + ".log")

        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename=log_file,
                            filemode='w')
        self.logger = logging.getLogger()
        if verbose:
            self.logger.setLevel(logging.DEBUG)
        else:
            self.logger.setLevel(logging.INFO)
        self.logger.info("Starting Twiker Bot")

        self.api = auth.access()

    # print all information about a user
    def user_info(self, username=None):
        """
        Get User info by username
        :param username: username to get info on twitter
        :return:

        """
        if username is None:
            username = self.api.me().screen_name

        try:
            info = self.api.get_user(screen_name=username)
            print("Name: " + str(info.name))
            print("Screen Name: " + str(info.screen_name))
            print("User ID: " + str(info.id))
            print("Location: " + str(info.location))
            print("Description: " + str(info.description))
            print("URL: " + str(info.url))
            print("Followers: " + str(info.followers_count))
            print("Following: " + str(info.friends_count))
            print("Tweets: " + str(info.statuses_count))
            print("Favorites: " + str(info.favourites_count))
            print("Created at: " + str(info.created_at))
            print("Time zone: " + str(info.time_zone))
            print("Geo enabled: " + str(info.geo_enabled))
            print("Verified: " + str(info.verified))
            print("Lang: " + str(info.lang))
            try:
                print("Status: " + str(info.status.text))
            except:
                print("Status: " + "None")

            print("Profile background color: " + str(info.profile_background_color))
            print("Profile background image: " + str(info.profile_background_image_url))
            print("Profile background image url: " + str(info.profile_background_image_url_https))
            print("Profile background tile: " + str(info.profile_background_tile))
            print("Profile link color: " + str(info.profile_link_color))
            print("Profile sidebar border color: " + str(info.profile_sidebar_border_color))
            print("Profile sidebar fill color: " + str(info.profile_sidebar_fill_color))
            print("Profile text color: " + str(info.profile_text_color))
            print("Profile use background image: " + str(info.profile_use_background_image))
            print("Profile image: " + str(info.profile_image_url))
            print("Profile image url: " + str(info.profile_image_url_https))
            print("Profile image url: " + str(info.profile_background_image_url_https))
            print("Profile image url: " + str(info.profile_background_image_url))


        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # tweet a message
    def tweet(self, message, media=None):
        """
        Tweet a message
        :param message: message to tweet
        :param media: media to tweet
        :return:
        
        
        """
        self.logger.debug("Tweeting message: %s", message)
        self.logger.info("Tweeting message: %s", message)
        try:
            if media is None:

                self.api.update_status(status=message)
            else:
                self.api.update_with_media(media, status=message)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # get user timeline
    def get_timeline(self, username):
        """
        Get user timeline
        :param username: username to get timeline
        :return:

        """

    def retweet(self, tweet_id):
        """
        Retweet a tweet by tweet.id
        :param tweet_id: tweet id to retweet a tweet
        :return:
        """
        self.logger.debug("Retweeting tweet with id: %s", tweet_id)
        try:
            self.api.retweet(tweet_id)
        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    def reply(self, message, tweet_id):
        """
        Reply to a tweet by tweet.id
        :param message: message to reply
        :param tweet_id: tweet id to reply
        :return:
        
        
        
        """
        try:
            self.api.update_status(status=message,
                                   in_reply_to_status_id=tweet_id,
                                   auto_populate_reply_metadata=True)
            logging.debug("Replied to tweet with id: %s", tweet_id)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    def follow(self, username):
        """
        Follow a user on twitter
        :param username: username to follow on twitter
        :return:


        
        
        """
        try:
            self.api.create_friendship(screen_name=username)
            logging.debug("Followed user: %s", username)
        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    def unfollow(self, username):
        """
        Unfollow a user on twitter
        :param username: username to unfollow on twitter
        :return:

        """

        try:
            self.api.destroy_friendship(screen_name=username)
            logging.debug("Unfollowed user: %s", username)
        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    def block(self, username):
        """
        Block a user on twitter
        :param username: username to block on twitter
        :return:

        
        """
        try:
            self.api.create_block(screen_name=username)
            logging.debug("Blocked user: %s", username)
        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    def unblock(self, username):
        """
        Unblock a user on twitter
        :param username: username to unblock on twitter
        :return:

        
        """
        try:
            self.api.destroy_block(screen_name=username)
            logging.debug("Unblocked user: %s", username)
        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    def get_user_id(self, username):
        """
        Get User id by username
        :param username: username to get id on twitter
        """

        try:
            return self.api.get_user(screen_name=username).user_id
        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # reply on a hashtag
    def reply_hashtag(self, message, hashtag):
        """
        Reply to all tweet on a hashtag
        :param message: message to in reply with hashtag
        :param hashtag: hashtag on which method have to reply
        :return:
        
        """
        try:

            for tweet_id in tp.Cursor(self.api.search, q=hashtag).items():
                self.reply(message, tweet_id.id)
                logging.debug("Replied to tweet on hashtag: %s tweet_id: %s", hashtag, tweet_id.id)


        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # retweet on a hashtag
    def retweet_hashtag(self, hashtag):
        """
        Retweet all tweet on a hashtag
        :param hashtag: hashtag on which method have to retweet
        :return:
        
        """
        try:
            for tweet_id in tp.Cursor(self.api.search, q=hashtag).items():
                self.retweet(tweet_id.id)
                logging.debug("Retweeted tweet on hashtag: %s tweet_id: %s", hashtag, tweet_id.id)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    def unretweet_hashtag(self, hashtag):
        """
        Unretweet all tweet on a hashtag
        :param hashtag: hashtag on which method have to unretweet
        :return:
        
        """
        try:
            for tweet_id in tp.Cursor(self.api.search, q=hashtag).items():
                self.unretweet(tweet_id.id)
                logging.debug("Unretweeted tweet on hashtag: %s tweet_id: %s", hashtag, tweet_id.id)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # like all tweet on a hashtag
    def like_hashtag(self, hashtag):
        """
        Like all tweet on a hashtag
        :param hashtag: hashtag on which method have to like
        :return:
        
        """
        try:
            for tweet_id in tp.Cursor(self.api.search, q=hashtag).items():
                try:
                    self.api.create_favorite(tweet_id.id)
                except Exception as e:
                    logging.error("Error: %s", e)
                    print(e)

                logging.debug("Liked tweet on hashtag: %s tweet_id: %s", hashtag, tweet_id.id)
                logging.info("Liked tweet on hashtag: %s tweet_id: %s", hashtag, tweet_id.id)


        except tp.TweepError as e:
            logging.error("Error: %s", e)

            print(e)

    def unlike_hashtag(self, hashtag):
        """
        Unlike all tweet on a hashtag
        :param hashtag: hashtag on which method have to unlike
        :return:
        
        """
        try:
            for tweet_id in tp.Cursor(self.api.search, q=hashtag).items():
                self.api.destroy_favorite(tweet_id.id)
                logging.debug("Unliked tweet on hashtag: %s tweet_id: %s", hashtag, tweet_id.id)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # follow all user on a hashtag
    def follow_hashtag(self, hashtag):
        """
        Follow all user on a hashtag
        :param hashtag: hashtag on which method have to follow
        :return:
        
        """
        try:
            for tweet_id in tp.Cursor(self.api.search, q=hashtag).items():
                self.follow(tweet_id.user.screen_name)
                logging.debug("Followed user: %s", tweet_id.user.screen_name)
                logging.info("Followed user: %s", tweet_id.user.screen_name)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    def unfollow_hashtag(self, hashtag):
        """
        Unfollow all user on a hashtag
        :param hashtag: hashtag on which method have to unfollow
        :return:
        
        """
        try:
            for tweet_id in tp.Cursor(self.api.search, q=hashtag).items():
                self.unfollow(tweet_id.user.screen_name)
                logging.debug("Unfollowed user: %s", tweet_id.user.screen_name)
                logging.info("Unfollowed user: %s", tweet_id.user.screen_name)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # like all tweet of a user
    def like_user(self, username):
        """
        Like all tweet of a user
        :param username: username on which method have to like
        :return:
        
        """
        try:
            for tweet_id in tp.Cursor(self.api.user_timeline, screen_name=username).items():
                self.api.create_favorite(tweet_id.id)
                logging.debug("Liked tweet of user: %s tweet_id: %s", username, tweet_id.id)
                logging.info("Liked tweet of user: %s tweet_id: %s", username, tweet_id.id)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # unlike all tweet of a user
    def unlike_user(self, username):
        """
        Unlike all tweet of a user
        :param username: username on which method have to unlike
        :return:
        
        """
        try:
            for tweet_id in tp.Cursor(self.api.user_timeline, screen_name=username).items():
                self.api.destroy_favorite(tweet_id.id)
                logging.debug("Unliked tweet of user: %s tweet_id: %s", username, tweet_id.id)
                logging.info("Unliked tweet of user: %s tweet_id: %s", username, tweet_id.id)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # retweet all tweet of a user
    def retweet_user(self, username):
        """
        Retweet all tweet of a user
        :param username: username on which method have to retweet
        :return:
        
        """
        try:
            for tweet_id in tp.Cursor(self.api.user_timeline, screen_name=username).items():
                self.api.retweet(tweet_id.id)
                logging.debug("Retweeted tweet of user: %s tweet_id: %s", username, tweet_id.id)
                logging.info("Retweeted tweet of user: %s tweet_id: %s", username, tweet_id.id)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # dm to single user
    def dm(self, username, message, media=None):
        """
        Direct message to single user
        :param username: username on which method have to dm
        :param message: message to dm
        :param media: media to dm
        :return:
        
        """
        try:
            recipient = self.api.get_user(username)
            self.api.send_direct_message(recipient_id=recipient.id_str, text=message)
            logging.debug("Direct message to user sent: %s", recipient.screen_name)
            logging.info("Direct message to user sent: %s", recipient.screen_name)
            if media:
                self.api.media_upload(media)
                self.api.send_direct_message(recipient_id=recipient.id_str, text=message, attachment_type="media",
                                             attachment_media_id=self.api.media_upload(media).media_id)

                logging.debug("Direct message to user with media sent: %s", recipient.screen_name)
                logging.info("Direct message to user with media sent: %s", recipient.screen_name)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # dm to multiple user
    def dm_multiple(self, usernames, message, media=None):
        """
        Direct message to multiple user
        :param usernames: list(usernames) on which method have to dm ["username1", "username2", ...]
        :param message: message to dm
        :return:
        
        """
        try:
            for user in usernames:
                recipient = self.api.get_user(user)
                try:

                    self.api.send_direct_message(recipient_id=recipient.id, text=message)
                    logging.debug("Direct message to user sent: %s", recipient.screen_name)
                    logging.info("Direct message to user sent: %s", recipient.screen_name)
                except Exception as e:
                    logging.error("Error: %s", e)
                    print(e)
                if media:
                    try:

                        self.api.media_upload(media)
                        self.api.send_direct_message(recipient_id=recipient.id_str, text=message,
                                                     attachment_type="media",
                                                     attachment_media_id=self.api.media_upload(media).media_id)
                    except Exception as e:
                        logging.error("Error: %s", e)
                        print(e)

                    logging.debug("Direct message to user with media sent: %s", recipient.screen_name)
                    logging.info("Direct message to user with media sent: %s", recipient.screen_name)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # dm all user of a hashtag
    def dm_hashtag(self, hashtag, message, media=None):
        """
        Direct message to all user of a hashtag
        :param hashtag: hashtag on which method have to dm
        :param message: message to dm
        :return:
        
        """
        try:

            for tweet_id in tp.Cursor(self.api.search, q=hashtag).items():
                recipient = self.api.get_user(tweet_id.user.screen_name)
                # 
                # check if user is protected or dm is disabled
                users = []
                if not recipient.protected:
                    users.append(recipient.id)

                for user in users:
                    try:
                        self.api.send_direct_message(recipient_id=user, text=message)
                    except Exception as e:
                        logging.error("Error: %s", e)
                        print(e)

                    logging.debug("Direct message to user sent: %s", recipient.screen_name)
                    logging.info("Direct message to user sent: %s", recipient.screen_name)
                    print(recipient.screen_name)
                    if media:
                        try:

                            self.api.media_upload(media)
                            self.api.send_direct_message(recipient_id=user, text=message, attachment_type="media",
                                                         attachment_media_id=self.api.media_upload(media).media_id)
                        except Exception as e:
                            logging.error("Error: %s", e)
                            print(e)

                        logging.debug("Direct message to user with media sent: %s", recipient.screen_name)
                        logging.info("Direct message to user with media sent: %s", recipient.screen_name)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    def update_profile(self, *args):
        """
        Update profile
        possible args:
        name, url, location, description, profile_link_color, include_entities, skip_status
        :param args:

       
        :return:
        
        """
        try:
            self.api.update_profile(*args)
            logging.debug("Profile updated")
            logging.info("Profile updated")

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # follow all followers who have followed you
    def follow_followers(self):
        """
        Follow all followers who have followed you
        :return:
        
        """
        try:
            for follower in tp.Cursor(self.api.followers).items():
                if not follower.following:
                    follower.follow()
                    logging.debug("Followed: %s", follower.screen_name)
                    logging.info("Followed: %s", follower.screen_name)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # unfollow all followers who have followed you
    def unfollow_followers(self):
        """
        Unfollow all followers who have followed you
        :return:
        
        """
        try:
            for follower in tp.Cursor(self.api.followers).items():
                if follower.following:
                    follower.unfollow()
                    logging.debug("Unfollowed: %s", follower.screen_name)
                    logging.info("Unfollowed: %s", follower.screen_name)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # follow users with a keyword
    def follow_keyword(self, keyword, count=1):
        """
        Follow users with a keyword
        :param keyword: keyword to search
        :param count: number of users to follow
        :return:
        
        """
        try:
            for tweet in tp.Cursor(self.api.search, q=keyword).items(count):
                if not tweet.user.following:
                    tweet.user.follow()
                    logging.debug("Followed: %s", tweet.user.screen_name)
                    logging.info("Followed: %s", tweet.user.screen_name)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # get latest tweets from twitter
    def get_tweets(self, count=1):
        """
        Get latest tweets from twitter
        :param count: number of tweets to get
        :return:
        
        """
        try:
            for tweet in tp.Cursor(self.api.home_timeline).items(count):
                print("Tweet: %s" % tweet.text)
                print("User: %s" % tweet.user.screen_name)
                print("User id: %s" % tweet.user.id)
                print("Date: %s" % tweet.created_at)
                logging.debug("Tweet: Feched")

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # get all followers of a user
    def get_followers(self, username=None):
        """
        Get all followers of a user 
        Note: twitter api only have limit of of fetching limited requests at a time
        :param username: username of user
        :param count: number of followers to get
        :return:
        
        """
        if username is None:
            username = self.api.me().screen_name
        try:
            count = 1

            for follower in tp.Cursor(self.api.followers, screen_name=username).items():
                # get total followers
                print("Follower: %s" % follower.screen_name)
                print("Follower Count: %s" % count)
                print("Follower id: %s" % follower.id)
                print("Follower date: %s" % follower.created_at)
                count += 1
    
        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)



    def get_following(self, username=None):
        """
        Get all following of a user
        Note: twitter api only have limit of of fetching limited requests at a time
        :param username: username of user


        """
        if username is None:
            username = self.api.me().screen_name
        try:
            count = 1

            for follower in tp.Cursor(self.api.friends, screen_name=username).items():
                # get total followers
                print("Following: %s" % follower.screen_name)
                print("Following Count: %s" % count)
                print("Following id: %s" % follower.id)
                print("Following date: %s" % follower.created_at)
                count += 1


        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    def search_user(self, username):
        """
        Search a user on twitter by username
        :param username: username to search
        :return:
        """
        try:
            self.user_info(username=username)
            logging.debug("User searched: %s", username)
            logging.info("User searched: %s", username)

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    # get random user and return username
    def get_random_user(self, *args, count=1):
        """
        Get random user
        :param args:
        pssible args:
        keyword
        :param count: number of users to get

        :return: username
        
        """
        try:
            # get random user
            for tweet in tp.Cursor(self.api.search, q=args).items(count):
                return tweet.user.screen_name


        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)


    def get_hashtag_tweets(self, hashtag):
        """
        Get tweets by hashtag
        :param hashtag: hashtag to search
        :return:
        
        """
        try:
            for tweet in tp.Cursor(self.api.search, q=hashtag).items():
                print("Tweet: %s" % tweet.text)
                print("User: %s" % tweet.user.screen_name)
                print("User id: %s" % tweet.user.id)
                print("Date: %s" % tweet.created_at)
                logging.debug("Tweet: Feched")

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)


    # get all direct messages
    def get_messages(self, count=1):
        """
        Get all direct messages
        :param count: number of messages to get
        :return:
        
        """
        try:
            message = self.api.list_direct_messages(count=count)
            for msg in reversed(message):
                sender = msg.message_create['sender_id']
                recipient = msg.message_create['target']['recipient_id']
                sender_name = self.api.get_user(sender).screen_name
                recipient_name = self.api.get_user(recipient).screen_name
                print("Sender: %s" % sender)
                print("Sender name: %s" % sender_name)
                print("Recipient: %s" % recipient)
                print("Recipient name: %s" % recipient_name)
                print("Message: %s" % msg.message_create['message_data']['text'])
            

        except tp.TweepError as e:
            logging.error("Error: %s", e)
            print(e)

    

    # 