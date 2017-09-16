import global_constants
from train import MailConsistShort, MailConsistLong, MailCar

def main():
    #--------------- pony ----------------------------------------------------------------------
    consist = MailConsistShort(title = '[Mail Car] Short',
                               roster = 'pony',
                               base_numeric_id = 2220,
                               wagon_generation = 1,
                               intro_date = 1860,
                               vehicle_life = 40,
                               speedy = True)

    consist.add_unit(MailCar(consist = consist,
                             capacity_mail = 15,
                             weight = 15,
                             vehicle_length = 4))

    consist.add_model_variant(intro_date = 0,
                              end_date=global_constants.max_game_date)


    consist = MailConsistLong(title = '[Mail Car] Long',
                              roster = 'pony',
                              base_numeric_id = 920,
                              wagon_generation = 2,
                              intro_date = 1900,
                              vehicle_life = 40,
                              speedy = True)

    consist.add_unit(MailCar(consist = consist,
                             capacity_mail = 25,
                             weight = 29,
                             vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)


    consist = MailConsistLong(title = '[Mail Car] Long',
                              roster = 'pony',
                              base_numeric_id = 940,
                              wagon_generation = 3,
                              intro_date = 1960,
                              vehicle_life = 40,
                              speedy = True)

    consist.add_unit(MailCar(consist = consist,
                             capacity_mail = 40,
                             weight = 31,
                             vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)


    consist = MailConsistLong(title = '[Mail Car] Long',
                              roster = 'pony',
                              base_numeric_id = 950,
                              wagon_generation = 1,
                              intro_date = 1860,
                              vehicle_life = 40,
                              track_type = 'NG')

    consist.add_unit(MailCar(consist = consist,
                             capacity_mail = 24,
                             weight = 5,
                             vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                              end_date=global_constants.max_game_date)

    """
    #--------------- llama ----------------------------------------------------------------------
    consist = MailConsistLong(title = '[Mail Car] Long',
                          roster = 'llama',
                          base_numeric_id = 960,
                          wagon_generation = 1,
                          intro_date = 1860,
                          vehicle_life = 40,
                          speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 30,
                            weight = 29,
                            vehicle_length = 7))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsistLong(title = '[Mail Car] Long',
                          roster = 'llama',
                          base_numeric_id = 970,
                          wagon_generation = 2,
                          intro_date = 1920,
                          vehicle_life = 40,
                          speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 45,
                            weight = 30,
                            vehicle_length = 7))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsistLong(title = '[Mail Car] Long',
                          roster = 'llama',
                          base_numeric_id = 980,
                          wagon_generation = 3,
                          intro_date = 1980,
                          vehicle_life = 40,
                          speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 60,
                            weight = 31,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsistLong(title = '[Mail Car] Long',
                          roster = 'llama',
                          base_numeric_id = 990,
                          wagon_generation = 1,
                          intro_date = 1860,
                          speedy = True,
                          track_type = 'NG',
                          vehicle_life = 40)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 30,
                            weight = 12,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsistLong(title = '[Mail Car] Long',
                          roster = 'llama',
                          base_numeric_id = 1380,
                          wagon_generation = 2,
                          intro_date = 1920,
                          speedy = True,
                          track_type = 'NG',
                          vehicle_life = 40)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 40,
                            weight = 20,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsistLong(title = '[Mail Car] Long',
                          roster = 'llama',
                          base_numeric_id = 1450,
                          wagon_generation = 3,
                          intro_date = 1980,
                          speedy = True,
                          track_type = 'NG',
                          vehicle_life = 40)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 50,
                            weight = 20,
                            vehicle_length = 6))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)

    """
    #--------------- antelope ----------------------------------------------------------------------
    consist = MailConsistLong(title = '[Mail Car] Long',
                          roster = 'antelope',
                          base_numeric_id = 1730,
                          wagon_generation = 1,
                          intro_date = 1950,
                          vehicle_life = 40,
                          speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 40,
                            weight = 32,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsistLong(title = '[Mail Car] Long',
                          roster = 'antelope',
                          base_numeric_id = 2120,
                          wagon_generation = 1,
                          intro_date = 1860,
                          vehicle_life = 40,
                          track_type = 'NG',
                          speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 20,
                            weight = 14,
                            vehicle_length = 5))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)


    consist = MailConsistLong(title = '[Mail Car] Long',
                          roster = 'antelope',
                          base_numeric_id = 1950,
                          wagon_generation = 2,
                          intro_date = 1915,
                          vehicle_life = 40,
                          track_type = 'NG',
                          speedy = True)

    consist.add_unit(MailCar(consist = consist,
                            capacity_mail = 30,
                            weight = 22,
                            vehicle_length = 8))

    consist.add_model_variant(intro_date=0,
                           end_date=global_constants.max_game_date)
