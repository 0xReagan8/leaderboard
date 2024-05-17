import pandas as pd
from tabulate import tabulate
from lib.recruiters.accounting import Accounts
from lib.recruiters.recruits import Recruit

# test credit card
# 4242424242424242

results =  Accounts.leaderboard("classic_punk_party_aq23")

# convert to a dataframe
df = pd.DataFrame(results)

print(tabulate(df, headers='keys', tablefmt='psql'))   

recruits  = Recruit.get_recruits()

print()
