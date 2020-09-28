import matplotlib.pyplot as plt
from sklearn import datasets, svm
from sklearn.model_selection import train_test_split
from sklearn import metrics


# 1. Prepare the Data Set
digits = datasets.load_digits()

# Features are RGB collection of Image as input
FEATURES = digits.data

# Which are corresponding to the Input points and the classes which we wish to predict
LABELS = digits.target

print(digits.target_names)

# 2. Divide the DataSet
x_train, x_test, y_train, y_test = train_test_split(FEATURES, LABELS, test_size=0.3, random_state=1)

# 3. Create the Model
model = svm.SVC()

# 4. Train the Model
model.fit(x_train, y_train)

# 5. Do prediction on unseen data i.e. x_test and get prediction for finding accuracy scores
y_pred = model.predict(x_test)
print(y_pred)

score = metrics.accuracy_score(y_test, y_pred)
print("Accuracy Score:", score)

plt.subplot(2, 4, 1)
plt.imshow(digits['images'][8], cmap=plt.cm.gray_r)
plt.show()

predicted_label = model.predict([FEATURES[8]])
print(predicted_label)


# Assignment: Download the DataSet of Images
# 1. Cats and Dogs
# 2. Apples and Oranges
# 3. Human Faces and Lion Faces :)

# Simply replace Images DataSet with your own DataSet :)


# Reference Reading for Mathematical Part of SVM
# https://www.svm-tutorial.com/2014/11/svm-understanding-math-part-1/
# https://www.svm-tutorial.com/2014/11/svm-understanding-math-part-2/
# https://www.svm-tutorial.com/2014/11/svm-understanding-math-part-3/
