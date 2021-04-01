class player:
    DATA_OWN, PLAYER, AID_SERVER = [0,1,2]
    mapping = {
        "data_own":0,
        "players":1,
        "aid_server":2
        }
    def __init__(self, config):
        self._player_name = config["player_name"]
        self._config = config["service"][self.player_name]
        self._host = self.config["host"]
        self._pk = self.config["pk"]
        self._alias = config["alias"]
    @property
    def player_name(self):
        return self._player_name

    @property
    def config(self):
        return self._config
    
    @property
    def host(self):
        return self._host
    
    @property
    def pk(self):
        return self._pk

    @property
    def alias(self):
        return self._alias
    
    def check(self, player_name):
        return self.player_name == player_name
    
    def __repr__(self):
        return str({
            "name":self.player_name,
            "host":self.host
        })


import toml
player = 

if __name__ == "__main__":
    p = player(toml.load('../config.toml')) 
    print(p)
