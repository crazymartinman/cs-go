from random import randint
gun =(randint(1, 9))

class GunInfo:
    def __init__(self, name, price, mag_capacity, side, kill_award, damage, headshot):
        self.name = name
        self.price = price
        self.mag_capacity = mag_capacity
        self.side = side
        self.kill_award = kill_award
        self.damage = damage
        self.headshot = headshot

    def printInfo(self):
        print 'Gun Name: ' + self.name
        print 'Gun Price: ' , self.price
        print 'Gun Mag Capacity: ' + self.mag_capacity
        print 'Gun Side: ' + self.side
        print 'Gun Kill Award: ' , self.kill_award
        print 'Gun Damage: ' ,  self.damage
        print 'Gun Headshot: ' + self.headshot


def main():
    ak = GunInfo("The AK-47", 2700.00, "30 / 90", "Terrorist", 300.00, 36.00, "One shot")
    ak.printInfo()
    #aug = GunInfo ("The AUG", 3150 )

main();
