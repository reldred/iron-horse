from train import EngineConsist, ElectricEngineUnit


def main(roster_id):
    consist = EngineConsist(
        roster_id=roster_id,
        id="re_420",
        base_numeric_id=8930,
        name="Re 420 (Re 4/4ii)",
        role="ultra_heavy_freight",
        role_child_branch_num=-1,
        power=6700,
        random_reverse=True,
        gen=5,
        pantograph_type="diamond-double",
        # intro_year_offset=5,  # introduce later than gen epoch by design
        force_default_pax_mail_livery=2,  # pax/mail cars default to second livery with this engine
        default_livery_extra_docs_examples=[
            ("COLOUR_LIGHT_BLUE", "COLOUR_WHITE"),
            ("COLOUR_PALE_GREEN", "COLOUR_WHITE"),
            ("COLOUR_DARK_GREEN", "COLOUR_WHITE"),
            ("COLOUR_BLUE", "COLOUR_BLUE"),
        ],
        sprites_complete=False,
    )

    consist.add_unit(
        type=ElectricEngineUnit, weight=105, vehicle_length=8, spriterow_num=0
    )

    consist.description = """ """
    consist.foamer_facts = """SBB Re 420 (Re 4/4<sup>ii</sup>)"""

    return consist