"""
    Multi Threading
"""

import threading
import requests

# class PrintingTask:
#
#     def printDocument(self, name):
#         for i in range(1, 11):
#             print("Printing #{}# Copy #{}".format(name, i))

# A child thread is a class which is going to be inherited from threading.Thread class. A built in class
# run function needs to be overrided and we must keep all our jobs to be done in it :)
class PrintingTask(threading.Thread):

    # def __init__(self, name):
    #     threading.Thread.__init__(self) # if you create your constructor, execute Parent's as well
    #     self.name = name

    def init_printing_details(self, name):
        self.name = name

    def run(self):
        for i in range(1, 11):
            print("Printing #{}# Copy #{}".format(self.name, i))

# Totally dependent on Internet speed and may be the news data which we are fetching
class FetchNewsTask(threading.Thread):

    def run(self):
        url = "http://newsapi.org/v2/everything?q=bitcoin&from=2020-07-31&sortBy=publishedAt&apiKey=31c21508fad64116acd229c10ac11e84"
        response = requests.get(url)
        print(response.text)

# Rather than a normal class -> make it a thread as it may be a long running operation
# class FetchNewsTask():
#
#     def fetch(self):
#         url = "http://newsapi.org/v2/everything?q=bitcoin&from=2020-07-31&sortBy=publishedAt&apiKey=31c21508fad64116acd229c10ac11e84"
#         response = requests.get(url)
#         print(response.text)

def main():

    print("Main Started")

    news_task = FetchNewsTask()
    news_task.start() # start internally executes the run
    # news_task.fetch()

    # task = PrintingTask(name="LearningGo.pdf")
    # task.printDocument("LearningGo.pdf")
    task = PrintingTask()
    task.init_printing_details(name="LearningGo.pdf")
    task.start() # start internally executes the run function :)

    for i in range(1, 11):
        print("Printing *LearningPython.pdf* Copy #{}".format(i))

    print("Main Finished")


if __name__ == '__main__':
    main()