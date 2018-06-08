import hotel
import customer
from reservation import Reservation

class Test():

    rotana_hotel = hotel.Hotel(20,"Rotana","Abu Dhabi",200,40)
    #sheraton_hotel = hotel.Hotel(21,"Sheraton","Abu Dhabi",300,100)

    print hotel.Hotel.hotels
    
    customer1 = customer.Customer("omar")
    customer1.add_customer()
    print customer.Customer.customers

    r1 = Reservation("Rotana", "omar","+1232344332")
    print r1.add_new_reservation()
    print Reservation.reservations


Test()
