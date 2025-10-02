from shapes.project.core import Component, Ion
from shapes.project.files import FileManager


class Assets:
    def __init__(self, file_manager=None):
        self.file_manager = file_manager if file_manager else FileManager()

    @property
    def available_components(self):
        return self.file_manager.available_assets("Components")

    def get_component(self, name):
        if name not in self.available_components:
            raise ValueError(
                f"'{name}' component is not available in the Assets Archive"
            )

        s_path, top_path = self.file_manager.get_resource("Components", name)
        return Component(name, s_path, top_path)

    def get_ion(self, name):
        if name not in self.available_components:
            raise ValueError(f"'{name}' ion is not available in the Archive")

        s_path, top_path = self.file_manager.get_resource("Ions", name)
        return Ion(name, s_path, top_path)

    def save(self, resource, overwrite=False):
        SUBTYPE_MAP = {Component: "Components", Ion: "Ions"}
        type_name = SUBTYPE_MAP[type(resource)]

        if resource.name == "" or resource.name is None:
            raise ValueError("Cannot save without a proper name.")

        if (
            resource.name in self.file_manager.available_resources(type_name)
            and not overwrite
        ):
            return False

        saved_structure, saved_topology = self.file_manager.save(
            type_name, resource.structure_file_path, resource.topology_file_path
        )
        resource.structure_file_path = saved_structure
        resource.topology_file_path = saved_topology

        return True
