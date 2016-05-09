import csv
import psycopg2





# eliver a script that when run on the command line will ask if the user would like to like to import the data, or search the data. It is up to you to make your search as flexible as you would like. Can I search by name? Can I search by position? Can I search by age? Make an option for whatever you think best fits your data. And for inserting new data - make it a convenient experience. Prompt me for every column value as I enter it.
#
# Easy Mode
# Design a database structure (schema) that will fit your data model. Your data model is how the statistics for your sport are organized. If you can't think of a sport to analyze - give American football a try. Here is a link to the Nebraska Cornhuskers stats from 1983 (http://www.sports-reference.com/cfb/schools/nebraska/1983.html). Find the Rushing and Receiving table and create a database table structure that allows you to store that data inside of it.
# Create a python function that uses DELETE to delete the data in the table(s) created in #1.
# Create a python function to load your data into your program. In the Cornhuskers example above, the data isn't available via an API, so you'll have to save the csv data into a file, and load that with python's csv module. Follow this tutorial if the docs don't make sense.
# Create a python function that will take the data structure you created in #3, and insert the sample data into your database using the cursor.execute method with some INSERT statements.
# Write the main part of your script that asks the user if they want to import the data. If they do, first use the function from #2 to delete any existing data, then the function from #3 to load the data, and finally the function from #4 to insert the data in the database.
# At this point you should be able to use the psql command to SELECT * FROM <table> and see the data.
#
#Read stat csv.
def stat_Reader():
    playerData = []
    with open('manchester_united _stats.csv') as csvfile:
        playerReader = csv.reader(csvfile)
        header = next(playerReader)
        for row in playerReader:
            playerData.append(row[:])

    return playerData

# #INSERT data into table.
def footy_In(List):
    conn = psycopg2.connect("dbname=scottmccann user=scottmccann")
    cur = conn.cursor()
    for row in List:
        cur.execute("""
    INSERT INTO man_u
                (kit,
                 player,
                 position,
                 born,
                 international,
                 games_played,
                 goals,
                 yellow_cards,
                 red_cards)
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", row)
    conn.commit()
    cur.close()

#Get data from Database
def footy_Out():
    conn = psycopg2.connect("dbname=scottmccann user=scottmccann")
    cur = conn.cursor()
    cur.execute("""
    SELECT kit,
           player,
           position,
           born,
           international,
           games_played,
           goals,
           yellow_cards,
           red_cards
    FROM man_u ORDER BY kit
    """)
    data = cur.fetchall()
    conn.commit()
    cur.close()


    return data

#Delete data from table
def footy_Delete():
    conn = psycopg2.connect("dbname=scottmccann user=scottmccann")
    cur = conn.cursor()
    cur.execute("""
    DELETE FROM man_u
    """)
    conn.commit()
    cur.close()



########

delete = footy_Delete()
readStats = stat_Reader()
insertStats = footy_In(readStats)
pullStats= footy_Out()

for row in pullStats:
    print("Player: " +  str(row[0]) +' '+ str(row[1]))
    print('      Position: '+ str(row[2]))
    print('      Games Played: ' + str(row[5]))
    print('      Goals Scored: ' + str(row[6]))
    print(' ')
