from main import Business, Package
from time_helpers import get_current_date, get_yesterday_date, get_tomorrow_date

shipping_price = 10

def validate_date_results(business: Business, date, packages_quantity):
    results = business.generate_report(date)
    if results["total_packages"] != packages_quantity:
        return False
    if results["total_invoiced"] != packages_quantity * shipping_price:
        return False
    return True


def test_all_packages_today():
    business = Business(shipping_price)
    today_date = get_current_date()
    packages_quantity = 15
    # create today shippings
    for _ in range(packages_quantity):
        package = Package(sending_date=today_date)
        business.send_package(package)
    # validate report
    if not validate_date_results(business, today_date, packages_quantity):
        raise Exception("Error en los resultados al validar un solo día")


def test_all_packages_different_days():
    business = Business(shipping_price)
    today_date = get_current_date()
    yesterday_date = get_yesterday_date()
    tomorrow_date = get_tomorrow_date()
    packages_quantity_today = 8
    packages_quantity_yesterday = 5
    packages_quantity_tomorrow = 13
    # create today shippings
    for _ in range(packages_quantity_today):
        package = Package(sending_date=today_date)
        business.send_package(package)
    # create yesterday shippings
    for _ in range(packages_quantity_yesterday):
        package = Package(sending_date=yesterday_date)
        business.send_package(package)
    # create tomorrow shippings
    for _ in range(packages_quantity_tomorrow):
        package = Package(sending_date=tomorrow_date)
        business.send_package(package)
    # validate report
    if not validate_date_results(business, today_date, packages_quantity_today):
        raise Exception("Error en los resultados de la fecha de hoy")
    if not validate_date_results(business, yesterday_date, packages_quantity_yesterday):
        raise Exception("Error en los resultados de la fecha de ayer")
    if not validate_date_results(business, tomorrow_date, packages_quantity_tomorrow):
        raise Exception("Error en los resultados de la fecha de mañana")


def run_all_tests():
    try:
        test_all_packages_today()
        test_all_packages_different_days()
    except Exception as e:
        print(f"\033[91m{e}\033[0m")
        return
    print("\033[92mLos test se ejecturaron sin errores\033[0m")


run_all_tests()