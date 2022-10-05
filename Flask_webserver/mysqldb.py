import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = "insert into mbta_buses ( id, longitude, latitude, direction_id, current_stop_sequence, label, speed, trip_id, stop_id, bus_bearing, occupancy_status, current_status, updated_at) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (mbtaDict['id'], mbtaDict['longitude'], mbtaDict['latitude'], mbtaDict['direction_id'], mbtaDict['current_stop_sequence'], mbtaDict['label'], mbtaDict['speed'], mbtaDict['trip_id'], mbtaDict['stop_id'], mbtaDict['bus_bearing'], mbtaDict['occupancy_status'], mbtaDict['current_status'], mbtaDict['updated_at'])
        mycursor.execute(sql, val)

    mydb.commit()