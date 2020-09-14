import pandas as pd
import matplotlib.pyplot as plt

"""
    Plot Total Sales per month in Year
    How the total sales has increased over the months in an year
    which month has lowest sales
"""

def anaylze_yearly_sales():
    table = pd.read_csv("BigMartSalesData.csv")
    print(table)

    print()

    # extract the rows as a table where year is 2011
    table_year_2011 = table[table['Year'] == 2011]
    print(table_year_2011)

    print()

    # sales per month
    # we need to group the data
    sales_year_2011_monthly_data = table_year_2011.groupby('Month').sum()['Amount']
    print(sales_year_2011_monthly_data)

    # plt.plot(sales_year_2011_monthly_data.index, sales_year_2011_monthly_data.values)
    # plt.bar(sales_year_2011_monthly_data.index, sales_year_2011_monthly_data.values, color="red")
    # plt.xlabel("Month")
    # plt.xlabel("Sales")
    # plt.title("Big Mart 2011 Sales Report")
    # plt.show()

    print("Lowest Sales {} recorded in month {}".format(sales_year_2011_monthly_data.min(), sales_year_2011_monthly_data.idxmin()))
    print("Highest Sales {} recorded in month {}".format(sales_year_2011_monthly_data.max(),
                                                        sales_year_2011_monthly_data.idxmax()))

def anaylze_global_sales():
    table = pd.read_csv("BigMartSalesData.csv")
    print(table)

    print()

    # extract the rows as a table where year is 2011
    table_year_2011 = table[table['Year'] == 2011]
    print(table_year_2011)

    print()

    # Group Data Country Wise for year 2011
    table_year_2011_countrywise_sales = table_year_2011.groupby('Country').sum()['Amount']
    print(table_year_2011_countrywise_sales)

    plt.pie(table_year_2011_countrywise_sales.values, labels=table_year_2011_countrywise_sales.values, autopct='%1.1f%%')
    plt.legend()
    plt.show()

    # Plot the data in wel formatted way :)
    # You may use seaborn :)

def analyze_sales_concentration():
    table = pd.read_csv("BigMartSalesData.csv")
    print(table)

    print()

    # extract the rows as a table where year is 2011
    table_year_2011 = table[table['Year'] == 2011]
    print(table_year_2011)

    # group the data on the invoice and plot it as scatter plot to see concentrations
    table_year_2011_invoice_sales = table_year_2011.groupby('InvoiceNo').sum()['Amount']
    print(table_year_2011_invoice_sales)

    plt.scatter(table_year_2011_invoice_sales.values, table_year_2011_invoice_sales.values)
    plt.show()

def main():
    # anaylze_yearly_sales()
    # anaylze_global_sales()
    analyze_sales_concentration()

if __name__ == '__main__':
    main()