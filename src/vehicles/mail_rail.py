from train import MailEngineRailcarConsist, DieselRailcarUnit

consist = MailEngineRailcarConsist(id='mail_rail',
                                   base_numeric_id=3000,
                                   name='Mail Rail',
                                   role='mail_railcar',
                                   power=700,
                                   # matched to fast (in this gen) freight speeds
                                   type_base_running_cost_points=-32,  # dibble running costs for game balance
                                   gen=6,
                                   intro_date_offset=-5)  # introduce early by design

consist.add_unit(type=DieselRailcarUnit,
                 weight=37,
                 vehicle_length=8,
                 capacity=40,
                 chassis='railcar')
