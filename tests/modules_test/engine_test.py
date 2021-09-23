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

from time import time
from twiker.modules.engine import Engine
from twiker.modules.tauth import Auth

engine = Engine("config.ini", verbose=False)

# engine.reply_hashtag("hello from twiker","KD001") # test reply_hashtag success
# engine.tweet("Hello I am back and alive") # test retweet_hashtag success
# engine.user_info("codacy") # test user_info success
# users = ["JANTV2012","parigivinod"]
# for i in range(100):
#     engine.dm("iamSRKsYoddha1", "I'm testing my self haha it's all automated haha") 
#     if i==10:
#         time.sleep(10)

# engine.dm_hashtag("Sony","How are you sir?")
# engine.like_hashtag("wednesdaythought")
# engine.follow_hashtag("wednesdaythought")
# engine.unfollow_hashtag("wednesdaythought")
# engine.like_hashtag("Twitter")
# engine.follow_followers()
# engine.follow_keyword("Python",count=10)

# engine.search_user("gen_aksh")

# engine.get_hashtag_tweets("python")

# engine.get_following()
# engine.get_messages(count=1000)
