from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    def __init__(self, name, elevation):
        super().__init__(name, elevation)

    def get_recommended_gear(self):
        return ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def calculate_difficulty_level(self):
        level = ""
        if self.elevation > 3000:
            level = "Extreme"
        elif 2000 <= self.elevation <= 3000:
            level = "Advanced"

        return level

