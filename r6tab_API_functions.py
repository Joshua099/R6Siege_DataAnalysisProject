# Based on my generic API template
import json
import requests

# Special thanks to R6Tab for their unofficial Rainbow Six Siege API
# https://github.com/Tabwire/R6Tab-API
# Functions are for uplay platform ONLY


api_token = 'your_api_token' # Not needed for R6tab


headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}


def get_player_info(player_name):

    """ Get a specified player's name. """

    api_url_base = 'https://r6tab.com/api/search.php?platform=uplay&search='
    api_url = api_url_base + player_name

    response = requests.get(api_url, headers=headers)

    # Error Handling
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


def get_leaderboard_info(sortregion_method):
    """ Get the leaderboard information for a specified region. """

    api_url_base = 'https://r6tab.com/api/leaderboards.php?sortplatform=uplay&sortregion='
    api_url = api_url_base + sortregion_method

    response = requests.get(api_url, headers=headers)

    # Error Handling
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


