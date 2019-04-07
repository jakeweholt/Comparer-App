from model import Model
from model.estimators import DiffLibRatioEstimator


class Matcher:

    def __init__(self):
        self.model = Model()
        self.model.pipeline.add_member(DiffLibRatioEstimator())
