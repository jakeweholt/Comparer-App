from leven import levenshtein
from model import Member


class LevenshteinEstimator(Member):

    def __init__(self):
        self.name = 'levenshtein_similarity'
        self.output = None

    def run(self, a, b):
        self.output = levenshtein(a, b)
