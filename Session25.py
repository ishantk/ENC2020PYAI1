"""
    Surprise Surprise Surprise :)

    Hackathon
    Live Online Coding

    Go to repl.it
    Share link of file in which you are working on the chat and whatsapp group

    Problem Statement:
    Garbage Collection Management
    > Console Based Software

    Their are 5 different plot sizes from 100 sq yards to 500 sq yards
    which a customer owns

    1. Create a Class Property(housenum, block, street, area, size with address and size details
    2. Create a Class Customer(name, phone, email, property) with details
    3. Link Customer and Property
       1 Customer can have 1 Property :)
    4. Create a Class Fee(phone, month, year, amount) which manages Fee for Garbage Collection every month
       Fee has to be saved in the file

    Problem Statement for Algorithmic Approach:
        A customer paid in th month of Aug i.e. 8
        9876512345, 8, 2020, 250
        9876512345, 9, 2020, 0
        9876512345, 10, 2020, 0
        9876512345, 11, 2020, 250+(500 + 0.30*500)
        Now he kipped 2 months and he has to pay in November month
        So, take the difference and calculate the bill accordingly

        A fine for 30% of the amount paid to be imposed for the non paid months

"""

fee_structure = {
    "100": 100,
    "200": 150,
    "300": 200,
    "400": 250,
    "500": 300,
}