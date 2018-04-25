from train import EngineConsist, SteamEngineUnit

consist = EngineConsist(id='express_tank',
                        base_numeric_id=1300,
                        name='2-6-2 Express Tank',
                        role='branch',
                        power=800,
                        tractive_effort_coefficient=0.2,
                        speed=90,
                        type_base_buy_cost_points=-2,  # dibble buy cost for game balance
                        type_base_running_cost_points=-6,  # dibble running costs for game balance
                        random_reverse=True,
                        gen=3)

consist.add_unit(type=SteamEngineUnit,
                 weight=57,
                 vehicle_length=6,
                 spriterow_num=0)

