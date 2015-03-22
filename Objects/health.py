__author__ = 'Ingus Mat Burleson'

class Health(object):

    def wounded(self, damage = 1):
        try:
            self.hit_points -= damage
        except:
            print("{} is not damagable.".format(self))

    def rest(self):
        try:
            if self.hitpoints < self.base_hit_points:
                self.hit_points += 1
        except:
            print("{} does not sleep.".format(self))
