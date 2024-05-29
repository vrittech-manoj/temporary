from air_defense_en import AirDefense

air_defense_obj = AirDefense()
air_defense_obj.Radar() #in public we can access .
air_defense_obj._hitTarget() #in protected we can access using obj
# air_defense_obj.__hitTargetBestVersion() #in private we can not access using obj
print(air_defense_obj._rad)

