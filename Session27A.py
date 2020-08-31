"""
    Multi Threading
    Synchronization
    (Locking)
"""

import threading
import time

# Create a Global Lock Object :)
lock = threading.Lock()

class MovieTicket:

    def __init__(self, name, time, row, seat_num):
        self.name = name
        self.time = time
        self.row = row
        self.seat_num = seat_num
        self.is_booked = False

    def book_movie_ticket(self):
        if self.is_booked:
            print("------")
        else:
            self.is_booked = True
            print("Ticket Details: {} | {} | {} | {} | {}".format(self.name, self.time, self.row, self.seat_num, self.email))

    def pay(self, email):

        self.email = email

        if self.is_booked:
            print("Sorry {}, This Ticket {} is already booked".format(self.email, self.seat_num))
        else:
            print("{}, Please Pay for your Movie Ticket {}".format(self.email, self.seat_num))
            time.sleep(1) # Just assuming 1 second time for payment transaction :)
            print("{}, Thank you for your Transaction for Seat {}".format(self.email, self.seat_num))


class BookMovieTicket(threading.Thread):

    def select_seat(self, ticket, email):
        self.ticket = ticket
        self.email = email

    def run(self):
        lock.acquire()
        self.ticket.pay(email=self.email)
        self.ticket.book_movie_ticket()
        lock.release()

def main():

    ticket1 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=1)
    ticket2 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=2)
    ticket3 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=3)
    ticket4 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=4)
    ticket5 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=5)
    ticket6 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=6)
    ticket7 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=7)
    ticket8 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=8)
    ticket9 = MovieTicket(name="Avengers", time="20:00", row="A", seat_num=9)

    row_a = [ticket1, ticket2, ticket3, ticket4, ticket5, ticket6, ticket7, ticket8, ticket9]

    user1 = BookMovieTicket()
    user2 = BookMovieTicket()

    # We may have a use case where both users would like to book the same movie ticket
    user1.select_seat(ticket=row_a[5], email="john@example.com")
    user2.select_seat(ticket=row_a[5], email="fionna@example.com")

    user1.start()
    user2.start()


if __name__ == '__main__':
    main()

# In Multi Threading -> we solve the problem by running any operation which takes more time in a separate thread
# >>>>> BUT, a situation where 2 threads can try accessing the same object may come <<<<
# Here, we need to implement synchronization

# synchronization -> when 2 diferent threads try to access the same object, they must execute the code in a sequence