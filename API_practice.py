# Set up a template with basic use cases for APIs
import json
import requests

# Special thanks to R6Tab for their unofficial Rainbow Six Siege API
# https://github.com/Tabwire/R6Tab-API


api_token = 'your_api_token' # Not needed for R6tab
api_url_base = 'https://r6tab.com/api/search.php?platform=uplay&search='

headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

def get_player_info(player_name):
    """ Get a specified player's name """

    api_url = api_url_base + player_name

    response = requests.get(api_url, headers=headers)

    if response.status_code >= 500:
        print('[!] [{0}] Server Error'.format(response.status_code))
        return None
    elif response.status_code == 404:
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code,api_url))
        return None
    elif response.status_code == 401:
        print('[!] [{0}] Authentication Failed'.format(response.status_code))
        return None
    elif response.status_code >= 300:
        print('[!] [{0}] Unexpected Redirect'.format(response.status_code))
        return None
    elif response.status_code == 200:
        return json.loads(response.content)
    else:
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code,response.content))
    return None


player_info = get_player_info('pathselector')
print(player_info) # A dictionary nested within a list, which is nested within the value of a key in the master dictionary... and that master dictionary contains two key,value pairs...

# My attempt to get inside this badboy... I'm sure its possible since the list is only one value (the dictionary)
# But why use lot word when few word do trick?

# if player_info is not None:
#     print("Here's your info:\n")
#     for list in player_info['results']:
#         for k, v in list:
#             print('{0}:{1}'.format(k, v))
#
#
# else:
#     print('[!] Request Failed')

# Easier way: Unpacking this crazy nested stuff...
print(player_info['results'])
player_dict = player_info['results']
final_dict = player_dict[0]

if player_info is not None:
    print("Here's your info:")
    for k, v in final_dict.items():
        print("{0}: {1}".format(k, v))
else:
    print('[!] Request Failed')

