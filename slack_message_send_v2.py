#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from slackclient import SlackClient

def slackmessage(msg,csatorna):
 slack_token = "####################################################" # Slack Api key
 sc = SlackClient(slack_token)
 sc.api_call(
  "chat.postMessage",
  channel=csatorna,					    # Slack channel
  username='Boldog SzülinAPPot',		# Slack display username
  icon_emoji=':wazehappy:',				# User icon
  text=msg
 )
