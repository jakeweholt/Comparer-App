from model import Model
from model.estimators import LevenshteinDistanceEstimator, DiffLibRatioEstimator


class Comparer:

    def __init__(self):
        self.model = Model()
        self.model.pipeline.add_member(LevenshteinDistanceEstimator())
        self.model.pipeline.add_member(DiffLibRatioEstimator())
