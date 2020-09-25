"""
    Dummy Variables -> One Hot Encoding
    One Hot Encoding is to replace categorical data with numerical values of either 1 or 0

            outlook temperature humidity  windy play
    0      sunny         hot     high  false    no
    1      sunny         hot     high   true    no
    2   overcast         hot     high  false    yes
    3      rainy        mild     high  false    yes
    4      rainy        cool   normal  false    yes
    5      rainy        cool   normal   true    no
    6   overcast        cool   normal   true    yes
    7      sunny        mild     high  false    no
    8      sunny        cool   normal  false    yes
    9      rainy        mild   normal  false    yes
    10     sunny        mild   normal   true    yes
    11  overcast        mild     high   true    yes
    12  overcast         hot   normal  false    yes
    13     rainy        mild     high   true    no

    We have data which is categorical
    outlook has 3 values -> sunny, overcast and rainy

    break outlook itself in 3 attributes        | outlook_sunny, outlook_overcast, outlook_rainy
    break temperature itself in 3 attributes    | temperature_hot, temperature_mild, temperature_cool
    break humidity in 2 attributes              | humidity_high, humidity_normal
    break windy itself in 2 attributes          | windy_true, windy_false

    outlook_sunny, outlook_overcast, outlook_rainy,  temperature_hot, temperature_mild, temperature_cool, humidity_high, humidity_normal, windy_true, windy_false, play
    1              0                 0               1                0                 0                 1              0                0           1            0

"""

import pandas as pd

table = pd.DataFrame()

# Outlook Column
table['outlook'] = ['sunny', 'sunny', 'overcast', 'rainy', 'rainy', 'rainy', 'overcast', 'sunny',
                    'sunny', 'rainy', 'sunny', 'overcast', 'overcast', 'rainy']


# Temperature Column
table['temperature'] = ['hot', 'hot', 'hot', 'mild', 'cool',
                        'cool', 'cool', 'mild', 'cool', 'mild',
                        'mild', 'mild', 'hot', 'mild']

# Humidity Column
table['humidity'] = ['high', 'high', 'high', 'high', 'normal', 'normal',
                     'normal', 'high', 'normal', 'normal','normal', 'high', 'normal', 'high']

# Windy Column
table['windy'] = ['false', 'true', 'false', 'false', 'false', 'true',
                  'true', 'false', 'false', 'false', 'true',
                  'true', 'false', 'true']

# Play Column
table['play'] = ['no', 'no', 'yes', 'yes', 'yes', 'no',
                 'yes', 'no', 'yes', 'yes', 'yes',
                 'yes', 'yes', 'no']

print(table)
print()


# When Outlook is sunny
print("When Outlook is sunny")
# len(table.loc((table['outlook'] == 'sunny') & (table['play'] == 'no')))
sunny_data_set = table[table['outlook'] == 'sunny']
print(sunny_data_set)
print(len(sunny_data_set))

sunny_no = sunny_data_set[sunny_data_set['play'] == 'no']
sunny_yes = sunny_data_set[sunny_data_set['play'] == 'yes']

print(sunny_no)
print(len(sunny_no))

print(sunny_yes)
print(len(sunny_yes))

print()

# When Outlook is Overcast
print("When Outlook is Overcast")
overcast_data_set = table[table['outlook'] == 'overcast']
print(overcast_data_set)
print(len(overcast_data_set))

overcast_no = overcast_data_set[overcast_data_set['play'] == 'no']
overcast_yes = overcast_data_set[overcast_data_set['play'] == 'yes']

print(overcast_no)
print(len(overcast_no))

print(overcast_yes)
print(len(overcast_yes))

print()

# When Outlook is rainy
print("When Outlook is rainy")
rainy_data_set = table[table['outlook'] == 'rainy']
print(rainy_data_set)
print(len(rainy_data_set))

rainy_no = rainy_data_set[rainy_data_set['play'] == 'no']
rainy_yes = rainy_data_set[rainy_data_set['play'] == 'yes']

print(rainy_no)
print(len(rainy_no))

print(rainy_yes)
print(len(rainy_yes))

print()

print("FREQUENCY TABLE FOR WEATHER")
# Creating a New Table from Pandas
frequency_table = pd.DataFrame()
frequency_table['Weather'] = ['Overcast', 'Rainy', 'Sunny', 'GrandTotal']

frequency_table['No'] = [len(overcast_no), len(rainy_no), len(sunny_no), (len(overcast_no)+len(rainy_no)+len(sunny_no))]
frequency_table['Yes'] = [len(overcast_yes), len(rainy_yes), len(sunny_yes), (len(overcast_yes)+len(rainy_yes)+len(sunny_yes))]

print(frequency_table)
print()

print("LIKELIHOOD TABLE FOR WEATHER")
# Creating a New Table from Pandas
likelihood_table = pd.DataFrame()
likelihood_table['Weather'] = ['Overcast', 'Rainy', 'Sunny', 'No', 'Yes']


likelihood_table['Probability'] = [
                                    (len(overcast_no)+len(overcast_yes))/len(table), (len(rainy_no)+len(rainy_yes))/len(table), (len(sunny_no)+len(sunny_yes))/len(table),
    (len(overcast_no)+len(rainy_no)+len(sunny_no))/len(table), (len(overcast_yes)+len(rainy_yes)+len(sunny_yes))/len(table)
                                   ]

print(likelihood_table)

# Bayes Theoram:
# P(Yes | Sunny) = P(Sunny | Yes) * P(Yes) / P (Sunny)

probability_yes_sunny = None # ?

