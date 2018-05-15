from train import EdiblesTankCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    # no gen 1 or 2 for edibles tank cars - straight to gen 3

    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=3030,
                                    gen=2,
                                    subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=1190,
                                    gen=3,
                                    subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=2990,
                                    gen=4,
                                    subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=4)

    consist = EdiblesTankCarConsist(roster='pony',
                                    base_numeric_id=3050,
                                    gen=5,
                                    subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    # no need for gen 6, would be same speed + capacity as gen 5

    #--------------- llama ----------------------------------------------------------------------
    consist = EdiblesTankCarConsist(roster='llama',
                                    base_numeric_id=1210,
                                    gen=1,
                                    subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    # no gen 2 for edibles tank cars - straight to gen 3

    consist = EdiblesTankCarConsist(roster='llama',
                                    base_numeric_id=1220,
                                    gen=3,
                                    subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)

    #--------------- antelope ----------------------------------------------------------------------
    consist = EdiblesTankCarConsist(roster='antelope',
                                    base_numeric_id=1690,
                                    gen=1,
                                    subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)

    consist = EdiblesTankCarConsist(roster='antelope',
                                    base_numeric_id=1700,
                                    gen=2,
                                    subtype='A')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)
