"""
    Apriori Algorithm

    DataSet

    TID Cover   Guard   PowerBank   Charger
    1   1       1       1           1
    2   1       0       1           1
    3   0       0       1           1
    4   0       1       0           0
    5   1       1       1           1
    6   1       1       0           1


    1. Support
    Support(Cover) = Number of Transactions in which Cover Appeared / Total Number of Transactions
    Support(Cover) = 4/6 => 0.66

    2. Confidence
    Confidence({Cover, Guard} => {PowerBank}) = Support({Cover, Guard, PowerBank}) / Support({Cover, Guard})
                                              = 2/6 / 3/6
                                              = 0.66
    3. Lift
    Lift({Cover, Guard} => {PowerBank}) = Support({Cover, Guard, PowerBank}) / Support(Cover) * Support(Guard)
                                        = 2/6  / 4/6*4/6
                                        = 0.77

    Lift(x=>y) = 1, no correlation so do not consider the relationship
    Lift(x=>y) > 1, positive correlation, likely to be bought
    Lift(x=>y) < 1, negative correlation, unlikely to be bought

    4. Conviction
    Conviction({Cover, Guard} => {PowerBank}) = 1 - Support(PowerBank) / 1-Confidence({Cover, Guard} => {PowerBank})
                                              = 1 - 4/6  / 1- 2/6 / 3/6
                                              = ?

    Conviction(x=>y) = 1, no correlation so do not consider the relationship
    Conviction(x=>y) > 1, More the Value, higher the Interest of item being purchased


    Frequency Tables  | To find Association Rules
    ----------------

    Item        Frequency
    Cover       4
    Guard       4
    PowerBank   4
    Charger     5


    Consider some Threshold Value -> 3 ( Support Value :) )
    Item        Frequency
    Cover       4
    Guard       4
    PowerBank   4
    Charger     5

    Lets Make Some Pairs
    Item                Frequency
    Cover, Guard        3
    Cover, PowerBank    3
    Cover, Charger      4
    Guard, PowerBank    2
    Guard, Charger      3
    PowerBank, Charger  4

    Based on our Support value Threshold i.e. 3
    We got below associations
    1. Cover, Charger
    2. PowerBank, Charger


"""
import pandas as pd
from apyori import apriori # pip install apyori

data_set = pd.read_csv("transactions.csv", header=None)
print(data_set)

print(data_set.shape)

records = []
for i in range(data_set.shape[0]):
    records.append([str(data_set.values[i, j]) for j in range(data_set.shape[1])])

print(records)

for record in records:
    print(record)

association_rules = apriori(records, min_support=0.50, min_confidence=0.7, min_lift=1, min_length=2)
# print(list(association_rules))

for rule in association_rules:
    print(rule)