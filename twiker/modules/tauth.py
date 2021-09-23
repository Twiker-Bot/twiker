"""
MIT License
Copyright (c) 2021 The Knight All rights reserved.
==========================
       twiker authuntication module
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

import configparser
import logging

import tweepy as tp


class Auth:
    """
    This is the API class for the Twitter Bot.
    :param self:
    :return:
    """

    def __init__(self, config_file):

        self.config_file = config_file

        """
        This is the init function for the API class.

        return the object of a Twitter API call."""

        self.__CONSUMER_KEY__ = self.read_config("cred", 'consumer_key')

        """This is the consumer key for the twitter app"""

        self.__CONSUMER_SECRET__ = self.read_config("cred", 'consumer_secret')

        """This is the consumer secret for the twitter app"""

        self.__ACCESS_TOKEN__ = self.read_config("cred", 'access_token')

        """This is the access token for the twitter app"""

        self.__ACCESS_SECRET__ = self.read_config("cred", 'access_secret')

        """This is the access secret for the twitter app"""

    def file_exists(self, file_path):
        """
        Checks if the file exists
        :return:
        :rtype: object
        :param file_path: path of the file
        :return
        """
        try:
            with open(file_path) as f:
                print("File exist")
                return True
        except IOError:
            return False

    def read_config(self, *args):
        """
        Reads the config file and returns the value of the requested content
        possible args:
        
        :configfile: config file to read
        :section: section of the config file
        :content: content of the config file
        :return:
        example:
            config = read_config('Twitter','__consumer_key__')
        
        """
        config = configparser.ConfigParser()
        config.read(str(self.config_file))
        print(str(self.config_file))
        keys = ['consumer_key', 'consumer_secret', 'access_token', 'access_secret']
        print(args[0], args[1])
        if args[1] in keys:
            try:
                print(args[0], args[1])

                data = config.get(args[0], args[1])
                print(data)
                return data
            except configparser.NoSectionError as e:
                logging.error("Config file can't be read")
                logging.error("Please check the config file")
                print("1")
                logging.error(e.message)


        else:
            try:
                data = config.get(args[0], args[1])
                return data
            except configparser.NoOptionError as e:
                logging.error("Config file can't be read")
                logging.error("Please check the config file")
                logging.error(e.message)

    def get_config_file(self, file_path=None):
        """
        Returns the config file
        :param file_path:
        :param self:
        :return


        """

        if self.file_exists(file_path):
            print("File exist")
            config_file = file_path
        else:
            config_file = "twiker/data/config.ini"

        return config_file

    def access(self):
        """
        This is the auth function for the API class.
        it will give the access to the twitter API.
        :param self:



        """
        auth = tp.OAuthHandler(self.__CONSUMER_KEY__, self.__CONSUMER_SECRET__)
        auth.set_access_token(self.__ACCESS_TOKEN__, self.__ACCESS_SECRET__)
        logging.info("Authentication successful")

        # print(self.__ACCESS_TOKEN__)
        # print(self.__CONSUMER_KEY__)
        # print(self.__ACCESS_SECRET__)
        # print(self.__CONSUMER_SECRET__)
        api = tp.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
        return api
