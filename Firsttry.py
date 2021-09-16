#!/usr/bin/python
# -*- coding: utf-8-*-

from pyrogram import Client, MessageHandler, Filters
from numpy.random import randint
import re
import time
import os

api_id = int(os.environ.get("APP_ID"))
api_hash = str(os.environ.get("API_HASH"))

app=Client(str(round(time.time() * 1000))+str(randint(1,10000)), api_id, api_hash)
app.start()
print(app.export_session_string())
app.stop()
