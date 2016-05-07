from bottle import route, run, template, response, request
import csv
import psycopg2

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

def footy_search(stat):
    conn = psycopg2.connect("dbname=scottmccann user=scottmccann")
    cur = conn.cursor()
    print(stat)
    cur.execute("""SELECT %s FROM man_u""",(stat, ))
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




@route('/')
@route('/hello/')
@route('/hello/<name>')
def index(name="Pardner"):

    return template('<div>Hello, {{person}}!</div>', person=name)


@route('/ManU')
def send_Data():
    pullStats = footy_Out()
    sendStats = pullStats
    response.content_type = 'application/json; charset=UTF-8'

    return {1:sendStats}


@route('/ManU/<stat:re:[a-z]+>')
def player_search(stat):
    search = footy_search(stat)
    response.content_type = 'application/json; charset=UTF-8'

    return {stat: search}





########

delete = footy_Delete()
readStats = stat_Reader()
insertStats = read_ToDb(readStats)
#
# for row in pullStats:
#     print("Player: " +  str(row[0]) +' '+ str(row[1] + ' ' + str(row[2])))
#     print('      Position: '+ str(row[3]))
#     print('      Games Played: ' + str(row[6]))
#     print('      Goals Scored: ' + str(row[7]))
#     print('      ')
#     print(pullStats)


run(host='localhost', port=8080,
     debug=True,reloader=True)
