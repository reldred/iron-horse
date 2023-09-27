from train import TankCarProductConsist, FreightCar


def main():
    # --------------- pony ----------------------------------------------------------------------

    consist = TankCarProductConsist(
        roster_id="pony",
        base_numeric_id=8860,
        gen=2,
        subtype="A",
        intro_year_offset=-10,  # let's be earlier for this one
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_filled_16px")

    consist = TankCarProductConsist(
        roster_id="pony",
        base_numeric_id=12400,
        gen=3,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="3_axle_filled_16px")

    consist = TankCarProductConsist(
        roster_id="pony",
        base_numeric_id=10930,
        gen=3,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_24px")

    consist = TankCarProductConsist(
        roster_id="pony",
        base_numeric_id=17960,
        gen=3,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_gapped_32px")

    consist = TankCarProductConsist(
        roster_id="pony",
        base_numeric_id=12420,
        gen=4,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = TankCarProductConsist(
        roster_id="pony",
        base_numeric_id=17370,
        gen=4,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = TankCarProductConsist(
        roster_id="pony",
        base_numeric_id=12440,
        gen=4,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")

    consist = TankCarProductConsist(
        roster_id="pony",
        base_numeric_id=16950,
        gen=5,
        subtype="A",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="2_axle_sparse_16px")

    consist = TankCarProductConsist(
        roster_id="pony",
        base_numeric_id=17060,
        gen=5,
        subtype="B",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_24px")

    consist = TankCarProductConsist(
        roster_id="pony",
        base_numeric_id=12470,
        gen=5,
        subtype="C",
        sprites_complete=True,
    )

    consist.add_unit(type=FreightCar, chassis="4_axle_sparse_32px")
