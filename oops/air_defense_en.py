class Radar:
    def __init__(self) -> None:
        self._rad = 34

    def  _display(self):
        print("this is radar. ")

class AirDefense(Radar):
    def __init__(self) -> None:
        self.__radar_password = "1223434"
        Radar.__init__(self)

    def Radar(self):
        print("you are accessing radar. congrats .")
        return "234.3445"
    
    def _hitTarget(self):
        self.__hitTargetBestVersion()
        print("lunched the target ")

    def __hitTargetBestVersion(self):
        print("lunched the target ")

#Difference between public,private and protected with example