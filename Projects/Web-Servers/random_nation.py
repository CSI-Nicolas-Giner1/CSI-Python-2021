from plistlib import UID


class random_nation:
    def __init__(self,id:int,uid:str, nationality:str, language:str, capital:str, national_sport:str, flag: str):
        self.id= id
        self.uid= uid
        self.nationality= nationality
        self.language= language
        self.capital= capital
        self.national_sport= national_sport
        self.flag= flag