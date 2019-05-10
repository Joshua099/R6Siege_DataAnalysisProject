import r6tab_API_functions as r6
import pandas as pd

# Test it

NA_leaderboard_info = r6.get_leaderboard_info('p_NA_currentmmr')
print(NA_leaderboard_info)
print(type(NA_leaderboard_info))

# Leaderboard info sends back a list of dictionaries
# Here's a loop to retrieve info on each player

# if NA_leaderboard_info is not None:
#     for i in NA_leaderboard_info:
#         print("\nHere's your info:")
#         for k, v in i.items():
#             print("{0}: {1}".format(k, v))
# else:
#     print('[!] Request Failed')

EU_leaderboard_info = r6.get_leaderboard_info('p_EU_currentmmr')
print(EU_leaderboard_info)
print(type(EU_leaderboard_info))

AS_leaderboard_info = r6.get_leaderboard_info('p_AS_currentmmr')
print(AS_leaderboard_info)
print(type(AS_leaderboard_info))

all_leaderboard_info = r6.get_leaderboard_info('p_currentmmr')
print(all_leaderboard_info)
print(type(all_leaderboard_info))

# DataFrame loading

NA = pd.DataFrame(NA_leaderboard_info)
print(NA)

EU = pd.DataFrame(EU_leaderboard_info)
AS = pd.DataFrame(AS_leaderboard_info)
all = pd.DataFrame(all_leaderboard_info)

