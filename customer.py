class Customer():
    customers = []
    def __init__(self, name):
        self.name = name


    def add_customer(self):
        for item in Customer.customers:
            if item == self.name:
                return 'found'

        Customer.customers.append(self.name)

    def dell_customer(self,name):
        for item in Customer.customers:
            if item == self.name:
                Customer.customers.remove(item)
