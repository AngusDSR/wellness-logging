import requests
import json

# Data points
# Total list of cards (excluding done, 1:1 D2P)
# of cards added
# number of cards moved to done

# Steps
# 1. Get list of lists
# 2. Drop excluded lists
# 3. For each remaining list
# 4. Get all cards and count them up per board

# 1. Get list of actions
# 2. Count number of new cards added (to which boards)
# 3. Count number added to 'Done'

# Get all cards:
# https://api.trello.com/1/boards/64afe3533900dcb5d46e09fe/cards?key=1bca705225f25d5ecdb83d7952ee2819&token=ATTA02a0bc5962b5038d4d6b659782dd7525206d41315d8541cc1722367a4794ef740DF8F49E

# List of lists:
# https://api.trello.com/1/boards/64afe3533900dcb5d46e09fe/lists?key=1bca705225f25d5ecdb83d7952ee2819&token=ATTA02a0bc5962b5038d4d6b659782dd7525206d41315d8541cc1722367a4794ef740DF8F49E

# Cards on {list}:
# https://api.trello.com/1/lists/{id}/cards?key=1bca705225f25d5ecdb83d7952ee2819&token=ATTA02a0bc5962b5038d4d6b659782dd7525206d41315d8541cc1722367a4794ef740DF8F49E

# Action on Done list:
# 'https://api.trello.com/1/lists/64afe8f419647521f5ea94aa/actions?key=1bca705225f25d5ecdb83d7952ee2819&token=ATTA02a0bc5962b5038d4d6b659782dd7525206d41315d8541cc1722367a4794ef740DF8F49E'
# "data": {
#     "listAfter": {
#       "id": "64afe8f419647521f5ea94aa",
#       "name": "Done 🎉"
#     }
# }

trello_key = '1bca705225f25d5ecdb83d7952ee2819'
trello_token = 'ATTA02a0bc5962b5038d4d6b659782dd7525206d41315d8541cc1722367a4794ef740DF8F49E'
trello_board_id = '64afe3533900dcb5d46e09fe'
trello_done_list_id = '64afe8f419647521f5ea94aa'

# FROM TRELLO DOCS
# headers = {
#   "Accept": "application/json"
# }

# query = {
#   'key': 'APIKey',
#   'token': 'APIToken'
# }

# response = requests.request(
#    "GET",
#    url,
#    headers=headers,
#    params=query
# )

