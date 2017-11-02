#!/usr/bin/env
"""
Behaviour patterns
    Strategy design patterns
"""
import abc


class Soldier(object):

    def refill_interface(self, refill_obj):
        refill_obj.refill()

    def repair_interface(self, repair_obj):
        repair_obj.repair()

    def attach(self):
        print('Go to attack')

    def gather(self):
        print('Gathering')


class RefillStrategy(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def refill(self):
        pass


class NoRefill(RefillStrategy):

    def refill(self):
        print('Refilling Not Required')


class WeaponRefill(RefillStrategy):

    def refill(self):
        print('Weapon Refilling Required')


class TimeRefill(RefillStrategy):

    def refill(self):
        print('Time Refilling Required')


class RepairStrategy(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def repair(self):
        pass


class NoRepair(RepairStrategy):

    def repair(self):
        print('Repairing not Required')


class InternalRepair(RepairStrategy):

    def repair(self):
        print('Internal Repairing Required')


class ExternalRepair(object):

    def repair(self):
        print('External Repairing Required')


class Gunman(Soldier):

    def __init__(self, repair_strategy, refill_strategy):
        # Repairing strategy
        self.repair_strategy = repair_strategy
        self.repair_interface(self.repair_strategy)

        # Refilling strategy
        self.refill_strategy = refill_strategy
        self.refill_interface(self.refill_strategy)


class Robot(Soldier):

    def __init__(self, repair_strategy, refill_strategy):
        # Repairing strategy
        self.repair_strategy = repair_strategy
        self.repair_interface(self.repair_strategy)

        # Refilling strategy
        self.refill_strategy = refill_strategy
        self.refill_interface(self.refill_strategy)


if __name__ == '__main__':
    print('----------------Gunman Here-----------------')
    repair_strategy = InternalRepair()
    refill_strategy = WeaponRefill()
    Gunman(repair_strategy, refill_strategy)

    print('----------------Robot Here-----------------')
    repair_strategy = ExternalRepair()
    refill_strategy = TimeRefill()
    Robot(repair_strategy, refill_strategy)
