from Calculator import Calculator, Car, ElectroCar

if __name__ == "__main__":
    calc = Calculator(mileage=15000, years=3, year_loss=10)

    calc.add_car(
        Car("Toyota Corolla", 30000, 7, 300, 700)
    )
    calc.add_car(
        ElectroCar("Tesla Model 3", 50000, 800, 150)
    )

    calc.print_cars()
