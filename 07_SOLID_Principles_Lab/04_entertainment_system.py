class EntertainmentDevice:
    def connect_device_to_power_outlet(self, device): pass


class ConnectRCA:
    def rca_connect(self, obj):
        pass


class ConnectHDMI:
    def hdmi_connect(self, obj):
        pass


class ConnectEthernet:
    def ethernet_connect(self, obj):
        pass


class Television(EntertainmentDevice, ConnectRCA, ConnectHDMI):
    def connect_to_dvd(self, dvd_player):
        ConnectRCA.rca_connect(self, dvd_player)

    def connect_to_game_console(self, game_console):
        ConnectHDMI.hdmi_connect(self, game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(EntertainmentDevice, ConnectHDMI):
    def connect_to_tv(self, television):
        ConnectHDMI.hdmi_connect(self, television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice, ConnectHDMI, ConnectEthernet):
    def connect_to_tv(self, television):
        ConnectHDMI.hdmi_connect(self, television)

    def connect_to_router(self, router):
        ConnectEthernet.ethernet_connect(self, router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice, ConnectEthernet):
    def connect_to_tv(self, television):
        ConnectEthernet.ethernet_connect(self, television)

    def connect_to_game_console(self, game_console):
        ConnectEthernet.ethernet_connect(self, game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
