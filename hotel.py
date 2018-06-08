class Hotel():
    hotels = []
    def __init__(self, number,hotel_name, city,total_rooms,empty_rooms):
        self.number = number
        self.hotel_name = hotel_name
        self.city = city
        self.total_rooms = total_rooms
        self.empty_rooms = empty_rooms

        Hotel.hotels.append([self.number , self.hotel_name, self.city, self.total_rooms, self.empty_rooms])

    def list_hotels_in_city(self):
        count = 0
        for item in Hotel.hotels:
            if self.city in item:
                print Hotel.hotels[count][1], "  ", Hotel.hotels[count][2]
            count += 1
