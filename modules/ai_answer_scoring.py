from sentence_transformers import SentenceTransformer, util

# Load model once (fast after first run)
model = SentenceTransformer('all-MiniLM-L6-v2')


def semantic_score(transcript, reference_answer):
    """
    Returns score (0-100) based on semantic similarity
    """

    if not transcript or transcript.strip() == "":
        return 0

    embeddings = model.encode(
        [transcript, reference_answer],
        convert_to_tensor=True
    )

    similarity = util.cos_sim(
        embeddings[0],
        embeddings[1]
    ).item()

    score = max(0, similarity) * 100
    return round(score, 1)