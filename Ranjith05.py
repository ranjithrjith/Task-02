class TVClass:
    def __init__(self, brand, channel=1, price=0, inches=0, OnOFF=False, volume=50):
        self.brand = brand
        self.channel = channel
        self.price = price
        self.inches = inches
        self.OnOFF = OnOFF
        self.volume = volume

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_TV(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"

# Derived classes for specific types of TVs can be created based on this base class.