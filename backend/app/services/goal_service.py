from decimal import Decimal, ROUND_HALF_UP

from app.models.enums import ActivityLevel, DeficitLevel, GoalType, Sex

ACTIVITY_MULTIPLIERS = {
    ActivityLevel.SEDENTARY: Decimal("1.20"),
    ActivityLevel.LIGHT: Decimal("1.375"),
    ActivityLevel.MODERATE: Decimal("1.55"),
    ActivityLevel.ACTIVE: Decimal("1.725"),
    ActivityLevel.VERY_ACTIVE: Decimal("1.90"),
}

PROTEIN_MULTIPLIERS = {
    GoalType.LOSE_FAT: Decimal("2.00"),
    GoalType.MAINTAIN: Decimal("1.80"),
    GoalType.GAIN_MASS: Decimal("1.80"),
}

FAT_MULTIPLIER = Decimal("0.80")

DEFICIT_ADJUSTMENTS = {
    DeficitLevel.LIGHT: Decimal("300"),
    DeficitLevel.MEDIUM: Decimal("500"),
    DeficitLevel.AGGRESSIVE: Decimal("700"),
}

SURPLUS_BY_GOAL = {
    GoalType.GAIN_MASS: Decimal("250"),
}


def calculate_targets(*, sex: Sex, age: int, height_cm: Decimal, weight_kg: Decimal, activity_level: ActivityLevel, goal_type: GoalType, deficit_level: DeficitLevel) -> dict[str, Decimal]:
    maintenance_calories = calculate_maintenance_calories(
        sex=sex,
        age=age,
        height_cm=height_cm,
        weight_kg=weight_kg,
        activity_level=activity_level,
    )
    target_calories = adjust_calories(
        maintenance_calories=maintenance_calories,
        goal_type=goal_type,
        deficit_level=deficit_level,
    )
    target_protein = quantize(weight_kg * PROTEIN_MULTIPLIERS[goal_type])
    target_fat = quantize(weight_kg * FAT_MULTIPLIER)
    protein_calories = target_protein * Decimal("4")
    fat_calories = target_fat * Decimal("9")
    remaining_calories = max(target_calories - protein_calories - fat_calories, Decimal("0"))
    target_carbs = quantize(remaining_calories / Decimal("4"))

    return {
        "maintenance_calories": maintenance_calories,
        "target_calories": target_calories,
        "target_protein": target_protein,
        "target_carbs": target_carbs,
        "target_fat": target_fat,
    }


def calculate_maintenance_calories(*, sex: Sex, age: int, height_cm: Decimal, weight_kg: Decimal, activity_level: ActivityLevel) -> Decimal:
    if sex == Sex.MALE:
        bmr = Decimal("10") * weight_kg + Decimal("6.25") * height_cm - Decimal("5") * Decimal(age) + Decimal("5")
    else:
        bmr = Decimal("10") * weight_kg + Decimal("6.25") * height_cm - Decimal("5") * Decimal(age) - Decimal("161")

    return quantize(bmr * ACTIVITY_MULTIPLIERS[activity_level])


def adjust_calories(*, maintenance_calories: Decimal, goal_type: GoalType, deficit_level: DeficitLevel) -> Decimal:
    if goal_type == GoalType.LOSE_FAT:
        return quantize(max(maintenance_calories - DEFICIT_ADJUSTMENTS[deficit_level], Decimal("1200")))
    if goal_type == GoalType.GAIN_MASS:
        return quantize(maintenance_calories + SURPLUS_BY_GOAL[goal_type])
    return quantize(maintenance_calories)


def quantize(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
