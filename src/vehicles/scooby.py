from train import MailEngineRailcarConsist, DieselRailcarUnit

consist = MailEngineRailcarConsist(id='scooby',
                            base_numeric_id=3070,
                            name='Scooby',
                            role='mail_railcar',
                            power=420,
                            speed=75,
                            type_base_running_cost_points=-32,  # dibble running costs for game balance
                            intro_date=1955)  # explicit intro date by design

consist.add_unit(type=DieselRailcarUnit,
                 weight=37,
                 vehicle_length=8,
                 capacity=40,
                 chassis='railcar')

