"""
    Integrating FLASK with ML/DL
"""

from flask import *

from sklearn.datasets import load_iris
from sklearn import tree

app = Flask("MyApp")
model = tree.DecisionTreeClassifier()
NAMES = None

@app.route("/")
def index():
    return render_template("ml-index.html")


@app.route("/train")
def train_model():
    global NAMES
    # loading a built in data set from sklearn
    iris_data_set = load_iris()

    FEATURES = iris_data_set.data
    LABELS = iris_data_set.target
    NAMES = iris_data_set.target_names
    model.fit(FEATURES, LABELS)

    return render_template("ml-training-success.html", classes=str(NAMES))

@app.route("/predict", methods=["POST"])
def predict_class():
    global NAMES
    # Read Features from HTTP request and convert it to type as expected by us
    feature1 = float(request.form["feature1"])
    feature2 = float(request.form["feature2"])
    feature3 = float(request.form["feature3"])
    feature4 = float(request.form["feature4"])

    features = [feature1, feature2, feature3, feature4]
    print(features)

    predicted_label = model.predict([features])

    print(predicted_label)

    # return "LABEL PREDICTED IS {} and CLASS IS {}".format(predicted_label, NAMES[predicted_label[0]])
    return render_template("ml-prediction.html", predicted_class="{} | {}".format(predicted_label, NAMES[predicted_label[0]]))

if __name__ == '__main__':
    app.run(debug=True)
