from train import EngineConsist, DieselEngineUnit

consist = EngineConsist(id='hippo',
                        base_numeric_id=1870,
                        name='Hippo',
                        power=3600,
                        track_type='NG',
                        intro_date=1975)

consist.add_unit(type=DieselEngineUnit,
                 weight=130,
                 vehicle_length=8,
                 spriterow_num=0)
