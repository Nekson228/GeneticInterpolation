from typing import TypedDict

SettingsData = TypedDict('SettingsData', {
    'f(x)': list[float],
    'steps_amount': int,
    'left_bound': float,
    'right_bound': float,
})
