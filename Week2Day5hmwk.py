class ParkingGarage:
    def __init__(self, parkingspace=100, tickets = 100):
        self.parkingspaces = parkingspace
        self.tickets = []

    def take_ticket(self,):
        #Decrease amount of tickets available by 1
        #Decrease the amount of parkingspaces by 1
        self.parkingspaces -= 1
        self.tickets.append(Ticket())

        

    
    def spots_available(self):
        return self.parkingspaces
        


    def payforparking(self):
        #display input that waits for amount from user and store as variable
        #If the payment variable is not empty then (meaning the ticket has been paid)
        #-> display a message to the user that their ticket has been paid and they have 15mins to leave
        #This should update the "currentTicket" dictionary key "paid" to True
        amount = (input(""))
        if amount == 0:
            self.paid = True
            print("Your ticket has been paid, you have 15mins to leave.")



    def leavegarage(self):
        #if the ticket has been paid, display a message of "Thank You, have a nice day"
        #If the ticket has not been paid, display an input prompt for payment
        # Once paid, display message "Thank you, have a nice day!"
        #Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
        #Update tickets list to increase by 1 (meaning add to the tickets list)
        if amount == 0:
            print("Thank You, have a nice day")
            self.parkingspaces += 1
            self.tickets.pop(Ticket())
        else:
            print("Please pay your ticket")



    #attributes needed
    # tickets - list tickets = []
     #parkingSpaces -> list parkingspaces = []
    #currentTicket -> dictionary currentticket = {}

class Ticket:
    def __init__(self, paid):
        self.paid = False