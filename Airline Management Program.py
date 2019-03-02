# AIRLINE MANAGEMENT SYSTEM
# This Program Includes:
# 1. Reservations w.r.t route 
# 2. Fleet Management 
# 3. Pilot Management
# 4. Flight Routes 

import random
import string
import sys

# def main(Airline):     
# print('****** WELCOME TO QUANTUS AIRLINES ******')
# print('Choose one of the following options :')
# print('1. Book Flight')
# print('2. Pilot Login')
# print('3. Distance calculation between airports')
# user_response = print(int(input('Enter your response :')))

# if user_response == 1:
#     Booking = lambda: Flight_Booking()
# elif user_response == 2:
# main()  

class Airline:      ## Parent class for this System

    no_of_planes = 0
    no_of_pilots = 0
    no_of_passengers = 0

    class Booking:            ## Class for Booking Seats

        # def Flight_Booking():

        print('')

        def Pass_name():        ## Function for Entering Passenger name 
            return str(input("Enter your Name :"))
        Pass_name()
        print('')        

        def con_no():       ## Function for Entering Passenger's Contact number
            return int(input("Enter you Cell Number :"))
        con_no()
        print('')

        def dep_air():      ## Fucntion for Departure airport of passenger
            print("'LON', 'JFK', 'DEL', 'AMD', 'SIN'")
            user_response = str(input('Enter your Departure Airport from above airports :'))
            print('')

            if user_response in  ['LON', 'JFK', 'DEL', 'AMD', 'SIN']:
                Booking: lambda: arr_air()
            else:
                print('ENTERED AIRPORT IS INVALID !!!!')
                sys.exit()

        dep_air()
        print('')

        def arr_air():      ##  Fucntion for Arrival airport of passenger
            print("'LON', 'JFK', 'DEL', 'AMD', 'SIN'")
            str(input('Enter your Destination Airport from above airport : '))
        arr_air()
        print('')

        def Seat_Booking():         ## Functions for Generating Seat Number
            return (random.choice(string.ascii_letters[0:25]).upper() + str(random.randint(0,9)))
        print('Your Seat Number is : ')
        print(Seat_Booking()) 
        print('')

        Dict = {'name': Pass_name(), 'contact no': con_no(), 'seat no': Seat_Booking(), 'Dep Airport': dep_air(), 'Arr Airport': arr_air()}

        print(Booking.no_of_passengers)

        # Flight_Booking()

    # class Fleet(Airline):       ## Class for Fleet Information

    #     def fleet_info():       ## Function for Fleet Info
    #         Planes = ['A380', 'B320', 'ATR72']

    class Pilot(Airline):       ## Class for Pilot Details

        def pilot_name():       ## Function for Entering Pilot Information 
            print(str(input('Enter Pilot\'s Name: ')))
        pilot_name()

        def pilot_exp():        ## Function for Entering Pilot's Experience in Hours
            print(int('Enter Pilot\'s Experience in Hours :'))
        pilot_exp()

        Pilot_info = {'name': pilot_name(), 'pilot_exp': pilot_exp()}

    class Flight_Route(Airline, Pilot):     ## Class for making flight route

        Rou_Dis = [['LON', 'JFK', 'DEL', 'AMD', 'SIN'], [5000, 6000, 7000, 6000, 10000]] 
        for elem in Rou_Dis:
            print(elem, end ='')
        print()

        # def Route_Assign():   ## Function for assigning flight route to pilots
        #     if exp < 500:
        #     #    distance < 500

        #     elif exp < 1000 and exp > 500:
        #      #   distance 
