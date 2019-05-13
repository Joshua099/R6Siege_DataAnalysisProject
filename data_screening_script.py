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

# Trying SQL UNION

with engine.connect() as con:

    union_query = """SELECT * FROM %s UNION SELECT * FROM %s UNION SELECT * FROM %s"""

    test = con.execute(union_query % ('r6_leaderboard_database.na_leaderboard',
                                      'r6_leaderboard_database.eu_leaderboard',
                                      'r6_leaderboard_database.as_leaderboard'))

    # Attempts to get it to work...
    
    # for row in test:
    #     print(row)
    #
    # test_df = pd.read_sql_query(sql=union_query % ('r6_leaderboard_database.na_leaderboard',
    #                                          'r6_leaderboard_database.eu_leaderboard',
    #                                          'r6_leaderboard_database.as_leaderboard'),
    #                       con=con,
    #                       index_col=False,
    #                       chunksize=1000
    #                       )
    #
    # print(list(test_df))

    df = pd.DataFrame(test.fetchall())
    df.columns = test.keys()

    con.close()

print(df)

df.to_sql(name='all_leaderboard', con=engine,
          if_exists='replace', index=False, chunksize=1000)

print('good to go')

# Further Data cleansing is required. First, the data types of the columns are all in TEXT. We need to change some
# into number data types to be able to run analysis on them.

# For example, the kd column is actually a ratio column.

# player One.TT has a kd of 251, which should be 2.51. So we need to do this calculation (kd / 100)

# similar situation for p_headshotaccuracy.

# One.TT has a hs accuracy of 64,590,000. This should be a percentage (64.59%): (p_headshotacc / 1,000,000)

# Other columns such as p_currentmmr should simply be an integer column.

with engine.connect() as con:

    aggregate_query = """
                      SELECT p_name,
                             cast(kd / 100 as decimal(10,2)) as kd_ratio, 
                             cast(p_headshotacc / 1000000 as decimal(10,2)) as p_headshotacc,
                             cast(p_currentmmr as UNSIGNED) as p_currentmmr,
                             cast(p_level as UNSIGNED) as p_level,
                             cast(p_skillrating as UNSIGNED) as p_skillrating
                        FROM all_leaderboard
                      """

    aggregate_exec = con.execute(aggregate_query)

    df_aggregate = pd.DataFrame(aggregate_exec.fetchall())
    df_aggregate.columns = aggregate_exec.keys()
    print(df_aggregate)

    con.close()

df_aggregate.to_sql(name='training', con=engine,
          if_exists='replace', index=False, chunksize=1000)
print('good to go')
