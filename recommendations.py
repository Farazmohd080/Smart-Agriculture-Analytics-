def recommend_actions(rainfall, temperature, humidity):
    suggestions = []
    if rainfall < 300:
        suggestions.append("Consider supplemental irrigation for low rainfall.")
    if temperature > 35:
        suggestions.append("Use heat-tolerant crop varieties.")
    if humidity < 30:
        suggestions.append("Consider moisture-retaining mulch.")

    if not suggestions:
        suggestions.append("Conditions look optimal. Maintain current practices.")
    return suggestions
