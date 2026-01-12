import numpy as np

def elo_rating_update(ratings: dict, matches: list, k_factor: float) -> dict:
    """
    Update Elo ratings based on pairwise comparison results.

    Args:
        ratings: Dictionary mapping model names to their current Elo ratings
        matches: List of tuples (model_a, model_b, result) where result is 'a', 'b', or 'draw'
        k_factor: The K-factor controlling rating update magnitude

    Returns:
        Dictionary with updated ratings for all models
    """
    updated_ratings = ratings.copy()
    for model_a, model_b, result in matches:
        rating_a = updated_ratings[model_a]
        rating_b = updated_ratings[model_b]

        # Standard Elo expected score
        expected_a = 1 / (1 + 10 ** ((rating_b - rating_a) / 400))
        expected_b = 1 - expected_a

        # Actual score
        if result == 'a':
            score_a, score_b = 1, 0
        elif result == 'b':
            score_a, score_b = 0, 1
        elif result == 'draw':
            score_a, score_b = 0.5, 0.5
        else:
            raise ValueError("Result must be 'a', 'b', or 'draw'.")

        updated_ratings[model_a] += k_factor * (score_a - expected_a)
        updated_ratings[model_b] += k_factor * (score_b - expected_b)

    return updated_ratings

def main():
    ratings = {'model_a': 1500, 'model_b': 1500}
    matches = [('model_a', 'model_b', 'a')]
    k_factor = 32

    # {'model_a': 1516.0, 'model_b': 1484.0}
    result = elo_rating_update({'model_a': 1600, 'model_b': 1400}, [('model_a', 'model_b', 'b')], 32)
    print(result)

if __name__ == '__main__':
    main()

