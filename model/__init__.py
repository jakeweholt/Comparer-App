# Models consist of Pipelines, Pipelines are built with Members.

from abc import ABC, abstractmethod


class Member(ABC):

    def __init__(self):
        super().__init__()
        pass

    @abstractmethod
    def run(self):
        pass


class Pipeline:

    def __init__(self):
        self.members = list()

    def add_member(self, new_member):
        self.members.append(new_member)


class Model:

    def __init__(self):
        self.pipeline = Pipeline()

    def run_pipeline(self, a, b):
        outputs = {}
        for member in self.pipeline.members:
            member.run(a, b)
            outputs[member.name] = member.output
        return(outputs)
