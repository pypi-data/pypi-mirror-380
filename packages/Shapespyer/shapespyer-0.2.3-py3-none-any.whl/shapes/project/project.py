import logging
import sys

from shapes.project.analysis import Analysis
from shapes.project.sample_model import SampleModels


class Project:
    def __init__(self):
        self.title = None
        self.description = None
        self.sample_models = SampleModels()
        self.analysis = Analysis()

    def save(self):
        raise NotImplementedError

    def save_as(self):
        raise NotImplementedError

    @property
    def summary(self):
        return Summary(self)


class Summary:
    def __init__(self, project):
        raise NotImplementedError

    def show_report(self):
        raise NotImplementedError
