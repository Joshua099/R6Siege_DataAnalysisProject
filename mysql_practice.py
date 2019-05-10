import r6tab_API_functions as r6
import pandas as pd
from pandas.io import sql
import mysql.connector
import pymysql
import sqlalchemy

# Test it

NA_leaderboard_info = r6.get_leaderboard_info('p_NA_currentmmr')
EU_leaderboard_info = r6.get_leaderboard_info('p_EU_currentmmr')
AS_leaderboard_info = r6.get_leaderboard_info('p_AS_currentmmr')
all_leaderboard_info = r6.get_leaderboard_info('p_currentmmr')



# DataFrame loading

NA = pd.DataFrame(NA_leaderboard_info)
EU = pd.DataFrame(EU_leaderboard_info)
AS = pd.DataFrame(AS_leaderboard_info)
all = pd.DataFrame(all_leaderboard_info)


# print(NA)
# Creating database and tables
user = 'root'
passw = 'ops011260910'
host = 'localhost'
port = '3306'
database = 'r6_leaderboard_database'

engine_stmt = 'mysql+mysqlconnector://%s:%s@%s:3306/%s' % ('root', 'passw here', 'localhost', 'r6_leaderboard_database')

engine = sqlalchemy.create_engine(engine_stmt)

# Work the magic

NA.to_sql(name='na_leaderboard', con=engine,
          if_exists='replace', index=False, chunksize=1000)
EU.to_sql(name='eu_leaderboard', con=engine,
          if_exists='replace', index=False, chunksize=1000)
AS.to_sql(name='as_leaderboard', con=engine,
          if_exists='replace', index=False, chunksize=1000)


print('it worked?')

new_df = pd.read_sql("SELECT * FROM na_test", engine)

print(new_df)

print('it WORKED.')


# All my fuckin' attempts

# engine = create_engine('mysql+mysqlconnector://[root]:[pw here]@[localhost]:[3306]/[r6_leaderboard_database]', echo=False)
#
# NA.to_sql(name='test_NA', con=engine, if_exists='replace')


# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd="pw here"
#     )
# print(conn)
# c = conn.cursor()
# # c.execute("CREATE DATABASE r6_leaderboard_database")
# c.execute("SHOW DATABASES")
# for x in c:
#     print(x)
#
# mydb = pymysql.connect(host="localhost", port=3306, user="root", passwd="pw here", db="r6_leaderboard_database")
#
# NA.to_sql(con=conn, name='NA_leaders', if_exists='replace',)



# Adding the data frames
#
# column_names = []
# for k in NA_leaderboard_info[0]:
#     column_names.append(k)
#
# print(column_names)

# conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="passw here", db="r6_leaderboard_database")
# try:
#     with conn.cursor() as cursor:
#         column_names = [
#             'position', 'p_id', 'p_name', 'p_level', 'p_platform', 'p_user', 'p_currentmmr',
#             'p_currentrank', 'p_skillrating', 'p_NA_rank', 'p_EU_rank', 'p_AS_rank', 'kd', 'verified',
#             'p_headshotacc', 'p_NA_currentmmr'
#         ]
#         column_names_str = ', '.join(column_names)
#         binds_str = ', '.join('%' for _ in range(len(column_names))) # %bind prevents any additional typos.
#
#         for data_dict in NA_leaderboard_info:
#             sql = ("INSERT INTO 'NA_leaderboard' ({column_names}) VALUES({binds})").format(column_names=column_names_str, binds=binds_str)
#             values = [data_dict[column_name] for column_name in column_names]
#             cursor.execute(sql, values)
#
#         print("Insert successful!")
#         conn.commit()
# finally:
#     conn.close()
