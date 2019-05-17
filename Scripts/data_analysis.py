import pandas as pd
import sqlalchemy
import statsmodels.formula.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

# Log in information for mysql server
user = 'root'
passw = 'pw'
host = 'localhost'
database = 'r6_leaderboard_database'

# Establish a connection to the mysql server

engine_stmt = 'mysql+mysqlconnector://%s:%s@%s:3306/%s' % (user, passw, host, database)

engine = sqlalchemy.create_engine(engine_stmt)

query = """
        SELECT kd_ratio, 
               p_headshotacc, 
               p_currentmmr, 
               p_level, 
               p_skillrating 
          FROM r6_leaderboard_database.focus
        """

df = pd.read_sql(query, con=engine)
print(df.isnull().sum())
plt.figure(figsize=(10, 10))
sns.heatmap(df.corr(), annot=True, fmt='.1f')
plt.show()
# # OLS of kd_ratio on p_currentmmr
#
# query = """SELECT kd_ratio, p_currentmmr FROM r6_leaderboard_database.training"""
# df = pd.read_sql(query, con=engine)
#
# result = sm.ols(formula="p_currentmmr ~ kd_ratio", data=df).fit()
#
# print(result.summary())
#
# sns.lmplot(x='kd_ratio', y='p_currentmmr', data=df, height=8)
# plt.show()
#
#
# # OLS of p_headshotacc on p_currentmmr
#
# query = """SELECT p_headshotacc, p_currentmmr FROM r6_leaderboard_database.training"""
# df = pd.read_sql(query, con=engine)
#
# result = sm.ols(formula="p_currentmmr ~ p_headshotacc", data=df).fit()
#
# print(result.summary())
#
# sns.lmplot(x='p_headshotacc', y='p_currentmmr', data=df, height=8)
# plt.show()
#
# # OLS of p_skillrating on p_currentmmr
#
# query = """SELECT p_skillrating, p_currentmmr FROM r6_leaderboard_database.training"""
# df = pd.read_sql(query, con=engine)
#
# result = sm.ols(formula="p_currentmmr ~ p_skillrating", data=df).fit()
#
# print(result.summary())
#
# sns.lmplot(x='p_skillrating', y='p_currentmmr', data=df, height=8)
# plt.show()
#
#
# # OLS of kd_ratio + p_headshotacc + p_skillrating on p_currentmmr
#
# query = """SELECT kd_ratio, p_headshotacc, p_skillrating, p_currentmmr FROM r6_leaderboard_database.training"""
# df = pd.read_sql(query, con=engine)
#
# result = sm.ols(formula="p_currentmmr ~ kd_ratio + p_headshotacc + p_skillrating", data=df).fit()
#
# print(result.summary())
#
# ******************** BEGINNING OF MODEL 2 ***********************
# EDA of kd_ratio on p_skillrating

query = """SELECT kd_ratio, p_skillrating FROM r6_leaderboard_database.training"""
df = pd.read_sql(query, con=engine)

result = sm.ols(formula="p_skillrating ~ kd_ratio", data=df).fit()

print(result.summary())

sns.lmplot(x='kd_ratio', y='p_skillrating', data=df, height=8)
plt.show()

# EDA of p_headshotacc on p_skillrating

query = """SELECT p_headshotacc, p_skillrating FROM r6_leaderboard_database.training"""
df = pd.read_sql(query, con=engine)

result = sm.ols(formula="p_skillrating ~ p_headshotacc", data=df).fit()

print(result.summary())

sns.lmplot(x='p_headshotacc', y='p_skillrating', data=df, height=8)
plt.show()

# EDA of p_currentmmr on p_skillrating

query = """SELECT p_currentmmr, p_skillrating FROM r6_leaderboard_database.training"""
df = pd.read_sql(query, con=engine)

result = sm.ols(formula="p_skillrating ~ p_currentmmr", data=df).fit()

print(result.summary())

sns.lmplot(x='p_currentmmr', y='p_skillrating', data=df, height=8)
plt.show()

# EDA of kd_ratio + p_headshotacc on p_skillrating

query = """SELECT kd_ratio, p_headshotacc, p_skillrating FROM r6_leaderboard_database.training"""
df = pd.read_sql(query, con=engine)

result = sm.ols(formula="p_skillrating ~ kd_ratio + p_headshotacc", data=df).fit()

print(result.summary())



# Multiple OLS of kd_ratio + p_headshotacc + p_currentmmr on p_skillrating

query = """SELECT kd_ratio, p_headshotacc, p_currentmmr, p_skillrating FROM r6_leaderboard_database.training"""
df = pd.read_sql(query, con=engine)

result = sm.ols(formula="p_skillrating ~ kd_ratio + p_headshotacc +p_currentmmr", data=df).fit()

print(result.summary())