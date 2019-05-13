import r6tab_API_functions as r6
import pandas as pd
import sqlalchemy

# Load in list of dictionaries containing leader boards
NA_leaderboard_info = r6.get_leaderboard_info('p_NA_currentmmr')
EU_leaderboard_info = r6.get_leaderboard_info('p_EU_currentmmr')
AS_leaderboard_info = r6.get_leaderboard_info('p_AS_currentmmr')
all_leaderboard_info = r6.get_leaderboard_info('p_currentmmr')

# Store leader boards into pandas data frames to easily upload to mysql server

NA = pd.DataFrame(NA_leaderboard_info)
EU = pd.DataFrame(EU_leaderboard_info)
AS = pd.DataFrame(AS_leaderboard_info)
all = pd.DataFrame(all_leaderboard_info)

# Log in information for mysql server
user = 'root'
passw = 'ops011260910'
host = 'localhost'
database = 'r6_leaderboard_database'

# Establish a connection to the mysql server
engine_stmt = 'mysql+mysqlconnector://%s:%s@%s:3306/%s' % (user, passw, host, database)

engine = sqlalchemy.create_engine(engine_stmt)

# Work the magic

NA.to_sql(name='na_leaderboard', con=engine,
          if_exists='replace', index=False, chunksize=1000)
EU.to_sql(name='eu_leaderboard', con=engine,
          if_exists='replace', index=False, chunksize=1000)
AS.to_sql(name='as_leaderboard', con=engine,
          if_exists='replace', index=False, chunksize=1000)

print('it worked?')

new_df = pd.read_sql("SELECT * FROM eu_leaderboard", engine)

print(new_df)

print('it WORKED.')