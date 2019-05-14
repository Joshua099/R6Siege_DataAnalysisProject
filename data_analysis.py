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

# EDA on p_currentmmr and kd_ratio

eda_query = """SELECT kd_ratio, p_currentmmr FROM r6_leaderboard_database.training"""
eda_df = pd.read_sql(eda_query, con=engine)


# OLS of kd_ratio on p_currentmmr
result = sm.ols(formula="p_currentmmr ~ kd_ratio", data=eda_df).fit()

print(result.params)

print(result.summary())

sns.lmplot(x='kd_ratio', y='p_currentmmr', data=eda_df, height=12)
plt.show()
