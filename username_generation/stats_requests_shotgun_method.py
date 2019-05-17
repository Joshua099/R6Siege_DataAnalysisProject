"""
Using a shotgun methodology to try and get Siege stats from randomly generated screennames
Created by Joshua Pantoja, Kevin Sattakun

"""

# Set up a template with basic use cases for APIs
import json
import multiprocessing as mp
import time

import requests

# Special thanks to R6Tab for their unofficial Rainbow Six Siege API
# https://github.com/Tabwire/R6Tab-API

siege_stats = []

api_token = 'your_api_token'  # Not needed for R6tab
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
        print('[!] [{0}] URL not found: [{1}]'.format(response.status_code, api_url))
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
        print('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))
    return None


# screennames_file = open(r"C:\Users\kevin\.PyCharmCE2018.3\config\scratches\screennames.txt", 'r')
# screennames = screennames_file.readlines()

def get_stats(screenname):
    """Attempt to pass a screenname and get stats back"""
    try:
        print(screenname + " passed.")
        player_info = get_player_info(screenname)
        print(player_info['results'])
        player_dict = player_info['results']
        final_dict = player_dict[0]
        siege_stats.append(final_dict)
    except:
        pass


def main():
    """utilize multiprocessing to read through 800000 randomly generated names and request stats from Siege API"""
    pool = mp.Pool(4)
    with open(r"C:\Users\kevin\.PyCharmCE2018.3\config\scratches\screennames.txt", 'r') as screennames_file:
        screennames = screennames_file.readlines()
        time.sleep(2)
        pool.map(get_stats, (screennames))
    print(len(siege_stats))


if __name__ == "__main__":
    main()
