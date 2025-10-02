import uuid
from collections import defaultdict
from typing import Optional

from shapes.project.files import FileManager


class BaseItem:
    def __init__(self, name: Optional[str] = None):
        super().__init__()
        if name is None:
            self.name = str(uuid.uuid1())[-12:]
        else:
            self.name = name

    def __str__(self):
        return f"{self.__class__.__name__}({self.name})"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other) -> bool:
        return isinstance(self, type(other)) and self.name == other.name

    def load_from_library(self):
        return self


class Component(BaseItem):
    def __init__(self, *args):
        super().__init__(*args)
        self.structure_file_path = ""
        self.topology_file_path = ""
        component_data = FileManager().locate_component(
            self.__class__.__name__, self.name
        )
        if component_data[0]:
            self.structure_file_path = component_data[0]
        if component_data[1]:
            self.topology_file_path = component_data[1]

    def show(self):
        raise NotImplementedError


class Ion(Component):
    def __init__(self, *args):
        super().__init__(*args)
        self.amount = 0

    def __str__(self):
        return f"{self.amount} {super().__str__()}"

    def __repr__(self):
        return str(self)


class Lipid(Component):
    pass


class Surfactant(Component):
    pass


class BaseCollection:
    def __init__(self):
        self._items = []
        self._name_map = {}
        self._references = defaultdict(list)

    def __str__(self):
        return f"{self.__class__.__name__}: {self._items}"

    def __repr__(self):
        return f"{self.__class__.__name__}: {self._items}"

    def __iter__(self):
        self._cursor = 0
        return self

    def __len__(self):
        return len(self._items)

    def __next__(self):
        if self._cursor >= len(self._items):
            raise StopIteration
        item_at_cursor = self._items[self._cursor]
        self._cursor += 1
        return item_at_cursor

    def __getitem__(self, idx):
        if isinstance(idx, str):
            idx = self._name_map[idx]
        return self._items[idx]

    def _find(self, idx):
        name = ""
        if isinstance(idx, int):
            name = self._items[idx].name
        if isinstance(idx, str):
            name = idx
            idx = self._name_map[name]

        return idx, name

    def _reset_name_map(self):
        new_map = {}
        for idx, item in enumerate(self._items):
            new_map[item.name] = idx
        self._name_map = new_map

    def __delitem__(self, idx):
        idx, name = self._find(idx)
        if name in self._name_map:
            del self._name_map[name]
        if idx < len(self._items) and idx >= 0:
            del self._items[idx]
        referenced_in = self._references[name]
        for ref_holder, ref_key in referenced_in:
            del ref_holder[ref_key]

    def __setitem__(self, idx, value):
        idx, name = self._find(idx)

        del self._name_map[name]

        self._items[idx] = value
        self._name_map[value.name] = idx

    def append(self, value):
        idx = len(self._items)
        self._items.append(value)
        self._name_map[value.name] = idx

    def insert(self, idx, value):
        self._items.insert(idx, value)
        self._reset_name_map()

    def add_reference(self, ref_holder, ref_key, item):
        self._references[item.name].append((ref_holder, ref_key))

    def pop(self, value=None):
        raise NotImplementedError


class Components(BaseCollection):
    def __init__(self):
        super().__init__()
        self._items: list[Component] = []


class Ions(BaseCollection):
    def __init__(self):
        super().__init__()
        self._items: list[Ion] = []


class Solution:
    def __init__(self, *args, **kwargs):
        self.ions = Ions()
        for arg in args:
            if isinstance(arg, Ion):
                self.ions.append(arg)
