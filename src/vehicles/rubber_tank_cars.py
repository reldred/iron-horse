from train import RubberTankCarConsist, FreightCar


def main():
    #--------------- pony ----------------------------------------------------------------------

    consist = RubberTankCarConsist(roster_id='pony',
                             base_numeric_id=4280,
                             gen=2,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')

    """
    # not needed?
    consist = RubberTankCarConsist(roster_id='pony',
                             base_numeric_id=4290,
                             gen=2,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')
    """

    consist = RubberTankCarConsist(roster_id='pony',
                             base_numeric_id=4300,
                             gen=3,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_filled_16px')


    consist = RubberTankCarConsist(roster_id='pony',
                             base_numeric_id=4310,
                             gen=3,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_gapped_24px')


    consist = RubberTankCarConsist(roster_id='pony',
                             base_numeric_id=4330,
                             gen=4,
                             subtype='A',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='2_axle_sparse_16px')


    consist = RubberTankCarConsist(roster_id='pony',
                             base_numeric_id=4340,
                             gen=4,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = RubberTankCarConsist(roster_id='pony',
                             base_numeric_id=4350,
                             gen=4,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')

    # no gen 5A or 6A

    consist = RubberTankCarConsist(roster_id='pony',
                             base_numeric_id=4370,
                             gen=5,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = RubberTankCarConsist(roster_id='pony',
                             base_numeric_id=4700,
                             gen=5,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')


    consist = RubberTankCarConsist(roster_id='pony',
                             base_numeric_id=4710,
                             gen=6,
                             subtype='B',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_24px')


    consist = RubberTankCarConsist(roster_id='pony',
                             base_numeric_id=4720,
                             gen=6,
                             subtype='C',
                             sprites_complete=True)

    consist.add_unit(type=FreightCar,
                     chassis='4_axle_sparse_32px')