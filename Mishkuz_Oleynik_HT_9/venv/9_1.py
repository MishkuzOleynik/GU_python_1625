from time import sleep

class TrifficLight:
    __color = ["Red", "Yellow", "Green"]
    count = 1

    def runnig(self, n):
        repeat = 0
        while repeat < n:
            for TrifficLight.count in range(1, 4):
                print(f'{TrifficLight.__color[TrifficLight.count - 1]}')
                if TrifficLight.count == 1:
                    sleep(7)
                elif TrifficLight.count == 2:
                    sleep(2)
                elif TrifficLight.count == 3:
                    sleep(10)
                TrifficLight.count +=1
            repeat += 1
traffic_light = TrifficLight()
traffic_light.runnig(2)

