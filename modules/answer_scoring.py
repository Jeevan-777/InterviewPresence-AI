def score_answer(transcript, keywords):
    """
    Calculates percentage of keyword matches in transcript.
    Returns score between 0–100.
    """

    if not transcript or transcript.strip() == "":
        return 0

    transcript = transcript.lower()

    matches = 0
    for word in keywords:
        if word.lower() in transcript:
            matches += 1

    score = (matches / len(keywords)) * 100
    return round(score, 1)