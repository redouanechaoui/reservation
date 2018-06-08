from hotel import Hotel
from customer import Customer
#import notification

class Reservation():
    reservations = []
    def __init__(self, hotel, customer, customer_num):
        self.hotel = hotel
        self.customer = customer
        self.number = customer_num

    def add_new_reservation(self):
        count = 0
        for item in Hotel.hotels:
            if self.hotel in item:
                if Hotel.hotels[count][4] == 0:
                    #send_text_message("sorry no rooms availeble", customer_num)
                    return "no sorry"
                else:
                    Reservation.reservations.append([self.hotel, self.customer, self.number])
                    #send_text_message("confirmation", customer_num)
                    Hotel.hotels[count][4] -=1
                    return 'confirmation'
            count +=1

    def list_resevrations_for_hotel(self):
        count = 0
        for item in Reservation.reservations:
            if hotel in item:
                print Reservation.reservations[count][1]
            count += 1
