"""
    GUI Based Program
    For Predictions with ML Model
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LinearRegression
import tkinter as tk

model = None
RDSpend = None
MKSpend = None


window = None
canvas = None

entry_X1 = None
entry_X2 = None




def on_click():

    global model
    global RDSpend
    global MKSpend

    global window
    global canvas

    global entry_X1
    global entry_X2

    RDSpend = float(entry_X1.get())
    MKSpend = float(entry_X2.get())

    print(RDSpend)
    print(MKSpend)

    predicted_profit = model.predict([[RDSpend, MKSpend]])
    predicted_text = ("Predicted Profit", predicted_profit)
    lbl_predicted_text = tk.Label(window, text=predicted_text)
    canvas.create_window(260, 280, window=lbl_predicted_text)


def prepare_model():

    global model
    global RDSpend
    global MKSpend

    global window
    global canvas

    data_set = pd.read_csv("company_profits.csv")

    X = data_set[['R&DSpend', 'MarketingSpend']]
    Y = data_set['Profit']

    model = LinearRegression()
    model.fit(X, Y)

    print("Interceptor:", model.intercept_)
    print("Coefficients:", model.coef_)

    # Profit = 48591.08 + 0.7712254*R&DSpend + 0.03033984*MarketingSpend

    RDSpend = 144372.41
    MKSpend = 383199.62

    predicted_profit = model.predict([[RDSpend, MKSpend]])
    print("predicted_profit is:", predicted_profit)

    return data_set

def main():

    global window
    global canvas

    global entry_X1
    global entry_X2


    data_set = prepare_model()

    window = tk.Tk()
    canvas = tk.Canvas(window, width=500, height=300)
    canvas.pack()

    interctept_text = ("Interceptor", model.intercept_)
    lbl_interctept_text = tk.Label(window, text=interctept_text, justify='center')
    lbl_interctept_text.pack()

    coef_text = ("Coefficients", model.coef_)
    lbl_coef_text = tk.Label(window, text=coef_text, justify='center')
    lbl_coef_text.pack()

    lbl_X1 = tk.Label(window, text="R&D Spend: ")
    canvas.create_window(100, 100, window=lbl_X1)

    entry_X1 = tk.Entry(window)
    canvas.create_window(260, 100, window=entry_X1)

    lbl_X2 = tk.Label(window, text="Marketing Spend: ")
    canvas.create_window(110, 130, window=lbl_X2)

    entry_X2 = tk.Entry(window)
    canvas.create_window(260, 130, window=entry_X2)

    btn_predict = tk.Button(window, text="PREDICT PROFIT", command=on_click)
    canvas.create_window(260, 160, window=btn_predict)


    # Plot Graph in Tkinter Window | R&DSpend VS Profit
    figure1 = plt.Figure(figsize=(5, 4), dpi=100)
    sub_plot1 = figure1.add_subplot(111)
    sub_plot1.scatter(data_set['R&DSpend'].astype(float), data_set['Profit'].astype(float), color='red')
    scatter_graph1 = FigureCanvasTkAgg(figure1, window)
    scatter_graph1.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
    sub_plot1.set_xlabel("R&D Spend")
    sub_plot1.set_ylabel("Profit")

    # Plot Graph in Tkinter Window | MarketingSpend VS Profit
    figure2 = plt.Figure(figsize=(5, 4), dpi=100)
    sub_plot2 = figure2.add_subplot(111)
    sub_plot2.scatter(data_set['MarketingSpend'].astype(float), data_set['Profit'].astype(float), color='green')
    scatter_graph2 = FigureCanvasTkAgg(figure2, window)
    scatter_graph2.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH)
    sub_plot2.set_xlabel("Marketing Spend")
    sub_plot2.set_ylabel("Profit")

    window.mainloop()

if __name__ == '__main__':
    main()