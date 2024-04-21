from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    RECOMMENDED_GEAR = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def get_recommended_gear(self):
        return self.RECOMMENDED_GEAR

    def calculate_difficulty_level(self):
        if 1500 <= self.elevation <= 2500:
            return "Advanced"
        return "Extreme"
