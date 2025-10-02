from scripts.bash_cli import gmx_add_ions_solv
from shapes.basics.options import InputOptions, Options, OutputOptions
from shapes.basics.utils import Generator
from shapes.project.core import BaseCollection, BaseItem, Component, Components
from shapes.project.files import FileManager


class Layer(BaseItem):
    DEFAULT_FRACTION = 100

    def __init__(self, components: Components, idx):
        super().__init__(idx)
        self._fractions = {}
        self.fractions = components

    def __str__(self):
        return f"Layer {self.name}: {self.fractions}"

    def __repr__(self):
        return str(self)

    def add_component(self, component: Component):
        self.fractions[component] = 100

    def remove_component(self, name: str):
        del self.fractions[name]

    @property
    def fractions(self):
        return self._fractions

    @fractions.setter
    def fractions(self, values):
        self._fractions = {}
        for value in values:
            if isinstance(value, Component):
                value = value.name
            self._fractions[value] = self.DEFAULT_FRACTION


class Layers(BaseCollection):
    # TODO typhint it's a collection of `Layer`
    def __init__(self, components: Components):
        super().__init__()
        self._components = components

    def add(self, amount=None):
        if amount is None:
            amount = 1
        for _ in range(amount):
            self.append(Layer(self._components, str(len(self))))

    def add_component_to_all(self, component: Component):
        for item in self._items:
            item.add_component(component)

    def remove_from_each(self, component: Component):
        for item in self._items:
            item.remove_component(component)

    @property
    def amount(self):
        # TODO setter to add multiple at once
        raise NotImplementedError


class Structure(BaseItem, Options):
    def __init__(self, *components: Component):
        super().__init__()
        self.components = Components()
        for component in components:
            if isinstance(component, Component):
                self.components.append(component)

        self._layers = Layers(self.components)

    @property
    def layers(self):
        # At the moment is_spherical == is layered
        if not self.shape.stype.is_spherical:
            raise KeyError(f"Layers are not available for Shape {self.shape.stype}")
        return self._layers

    def assemble(self):
        generator = Generator(self)

        self.molecule.resnames = [component.name for component in self.components]
        self.shape.layers.quantity = len(self.layers)
        fracs = []
        for layer in self.layers:
            layer_fracs = [
                layer.fractions.get(component.name, 0) for component in self.components
            ]
            fracs.append(layer_fracs)
        self.molecule.fracs = fracs

        for component in self.components:
            input_opts = InputOptions(component.structure_file_path)
            generator.read_input(input_opts, (component.name,))

        generator.generate_shape()
        generator.dump_file()

        self.output_file = generator.writer_handler.dfout


class Structures(BaseCollection):
    def __init__(self):
        super().__init__()


class SampleModels(BaseCollection):
    pass


class SampleModel(BaseItem):
    def __init__(self, solution, structure, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.solution = solution
        self.structure = structure
        self._file_manager = FileManager()
        self.output = OutputOptions()

    def assemble(self):
        self.structure.output.path = self._file_manager.locate("Structure")
        self.structure.output.base = self.structure.name

        self.structure.assemble()

        add_ions_input = self._file_manager.init_ionized(
            self.structure.output_file, sample_model_name=self.name
        )

        for ion in self.solution.ions:
            gmx_add_ions_solv(add_ions_input,str(ion.amount), ion.structure_file_path)
            add_ions_input = self._file_manager.locate_ionized(
                add_ions_input, str(ion.amount)
            )

        gmx_add_ions_solv(add_ions_input, "0", "single-ions.gro", "solvate")
        self.output.full_path = self._file_manager.finalize_solution(
            add_ions_input, self.name
        )
