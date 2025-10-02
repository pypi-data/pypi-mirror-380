class Analyses:
    def new(self):
        raise NotImplementedError


class Analysis:
    def __init__(self):
        self.force_field = None
        self.force_fields = None
        self.configuration = ""
        self.configurations = None
        self.steps = 1
        self.post_processors = None

    def equilibrate(self, name: str):
        raise NotImplementedError

    def show_radius_of_gyration(self, name: str):
        raise NotImplementedError


class AnalysisConfigurations:
    def add(self):
        raise NotImplementedError


class AnalysisConfiguration:
    def __init__(self):
        self.name = None
        self.parameters = None

    def load_from_file(self, file_path: str):
        raise NotImplementedError


class ForceFields:
    def add(self):
        raise NotImplementedError


class ForceField:
    def __init__(self):
        self.name = None
        self.file_path = None
