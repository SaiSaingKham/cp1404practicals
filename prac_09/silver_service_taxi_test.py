from silver_service_taxi import SilverServiceTaxi


def main():
    """SilverServiceTaxi Test"""
    taxi = SilverServiceTaxi("Test Car", 100, 5)
    taxi.drive(68)
    print(taxi)
    print(f"{taxi.get_fare():.2f}")

    taxi1 = SilverServiceTaxi("Test Car", 100, 2)
    taxi1.drive(18)
    print(taxi1)
    print(f"{taxi1.get_fare():.2f}")


if __name__ == '__main__':
    main()