import difflib
import pandas as pd
from typing import List


def string_cleaner(input_string: str) -> str:
    return input_string.lower().replace(' ', '')


def get_most_likely_value(dirty: str,
                          clean: List[str]) -> (str, str, float):
    scores = dict()
    for c in clean:
        scores[c] = difflib.SequenceMatcher(None,
                                            string_cleaner(c),
                                            string_cleaner(dirty)).ratio()
    most_likely_value = max(scores, key=lambda x: scores.get(x))
    return dirty, most_likely_value, scores[most_likely_value]


class MapperDataIn():

    def __init__(self,
                 clean_data: List[str],
                 dirty_data: List[str]):
        self.clean_data = clean_data
        self.dirty_data = dirty_data


class AtomicMappedData():

    def __init__(self,
                 clean_data_string: str,
                 dirty_data_string: str,
                 score: float):
        self.clean_data_string = clean_data_string
        self.dirty_data_string = dirty_data_string
        self.score = score


class StringMapper():

    def __init__(self, mapper_data_in: MapperDataIn):
        self.mapper_data_in = mapper_data_in
        self.mapped_data = dict()

        for c in mapper_data_in.clean_data:
            self.mapped_data[c] = list()

    def map(self):
        for dirty in self.mapper_data_in.dirty_data:
            dirty_return, clean_return, score_return = get_most_likely_value(
                dirty, self.mapper_data_in.clean_data)
            self.mapped_data[clean_return].append(AtomicMappedData(
                clean_return, dirty_return, score_return))


class StringReducer():

    def __init__(self, string_mapper: StringMapper):
        self.string_mapper = string_mapper
        self.dataframe_output = pd.DataFrame()

    def reduce(self):
        for x in self.string_mapper.mapped_data:
            for mapped in self.string_mapper.mapped_data[x]:
                self.dataframe_output = self.dataframe_output.append(
                    pd.DataFrame({
                        'dirty_data_string': mapped.dirty_data_string,
                        'clean_data_string': mapped.clean_data_string,
                        'score': mapped.score
                    }, index=[0]))
        self.dataframe_output = self.dataframe_output.reset_index(drop=True)

# t = MapperDataIn(clean_data_map, dirty_data)
# m = StringMapper(t)
# m.map()
# sr = StringReducer(m)
# sr.reduce()