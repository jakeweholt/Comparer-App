from Levenshtein import distance
import difflib

from model import Member

def string_cleaner(input_string):
    return(input_string.lower().replace(' ',''))


class LevenshteinDistanceEstimator(Member):

    def __init__(self):
        self.name = 'levenshtein_distance'
        self.output = None

    def run(self, a, b):
        try:
            self.output = distance(string_cleaner(a), string_cleaner(b))
        except:
            self.output = 'Error'


class DiffLibRatioEstimator(Member):

    def __init__(self):
        self.name = 'similarity_probability'
        self.output = None

    def run(self, a, b):
        try:
            self.output = difflib.SequenceMatcher(None, string_cleaner(a), string_cleaner(b)).ratio()
        except:
            self.output = 'Error'