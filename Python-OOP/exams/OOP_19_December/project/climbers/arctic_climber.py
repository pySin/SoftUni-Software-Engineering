from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self):
        if self.strength >= 100:
            return True
        return False

    def climb(self, peak: BasePeak):
        before_climb_strength = self.strength
        if peak.difficulty_level == "Extreme":
            self.strength = float(self.strength - (20 * 2))
        else:
            self.strength = float(self.strength - (20 * 1.5))

        if self.can_climb():
            self.conquered_peaks.append(peak.name)
        else:
            self.strength = before_climb_strength
