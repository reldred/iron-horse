import global_constants
from train import EngineConsist, SteamLoco, SteamLocoTender

consist = EngineConsist(id = 'standard',
              base_numeric_id = 480,
              title = '4-2-2 Standard [Steam]',
              power = 950,
              tractive_effort_coefficient = 0.07,
              speed = 65,
              type_base_buy_cost_points = 18, # dibble buy cost for game balance
              vehicle_life = 40,
              vehicle_generation = 1)

consist.add_unit(SteamLoco(consist = consist,
                        weight = 62,
                        vehicle_length = 5,
                        spriterow_num = 0))

consist.add_unit(SteamLocoTender(consist = consist,
                        weight = 30,
                        vehicle_length = 3,
                        spriterow_num = 1))

consist.add_model_variant(start_date=0,
                       end_date=global_constants.max_game_date)
