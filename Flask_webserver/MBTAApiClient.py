import urllib.request, json
import mysqldb

def callMBTAApi():
    mbtaDictList = []
    mbtaUrl = 'https://api-v3.mbta.com/vehicles?filter[route]=1&include=trip'
    with urllib.request.urlopen(mbtaUrl) as url:
        data = json.loads(url.read().decode())
        for bus in data['data']:
            busDict = dict()
            # complete the fields below based on the entries of your SQL table
            busDict['id'] = bus['id']
            busDict['longitude'] = bus['attributes']['longitude']
            busDict['latitude'] = bus['attributes']['latitude']
            busDict['direction_id'] = bus['attributes']['direction_id']
            busDict['current_stop_sequence'] = bus['attributes']['current_stop_sequence']
            busDict['label'] = bus['attributes']['label']
            busDict['speed'] = bus['attributes']['speed']
            busDict['trip_id'] = bus['relationships']['trip']['data']['id']
            busDict['stop_id'] = None
            busDict['bus_bearing'] = bus['attributes']['bearing']
            busDict['occupancy_status'] = bus['attributes']['occupancy_status']
            busDict['current_status'] = bus['attributes']['current_status']
            busDict['updated_at'] = bus['attributes']['updated_at']
            mbtaDictList.append(busDict)
    mysqldb.insertMBTARecord(mbtaDictList) 
    return mbtaDictList