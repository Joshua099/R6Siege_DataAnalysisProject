import pandas as pd
import sqlalchemy
import statsmodels.formula.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

# Log in information for mysql server
user = 'root'
passw = 'ops011260910'
host = 'localhost'
database = 'r6_leaderboard_database'

# Establish a connection to the mysql server

engine_stmt = 'mysql+mysqlconnector://%s:%s@%s:3306/%s' % (user, passw, host, database)

engine = sqlalchemy.create_engine(engine_stmt)

# OLS of kd_ratio on p_currentmmr

query1 = """SELECT kd_ratio, p_currentmmr FROM r6_leaderboard_database.training"""
df1 = pd.read_sql(query1, con=engine)

result = sm.ols(formula="p_currentmmr ~ kd_ratio", data=df1).fit()

print(result.params)
print(result.summary())

sns.lmplot(x='kd_ratio', y='p_currentmmr', data=df1, height=12)
plt.show()


# OLS of kd_ratio + p_headshotacc on p_currentmmr

query2 = """SELECT kd_ratio, p_headshotacc, p_currentmmr FROM r6_leaderboard_database.training"""
df2 = pd.read_sql(query2, con=engine)

result2 = sm.ols(formula="p_currentmmr ~ kd_ratio + p_headshotacc", data=df2).fit()

print(result2.summary())


# OLS of kd_ratio + p_headshotacc + p_skillrating on p_currentmmr

query3 = """SELECT kd_ratio, p_headshotacc, p_skillrating, p_currentmmr FROM r6_leaderboard_database.training"""
df3 = pd.read_sql(query3, con=engine)

result3 = sm.ols(formula="p_currentmmr ~ kd_ratio + p_headshotacc + p_skillrating", data=df3).fit()

print(result3.summary())
