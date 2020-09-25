"""
    Dummy Variables -> One Hot Encoding
    One Hot Encoding is to replace categorical data with numerical values of either 1 or 0

             outlook temperature humidity  windy play
    0      sunny         hot     high  false   no
    1      sunny         hot     high   true   no
    2   overcast         hot     high  false  yes
    3      rainy        mild     high  false  yes
    4      rainy        cool   normal  false  yes
    5      rainy        cool   normal   true   no
    6   overcast        cool   normal   true  yes
    7      sunny        mild     high  false   no
    8      sunny        cool   normal  false  yes
    9      rainy        mild   normal  false  yes
    10     sunny        mild   normal   true  yes
    11  overcast        mild     high   true  yes
    12  overcast         hot   normal  false  yes
    13     rainy        mild     high   true   no

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
from sklearn import tree
from sklearn import metrics                             # Accuracy Scores
from sklearn.model_selection import train_test_split    # Break the DataSet randomly into testing and training


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

# get_dummies from pandas shall do one hot encoding for us
one_hot_encoded_table = pd.get_dummies(table[['outlook', 'temperature', 'humidity',  'windy']])
print(one_hot_encoded_table)

print()

print(one_hot_encoded_table['outlook_overcast'])

x_train, x_test, y_train, y_test = train_test_split(one_hot_encoded_table, table['play'], test_size=0.3, random_state=1)

# 2. Create the Model
model = tree.DecisionTreeClassifier()

# 3. Train the Model with Split Data Set
model.fit(x_train, y_train)

# 4. Check for Accuracy by making predictions on test data set
y_pred = model.predict(x_test)
accuracy = metrics.accuracy_score(y_test, y_pred) # original and predicted y
print("ACCURACY SCORE:", accuracy)
print()

# outlook = sunny, temperature = hot, humidity = normal, windy false

input_data = [0, 0, 1, 0, 1, 0, 0, 1, 1, 0]
predicted_class = model.predict([input_data])
print("Predicted Class is:", predicted_class)