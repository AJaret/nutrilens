from enum import StrEnum


class Sex(StrEnum):
    MALE = "male"
    FEMALE = "female"


class ActivityLevel(StrEnum):
    SEDENTARY = "sedentary"
    LIGHT = "light"
    MODERATE = "moderate"
    ACTIVE = "active"
    VERY_ACTIVE = "very_active"


class GoalType(StrEnum):
    LOSE_FAT = "lose_fat"
    MAINTAIN = "maintain"
    GAIN_MASS = "gain_mass"


class DeficitLevel(StrEnum):
    LIGHT = "light"
    MEDIUM = "medium"
    AGGRESSIVE = "aggressive"


class MealType(StrEnum):
    BREAKFAST = "breakfast"
    LUNCH = "lunch"
    DINNER = "dinner"
    SNACK = "snack"
