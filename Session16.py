"""
    DataBase
    MySQL :)

    XAMPP: Accessible on Web UI
    https://www.apachefriends.org/download.html

    Accessible on Command Prompt
    https://dev.mysql.com/downloads/installer/

    PS: During Installation username and password will be asked
    if you dont put anything, user-> root and password->
    else, you need to remember what user and password you have

    DataBase
    Its a Collection of Tables

    Table
    Its a Collection or Rows and Columns
    Every Row in a Table is a record i.e. data
    Columns represent attributes of an object :)

    Step1: in PhpMyAdmin
    create database. give any name

    Step2: in database
    create a table

    ORM: Object Relational Mapping :)
    CovidIndia: state, confirmed, active, recovered, deceased, tested

    SQL Command:


    create table CovidIndia(
        state varchar(256) primary key,
        confirmed int,
        active int,
        recovered int,
        deceased int,
        tested int
    )


    insert into CovidIndia values('Maharashtra', 536790, 286512, 34566, 3455, 43314516)

    update CovidIndia set confirmed=636790, active=386512 where state = 'Maharashtra'

    fetching the data
    select * from CovidIndia
    select confirmed, active from CovidIndia
    select * from CovidIndia where state = 'Punjab'
    select * from CovidIndia where active > 500000

    delete from CovidIndia where state = 'Punjab'

    Ref for Learning and Exploring SQL : w3schools


"""

class CovidIndia:

    def __init__(self, state, confirmed, active, recovered, deceased, tested):
        self.state = state
        self.confirmed = confirmed
        self.active = active
        self.recovered = recovered
        self.deceased = deceased
        self.tested = tested


def main():
    # Object is constructed in the RAM. It is temporary and we must save its data in File or DB
    cRef1 = CovidIndia("Maharashtra", 536790, 286512, 34566, 3455, 43314516)
    print(cRef1.__dict__)

if __name__ == '__main__':
    main()