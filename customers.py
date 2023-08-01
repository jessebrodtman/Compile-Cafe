from cmu_graphics import *

class Customer:
    def __init__(self, name, ticket):
        self.name = name
        self.ticket = ticket
        self.served = False

    def serve(self):
        self.served = True
    
    def __eq__(self, other):
        if not isinstance(other, Customer): return False
        return (self.name == other.name) and (self.ticket==other.ticket)
    
    def __repr__(self):
        return f'Customer(Name: {self.name}, Served: {self.served})'

    def __hash__(self):
        return hash(str(self))