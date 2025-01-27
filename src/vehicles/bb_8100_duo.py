from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="bb_8100_duo",
        base_numeric_id=190,
        name="BB 8100 / 9200 (duo)",
        role="ultra_heavy_freight",
        role_child_branch_num=-3,
        power_by_power_source={"DC": 8700},
        speed=75,  # for lolz
        random_reverse=True,
        gen=3,  # spans gen 4 as well
        pantograph_type="diamond-double",
        intro_year_offset=8,  # introduce later than gen epoch by design
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=105, vehicle_length=6, spriterow_num=0, repeat=2
    )

    consist.description = """ """
    consist.foamer_facts = """SNCF BB 8100 / 9200 (duo)"""

    return consist
