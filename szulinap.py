#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import datetime
import sys
import lekerdezesek
import slack_message_send_v2

reload(sys)
sys.setdefaultencoding('utf8')

if lekerdezesek.szulinap() != "0":
	uzenet = ("Boldog Szülinapot kívánunk <@" + lekerdezesek.szulinap() + "> :tada: :birthday:")
	slack_message_send_v2.slackmessage(uzenet,"#off-line")

lekerdezesek.lefutottmost()
