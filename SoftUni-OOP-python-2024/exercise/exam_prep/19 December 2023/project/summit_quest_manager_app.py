from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak


class SummitQuestManagerApp:
    CLIMBER_TYPES = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    PEAK_TYPE = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers = []
        self.peaks = []

    def get_climber(self, climber_name):
        mew_climbers = [climber for climber in self.climbers if climber.name == climber_name]
        return mew_climbers[0] if mew_climbers else None

    def get_peaks(self, peak_name):
        new_peaks = [peak for peak in self.peaks if peak.name == peak_name]
        return new_peaks[0] if new_peaks else None

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.CLIMBER_TYPES.keys():
            return f"{climber_type} doesn't exist in our register."

        climber_check = self.get_climber(climber_name)
        if climber_check:
            return f"{climber_name} has been already registered."

        climber = self.CLIMBER_TYPES[climber_type](climber_name)
        self.climbers.append(climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.PEAK_TYPE.keys():
            return f"{peak_type} is an unknown type of peak."

        peak = self.PEAK_TYPE[peak_type](peak_name, peak_elevation)
        self.peaks.append(peak)

        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: list):
        climber = self.get_climber(climber_name)
        peak = self.get_peaks(peak_name)

        required_gear = set(peak.get_recommended_gear())
        missing_gear = required_gear - set(gear)

        if not missing_gear:
            return f"{climber_name} is prepared to climb {peak_name}."
        else:
            climber.is_prepared = False
            sorted_gear = sorted(list(missing_gear))
            return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted_gear)}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self.get_climber(climber_name)
        peak = self.get_peaks(peak_name)

        if not climber:
            return f"Climber {climber_name} is not registered yet."
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."
        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."
        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        result = [f"Total climbed peaks: {len(self.peaks)}\n**Climber's statistics:**"]

        sorted_climbers = sorted([climber for climber in self.climbers if climber.conquered_peaks],
                                 key=lambda c: (-len(c.conquered_peaks), c.name))

        result.append("\n".join(str(climber) for climber in sorted_climbers)) # appending the __str__ methood of each climber in the result

        return "\n".join(result)






