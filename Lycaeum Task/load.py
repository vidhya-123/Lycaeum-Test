import sqlite3, csv, sys

conn  = sqlite3.connect('nba.sqlite')               # Database Connection
cur = conn.cursor()                                 # cur is an object of cursor()
cur.execute('DROP TABLE IF EXISTS nba')             # To remove table if it is already exists
cur.execute('''                                     
    CREATE TABLE "nba"(
         "Number" TEXT,
        "Date" TEXT,
        "Start" TEXT,
        "Visitor" TEXT,
        "PTS" TEXT,
        "Home" TEXT,
        "PTS1" TEXT,
        "Unnamed6" TEXT,
        "Unnamed7" TEXT,
        "Attend" TEXT,
        "Notes" TEXT
        )
 ''')                                                          # To create a table

if len(sys.argv) > 1:                                             # To check argument
   filename = sys.argv[1]                                         # To store 1st argument  ie filename=nba.csv
   F_exctension = filename.split('.')[-1]                         # To check the given file is csv or not
   if F_exctension == 'csv':
      with open(filename) as csv_file:
           csv_reader = csv.reader(csv_file, delimiter=',')          # To read data in csv file,seperated with ','
           for row in csv_reader:                                    # Loop to fetch data and data insert into nba table
              print(row)
              Number = row[0]
              Date = row[1]
              Start = row[2]
              Visitor = row[3]
              PTS = row[4]
              Home = row[5]
              PTS1 = row[6]
              Unnamed6 = row[7]
              Unnamed7 = row[8]
              Attend = row[9]
              Notes = row[10]
              cur.execute('''
                  INSERT INTO nba(Number,Date,Start,Visitor,PTS,Home,PTS1,Unnamed6,Unnamed7,Attend,Notes)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?)''',(Number,Date,Start,Visitor,PTS,Home,PTS1,Unnamed6,Unnamed7,Attend,Notes))

              conn.commit()
   else:
      print("Invalid file")
else:
   print("You must set argument!!!")


