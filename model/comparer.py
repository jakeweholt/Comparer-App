from model import Model
from model.estimators import LevenshteinEstimator


class Comparer:

    def __init__(self):
        self.model = Model()
        self.model.pipeline.add_member(LevenshteinEstimator())
