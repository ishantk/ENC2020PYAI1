"""
    Decision Trees
"""

import pandas as pd
import numpy as np

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

def compute_entropy_space():
    # E(S) = -P(yes) * log_base2(P(yes)) - P(no) * log_base2(P(no))
    # E(S) = -P(9/14) * log_base2(P(9/14)) - P(5/14) * log_base2(P(5/14))
    # E(S) = 0.94

    total = len(table['play'])
    num_of_yes = len(table[table['play'] == 'yes'])
    num_of_no = len(table[table['play'] == 'no'])

    probability_yes = num_of_yes / total
    probability_no = num_of_no / total

    print("Total: {} Yes: {} No: {}".format(total, num_of_yes, num_of_no))
    print("P(yes): {} P(no): {}".format(probability_yes, probability_no))

    entropy_space = -(probability_yes * np.log2(probability_yes)) -(probability_no * np.log2(probability_no))
    # print("E(S): {}".format(entropy_space))

    return entropy_space


def information_gain_in_outlook():
    pass

def information_gain_in_temperature():
    pass

def information_gain_in_humidity():
    pass

def information_gain_in_windy():
    pass


print("E(S):", compute_entropy_space())
print("IG(Outlook):", information_gain_in_outlook())            # 0.247
print("IG(Temperature):", information_gain_in_temperature())    # 0.029
print("IG(Humidity):", information_gain_in_humidity())          # 0.152
print("IG(Windy):", information_gain_in_windy())                # 0.048