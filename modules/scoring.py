def calculate_score(face, eye, speech, silence_duration, total_duration):
    
    silence_percent = (silence_duration / total_duration) * 100
    silence_score = max(0, 100 - silence_percent)

    final_score = (
        0.25 * face +
        0.25 * eye +
        0.30 * speech +
        0.20 * silence_score
    )

    return round(final_score, 2)
