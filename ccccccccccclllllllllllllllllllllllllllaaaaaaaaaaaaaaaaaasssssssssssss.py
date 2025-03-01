ytrewq = {
    12345678910: ["цфыв","еапн","шолд","хэжъ"],
    19876543210: ["цфывf","еапнh","шолдk","икея"]
}

class Aqatobos:
    def __init__(self,trip):
        self.trip = trip
    def antenavegator(self,trip_stop):
        trip_marshute = ytrewq[self.trip]
        print(f"автобус {self.trip} прибыл на остановку {trip_marshute[trip_stop]}")

erorrrrrrrrrre = Aqatobos(12345678910)
erorrrrrrrrrre2 = Aqatobos(19876543210)
for o in range(4):
    erorrrrrrrrrre.antenavegator(o)
    erorrrrrrrrrre2.antenavegator(o)