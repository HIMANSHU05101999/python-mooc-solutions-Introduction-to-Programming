# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str):
    from pathlib import Path
    filename=Path(__file__).parent/filename
    dict={}
    with open(filename) as file:
        for line in file:
            #print(line.strip().split(";"))
            new_line=line.strip().split(";")
            if "name" in new_line:
                continue
            #for i in range(len(new_line)):
                #print(new_line[i])
            long=float(new_line[0])
            lat=float(new_line[1])
            dict[new_line[3]]=(long,lat)
    return(dict)

def distance_calculation(longitude1: int, longitude2: int, latitude1:int, latitude2: int):
    import math

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return(distance_km)

def distance(stations: dict, station1: str, station2: str):
    for key,val in stations.items():
        if station1 in key:
            long1=val[0]
            lat1=val[1]
        elif station2 in key:
            long2=val[0]
            lat2=val[1]
    return(distance_calculation(long1,long2,lat1,lat2))

def greatest_distance(stations: dict):
    temp_store_station=[]
    temp=0
    final_output=()
    for key in stations:
        #print("inner_loop")
        initial_station=key
        long1=stations[key][0]
        lat1=stations[key][1]
        #print(initial_station,long1,lat1)
        temp_store_station.append(key)
        for new_key in stations:
            if new_key in temp_store_station:
                continue
            else:
                #print("outer_loop")
                compare_station=new_key
                long2=stations[new_key][0]
                lat2=stations[new_key][1]
                #print(compare_station,long2,lat2)
                dis_bw=distance_calculation(long1,long2,lat1,lat2)
                if temp<dis_bw:
                    temp=dis_bw
                    final_output=(initial_station,compare_station,temp)
    return(final_output)                
       




def main():
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
    

if __name__=="__main__":
    main()