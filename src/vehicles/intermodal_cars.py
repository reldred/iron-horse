from train import IntermodalCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------
    """
    consist = IntermodalCarConsist(roster='pony',
                                   base_numeric_id=3710,
                                   gen=4,
                                   subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = IntermodalCarConsist(roster='pony',
                                   base_numeric_id=3720,
                                   gen=4,
                                   subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)


    consist = IntermodalCarConsist(roster='pony',
                                   base_numeric_id=3730,
                                   gen=5,
                                   subtype='B')

    consist.add_unit(type=FreightCar,
                     vehicle_length=6)


    consist = IntermodalCarConsist(roster='pony',
                                   base_numeric_id=3740,
                                   gen=5,
                                   subtype='C')

    consist.add_unit(type=FreightCar,
                     vehicle_length=8)
    """

    consist = IntermodalCarConsist(roster='pony',
                                   base_numeric_id=3770,
                                   gen=6,
                                   subtype='A',
                                   sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = IntermodalCarConsist(roster='pony',
                                   base_numeric_id=3750,
                                   gen=6,
                                   subtype='B',
                                   sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_24px')


    consist = IntermodalCarConsist(roster='pony',
                                   base_numeric_id=3760,
                                   gen=6,
                                   subtype='C',
                                   sprites_complete=False)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_1cc_filled_32px')

    #--------------- llama ----------------------------------------------------------------------
