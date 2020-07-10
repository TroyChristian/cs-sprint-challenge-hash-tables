#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
"""    ticket_hash_table = {}
   route = [None] * len(tickets)
   current_airport = "QQQ"
   next_airport = "ZZZ"

   for ticket in tickets:
       ticket_hash_table[ticket.source] = ticket.destination
   print(ticket_hash_table)

   for key, value in ticket_hash_table.items():
       if key == "NONE":
           route.insert(0, value)
           current_airport = value
       if value == "NONE":
           route.insert(-1, key)
   for key, value in ticket_hash_table.items():
        while next_airport != "NONE":
            if ticket_hash_table[key] == current_airport:
                route.insert(1,value)
                current_airport = value
                next_airport = ticket_hash_table[value]

   return route """
    
