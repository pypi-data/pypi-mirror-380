from __future__ import annotations

from typing import TYPE_CHECKING

from edc_constants.constants import (
    ABSENT,
    DECREASED,
    NO,
    PRESENT,
    PRESENT_WITH_REINFORCEMENT,
    REDUCED,
    YES,
)

if TYPE_CHECKING:
    from edc_mnsi.model_mixins import MnsiModelMixin


class MnsiPatientHistoryCalculatorError(Exception):
    pass


class MnsiPhysicalAssessmentCalculatorError(Exception):
    pass


class MnsiCalculator:
    """Michigan Neuropathy Screening Instrument (MNSI) calculators."""

    def __init__(self, model_obj: MnsiModelMixin | None = None, **kwargs):
        if model_obj:
            self.responses = model_obj.__dict__
        else:
            self.responses = kwargs

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(responses={self.responses})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(responses={self.responses})"

    def patient_history_score(self) -> int:
        """Returns MNSI score based on patient history questionnaire.

        Scoring based on:
            https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3641573/#S6title
        """
        try:
            # 1 point added for each 'YES' response for following Qs
            score = [
                self.responses["numb_legs_feet"],  # Q1
                self.responses["burning_pain_legs_feet"],  # Q2
                self.responses["feet_sensitive_touch"],  # Q3
                self.responses["prickling_feelings_legs_feet"],  # Q5
                self.responses["covers_touch_skin_painful"],  # Q6
                self.responses["open_sore_foot_history"],  # Q8
                self.responses["diabetic_neuropathy"],  # Q9
                self.responses["symptoms_worse_night"],  # Q11
                self.responses["legs_hurt_when_walk"],  # Q12
                self.responses["skin_cracks_open_feet"],  # Q14
                self.responses["amputation"],  # Q15
            ].count(YES)

            # 1 point added for each 'NO' response for following Qs
            score += [
                self.responses["differentiate_hot_cold_water"],  # Q7
                self.responses["sense_feet_when_walk"],  # Q13
            ].count(NO)

            # Note: Questions 4 (muscle_cramps_legs_feet) and 10 (feel_weak)
            # not included in scoring algorithm

        except KeyError as exc:
            raise MnsiPatientHistoryCalculatorError(
                f"Can't calculate patient history score for MNSI. "
                f"Expected response '{exc.args[0]}' "
                f"was missing from received responses: {self.responses.keys()}. "
                "Perhaps catch this in the form validation."
            ) from exc
        return score

    def physical_assessment_score(self) -> float:
        """Returns score based on lower extremity examination.

        Scoring based on:
            https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3641573/#S6title
            (plus up to 2 extra points awarded for monofilament assessments)
        """
        score = 0.0
        try:
            for foot_choice in ["left", "right"]:
                score += self._get_appearance_points(
                    self.responses[f"normal_appearance_{foot_choice}_foot"]
                )
                score += self._get_ulceration_points(
                    self.responses[f"ulceration_{foot_choice}_foot"]
                )
                score += self._get_ankle_reflex_points(
                    self.responses[f"ankle_reflexes_{foot_choice}_foot"]
                )
                score += self._get_vibration_perception_points(
                    self.responses[f"vibration_perception_{foot_choice}_toe"]
                )
                score += self._get_monofilament_points(
                    self.responses[f"monofilament_{foot_choice}_foot"]
                )
        except KeyError as exc:
            raise MnsiPhysicalAssessmentCalculatorError(
                f"Can't calculate physical assessment score for MNSI. "
                f"Expected response '{exc.args[0]}' "
                f"was missing from received responses: {self.responses.keys()}. "
                "Perhaps catch this in the form validation."
            ) from exc
        return score

    @staticmethod
    def _get_appearance_points(response: str) -> int:
        return 1 if response == NO else 0

    @staticmethod
    def _get_ulceration_points(response: str) -> int:
        return 1 if response == PRESENT else 0

    @staticmethod
    def _get_ankle_reflex_points(response: str) -> float:
        if response == PRESENT_WITH_REINFORCEMENT:
            return 0.5
        if response == ABSENT:
            return 1.0
        return 0.0

    @staticmethod
    def _get_vibration_perception_points(response: str) -> float:
        if response == DECREASED:
            return 0.5
        if response == ABSENT:
            return 1.0
        return 0.0

    @staticmethod
    def _get_monofilament_points(response: str) -> float:
        if response == REDUCED:
            return 0.5
        if response == ABSENT:
            return 1.0
        return 0.0
