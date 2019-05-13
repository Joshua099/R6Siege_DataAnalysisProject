import r6tab_API_functions as r6
import pandas as pd
import sqlalchemy

# Log in information for mysql server
user = 'root'
passw = 'ops011260910'
host = 'localhost'
database = 'r6_leaderboard_database'

# Establish a connection to the mysql server

engine_stmt = 'mysql+mysqlconnector://%s:%s@%s:3306/%s' % (user, passw, host, database)

engine = sqlalchemy.create_engine(engine_stmt)

# Data Screening

# ISSUE: the different leader board tables contain the same amount of columns and data types. BUT they are in a
# different order.

# To use SQL UNION, they must be in the same order.

# Rearrange columns to be uniform across all tables before combining.

# Each region's leader board has a separately labeled p_REGION_currentmmr field. In the rainbow six database, this is
# actually a global mmr. Also, in each region:
# p_REGION_currentmmr == p_currentmmr.

# So to solve this issue, delete each leader board table's p_REGION_currentmmr

# So let's check what's up with these two columns
# with engine.connect() as con:
#     check_dup = con.execute('select p_EU_currentmmr, p_currentmmr from r6_leaderboard_database.eu_leaderboard')
#
#     print(check_dup.keys())
#     for row in check_dup:
#         print(row)
#
#     con.close()

# Delete the p_REGION_currentmmr columns from each table

# Do a test run first..
with engine.connect() as con:
    try:
        sql_delete_query = """ALTER TABLE %s DROP COLUMN %s"""
        con.execute(sql_delete_query % ('r6_leaderboard_database.na_test', 'p_NA_currentmmr'))

        print('delete done')
    except:
        print("Already Deleted")

    con.close()

# Real Run
with engine.connect() as con:
    try:
        sql_delete_query = """ALTER TABLE %s DROP COLUMN %s"""
        con.execute(sql_delete_query % ('r6_leaderboard_database.na_leaderboard', 'p_NA_currentmmr'))
        con.execute(sql_delete_query % ('r6_leaderboard_database.eu_leaderboard', 'p_EU_currentmmr'))
        con.execute(sql_delete_query % ('r6_leaderboard_database.as_leaderboard', 'p_AS_currentmmr'))

        print('delete done')
    except:
        print("Already Deleted")

    con.close()

