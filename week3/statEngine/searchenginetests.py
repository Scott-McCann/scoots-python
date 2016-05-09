
import csv
import psycopg2
import unittest
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

def fetch():
    conn = psycopg2.connect("dbname=scottmccann user=scottmccann")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM man_u""")
    data = cur.fetchone()
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



class Unittest(unittest.TestCase):
    def test_Stat_Reader(self):
        stats = stat_Reader()
        print(stats)
        self.assertTrue(len(stats) != 0 )
        self.assertFalse(type(stats) is dict)

    def test_Read_ToDb(self):
        stats = stat_Reader()
        loadData = read_ToDb(stats)
        pull = footy_Out()
        print(pull)
        self.assertTrue(len(pull) != 0)
        self.assertFalse(type(pull) is dict)
        self.assertTrue(type(stats) is list)

    def test_insert(self):
        stats = stat_Reader()
        player = stats[0]
        insertion = insert(player)
        data = fetch()
        self.assertTrue(player[3] in data[4])
        self.assertFalse(player[2] in data[5])

    def test_fetch(self):
        stats = stat_Reader()
        player = stats[0]
        insertion = insert(player)
        data = fetch()
        self.assertTrue(player[3] in data[4])
        self.assertFalse(player[7] in data[5])

    def test_Footy_Out(self):
        d = footy_Delete()
        stats = stat_Reader()
        loadData = read_ToDb(stats)
        data = footy_Out()
        self.assertTrue(len(data) != 0)
        self.assertFalse(stats in data)
        self.assertTrue(data != stats)

    def test_Footy_Delete(self):
        stats = stat_Reader()
        loadData = read_ToDb(stats)
        data = footy_Out()
        d = footy_Delete()
        nothing = footy_Out()
        self.assertFalse(nothing)
        self.assertTrue(nothing not in data)
        self.assertFalse(data == nothing)






if __name__ == '__main__':
    unittest.main()
