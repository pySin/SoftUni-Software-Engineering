from project.climbers.base_climber import BaseClimber
# from project.peaks.arctic_peak import ArcticPeak
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self):
        if self.strength >= 75:
            return True
        return False

    def climb(self, peak: BasePeak):
        if self.can_climb():
            self.conquered_peaks.append(peak.name)
        # before_climb_strength = self.strength
        if peak.difficulty_level == "Advanced":
            self.strength = float(self.strength - (30 * 1.3))
        else:
            self.strength = float(self.strength - (30 * 2.5))

        # else:
        #     self.strength = before_climb_strength


# sc = SummitClimber("Frank")
# p = ArcticPeak("K2", 4500)
# sc.climb(p)
# print(sc.conquered_peaks)
# print(sc.strength)
