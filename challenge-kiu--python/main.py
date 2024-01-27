class Package:
    def __init__(self, sending_date):
        self.sending_date = sending_date
        # aqui irian más campos que se reciben como parámetro. ej:
        self.sending_address = "" 
        self.receiving_address = "" 
        self.customer_id = None 
        self.receiving_date = None # si es None, el packete no fue entregado

class Business:
    def __init__(self, shipping_price):
        self.shipping_price = shipping_price
        self.packages_sent = []

    def send_package(self, package: Package):
        self.packages_sent.append(package)

    def generate_report(self, date):
        packages = self.filter_packages_sent(date)
        total_packages = len(packages)
        total_invoiced = total_packages * self.shipping_price
        return {
            "total_packages": total_packages,
            "total_invoiced": total_invoiced,
        }
    
    def filter_packages_sent(self, date):
        return [p for p in self.packages_sent if p.sending_date == date]
