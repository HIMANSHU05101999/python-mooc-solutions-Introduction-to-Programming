# WRITE YOUR SOLUTION HERE:
class WeatherStation:
    def __init__ (self, name: str):
        self.__name=name
        self.__observation=[]

    def add_observation(self, observation: str):
            self.__observation.append(observation)
            
    def latest_observation(self):
        if self.__observation:
            tot_obs=self.number_of_observations()-1
            return self.__observation[tot_obs]
        else:
            return ""

    def number_of_observations(self):
        return len(self.__observation)

    def __str__(self):
        return(f"{self.__name}, {self.number_of_observations()} observations")

def main():
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)
if __name__=="__main__":
    main()