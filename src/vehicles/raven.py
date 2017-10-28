from train import EngineConsist, ElectricLoco

consist = EngineConsist(id='raven',
                        base_numeric_id=390,
                        title='Raven [Electric]',
                        power=1800,
                        tractive_effort_coefficient=0.25,
                        speed=80,
                        buy_cost=77,
                        intro_date=1905)  # explicit intro date by design

consist.add_unit(type=ElectricLoco,
                 weight=90,
                 vehicle_length=8,
                 spriterow_num=0)

consist.add_model_variant(spritesheet_suffix=0)
