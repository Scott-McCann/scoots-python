from bottle import route, run, template, response, request
import csv
import psycopg2
import time
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
def read_ToDb(List):
    conn = psycopg2.connect("dbname=scottmccann user=scottmccann")
    cur = conn.cursor()
    for row in List:
        cur.execute("""
    INSERT INTO man_u
                (kit,
                 first_name,
                 last_name,
                 position,
                 born,
                 international,
                 games_played,
                 goals,
                 yellow_cards,
                 red_cards)
          VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", row)
    conn.commit()
    cur.close()


def insert(List):
    conn = psycopg2.connect('dbname=scottmccann user=scottmccann')
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO man_u
               (kit,
                first_name,
                last_name,
                position,
                born,
                international,
                games_played,
                goals,
                yellow_cards,
                red_cards)
                VALUES (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s)""", List)
    conn.commit()
    cur.close()

#Get data from Database
def footy_Out():
    conn = psycopg2.connect("dbname=scottmccann user=scottmccann")
    cur = conn.cursor()
    cur.execute("""
    SELECT kit,
           first_name,
           last_name,
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

# def footy_search(stat):
#     conn = psycopg2.connect("dbname=scottmccann user=scottmccann")
#     cur = conn.cursor()
#     print(stat)
#     cur.execute("""SELECT %s FROM man_u""",(stat,))
#     data = cur.fetchall()
#     conn.commit()
#     cur.close()
#
#     return data


#Delete data from table
def footy_Delete():
    conn = psycopg2.connect("dbname=scottmccann user=scottmccann")
    cur = conn.cursor()
    cur.execute("""
    DELETE FROM man_u
    """)
    conn.commit()
    cur.close()




# @route('/')
# @route('/hello/')
# @route('/hello/<name>')
# def index(name="Pardner"):
#
#     return template('<div>Hello, {{person}}!</div>', person=name)
#
#
# @route('/ManU')
# def send_Data():
#     pullStats = footy_Out()
#     sendStats = pullStats
#     response.content_type = 'application/json; charset=UTF-8'
#
#     return {1:sendStats[0]}
#
#
# @route('/ManU/<stat:re:[a-z]+>')
# def player_search(stat):
#     search = footy_search(stat)
#     response.content_type = 'application/json; charset=UTF-8'
#
#     return {stat: search}





########

# delete = footy_Delete()
# readStats = stat_Reader()
# insertStats = read_ToDb(readStats)



print("""
                       _,aaadP""""""Ybaaaa,,_
                   ,adP,__,,,aaaadPYYYYY888888a,_
                ,a8888888P"''             "Y8888888b,
             _a888888888"                   `Y88888888b,
           ,d888888888P'                       "888888888b,
         ,'88888888P"Y8,                       ,P'   `""Y888b,
       ,d8888P"'     "Ya,                    ,P'         `Ya`b,
      ,P88"'           `Ya,                 ,P'            `b`Yi
     d",P                `"Y,              ,P'              `Y "i
   ,P' P'                   "888888888888888b                `b "i
  ,P' d'                    d8888888888888888b                `b `b
  d' d'                    ,'888888888888888888b                I, Y,
 ,f ,f                    ,'88888888888888888888b               `b, b
 d' d'                    d888888888888888888888b              ,'88,I
,P  8'                    ,88888888888888888888888b,_          ,d8888
d'  8,                   d8888888888888888888888P'`"Ya,_     ,d88888
p  d88b,             ,adP""Y888888888888888888P'      `""Ya, d88888P
p '88888b,       ,adP"'     `"Y8888888888888"'             `"888888I
Y'88888888b, ,adP"'             ""Y888888P"                  '888888'
'888888888888P'                     ""YP"                    888888
 I88888888888'                         8                     88888I
 `Y8888888888'                         8                     88888'
  `Y888888888'                         8                     8888I
   `Y88888888'                         8                     8P"8'
    `Y8888888'                         8                   ,d',d'
     `b"Y8b                            8                 ,d" ,d'
       "b,   Y,                       '8               ,P" ,d"
         "b,   "Ya,_                 ,d88ba,,___   _,aP" ,P"
           "Ya_   ""Ya,_       _,,ad88888888888888P"' _,d"
             `"Ya_    ""Yaaad88888888888888888888P _,d"'
                 `"Ya,_     "Y888888888888888888P",d"'
                    `""Ya,__`Y888888888888888P

""")
print("""
███████╗ ██████╗  ██████╗ ████████╗██╗   ██╗    ███████╗████████╗ █████╗ ████████╗███████╗
██╔════╝██╔═══██╗██╔═══██╗╚══██╔══╝╚██╗ ██╔╝    ██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝
█████╗  ██║   ██║██║   ██║   ██║    ╚████╔╝     ███████╗   ██║   ███████║   ██║   ███████╗
██╔══╝  ██║   ██║██║   ██║   ██║     ╚██╔╝      ╚════██║   ██║   ██╔══██║   ██║   ╚════██║
██║     ╚██████╔╝╚██████╔╝   ██║      ██║       ███████║   ██║   ██║  ██║   ██║   ███████║
╚═╝      ╚═════╝  ╚═════╝    ╚═╝      ╚═╝       ╚══════╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝
""")
print("                      WELCOME TO FOOTY STATS!!")

choice = 'n'

while choice is not 'q':
    print("[d]elete, [l]oad, [u]pdate, [v]iew, [i]nsert, [q]uit ")

    choice = input("What would you like to do? ")
    if choice is 'd':
        delete = footy_Delete()
        print("cleaning table....")
        print('.')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('...')
        print('Table is clean')

    elif choice is 'l':
        # stats = stat_Reader()
        load = read_ToDb(stat_Reader())
        print('.')
        time.sleep(1)
        print('..')
        time.sleep(1)
        print('Table loaded')

    elif choice is 'v':
        viewChoice = 'a'
        data = footy_Out()

        print('[a]ll, [p]layer, [g]oals, [c]ards, [n]games played [b]ack')
        viewChoice = input("What would you like to search by? ")
        viewChoice.lower()

        if viewChoice is 'a':
            for row in data:
                print('''Kit#: {} Name: {} {}
                position: {}
                from: {}
                international: {}
                games: {}
                goals: {}
                yellow cards: {}
                red cards: {}

                '''.format(str(row[0]),
                            str(row[1]),
                            str(row[2]),
                            str(row[3]),
                            str(row[4]),
                            str(row[5]),
                            str(row[6]),
                            str(row[7]),
                            str(row[8]),
                            str(row[9])))

        elif viewChoice is 'p':
            for row in data:
                print('''Kit#: {} Name: {} {}
                Position: {}'''.format(str(row[0]),
                                        str(row[1]),
                                        str(row[2]),
                                        str(row[3])))
                print(' ')


        elif viewChoice is 'g':
            for row in data:
                print('''Kit#: {} Name: {} {}
                Goals Scored: {}'''.format(str(row[0]),
                                            str(row[1]),
                                            str(row[2]),
                                            str(row[6])))
                print(' ')


        elif viewChoice is 'c':
            for row in data:
                print('''Kit#: {} Name: {} {}
                Yellow Cards: {}
                Red Cards:    {}'''.format(str(row[0]),
                                            str(row[1]),
                                            str(row[2]),
                                            str(row[8]),
                                            str(row[9])))
                print(' ')

        elif viewChoice is 'n':
            for row in data:
                print('''Kit#: {} Name: {} {}
                Games Played:  {}'''.format(str(row[0]),
                                             str(row[1]),
                                             str(row[2]),
                                             str(row[6])))
                print(' ')

        elif viewChoice is 'b':
            pass


        else:
            print('please enter a valid command')

    elif choice is 'i':
        statlist = []
        accept = ' '
        print("Please enter a new player: ")
        stat = input("Please enter the kit #: ")
        statlist.append(stat)
        stat = input("please enter a first name: ")
        statlist.append(stat)
        stat = input("please enter a Last name: ")
        statlist.append(stat)
        stat = input("please enter a Position: ")
        statlist.append(stat)
        stat = input("please enter where the player was born?: ")
        statlist.append(stat)
        stat = input("Does the player play on an international team?: ")
        statlist.append(stat)
        stat = input("How many games has he played?: ")
        statlist.append(stat)
        stat = input("How many goals has he scored?: ")
        statlist.append(stat)
        stat = input("How many yellow cards does he have?: ")
        statlist.append(stat)
        stat = input("How many red cards does he have?: ")
        statlist.append(stat)

        print("This is the Player You wish to add:")
        print('''Kit#: {} Name: {} {}
        position: {}
        from: {}
        international: {}
        games: {}
        goals: {}
        yellow cards: {}
        red cards: {}''' .format(str(statlist[0]),
                                 str(statlist[1]),
                                 str(statlist[2]),
                                 str(statlist[3]),
                                 str(statlist[4]),
                                 str(statlist[5]),
                                 str(statlist[6]),
                                 str(statlist[7]),
                                 str(statlist[8]),
                                 str(statlist[9])))
        print(' ')

        accept = input("Would you like to submit this player to the Database?[y/n]")
        if accept is 'y':
            insert(statlist)

        else:
            statlist = []








# for row in readStats:
#
#


# run(host='localhost', port=8080,
#      debug=True,reloader=True)
