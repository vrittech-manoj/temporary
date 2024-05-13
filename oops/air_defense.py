#track un-identified object
#Iron Dom (isareal) air defense system

class AirDefense:

    def radar(self):
        self.angel=45
        self.speed=1200
        self.distance=230
        return True,{"angel":self.angel,"speed":self.speed,"distance":self.distance}
    
    def defense(self):
        print("*********ALERT!!!*********")
        print(f"Enemy detected at angel {self.angel} with speed  {self.speed}km/hr at distance {self.distance}km/hr ")

        target_position = self.calculateTargetPosition()
        print(f" target position found !!! at angel {target_position[0]} longitude {target_position[1]} and alt {target_position[2]} " )
        self.rocket_luncher(target_position)
    
    def calculateTargetPosition(self):
        #calculate target position acc. to  physics law where input data is self.angel=45, self.speed=1200,self.distance=230
        longt = "12.32.34"
        alt="34.23.354"
        return 35,longt,alt
    
    def rocket_luncher(self,target_position):
        print("Congrats!!! it hit enemy target position.",target_position)


air_defense_obj = AirDefense()
is_enemy_detected = air_defense_obj.radar()

if is_enemy_detected[0] == True:
    air_defense_obj.defense()
    

#Tesla car autmatic driving system
    
TeslaCAr("Kathmanduu")
    object_detect()
    break_car,turn_car





    
