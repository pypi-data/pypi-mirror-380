import os
import shutil

import platformdirs
import pooch

from shapes.basics.defaults import STRUCTURE_EXTENSIONS

# TODO Add resname/name to the registry and read it from some file in assets dir
REGISTRY = [
    {
        "name": "DOPC",
        "fname": "DOPC.gro",
        "ftype": "Lipids",
        "url": "https://gitlab.com/simnavi/shapespyer/-/raw/main/examples/CG_DOPC/setup/DOPC_single.gro",
    },
    {
        "name": "POPC",
        "fname": "POPC.pdb",
        "ftype": "Lipids",
        "url": "https://gitlab.com/simnavi/shapespyer/-/raw/main/examples/POPC/inp/POPC.pdb",
    },
    {
        "name": "CTA",
        "fname": "CTA.gro",
        "ftype": "Surfactants",
        "url": "https://gitlab.com/simnavi/shapespyer/-/raw/main/examples/SDS-CTAB/inp/config_smiles_SDS-C10TAB.gro",
    },
    {
        "name": "SDS",
        "fname": "SDS.gro",
        "ftype": "Surfactants",
        "url": "https://gitlab.com/simnavi/shapespyer/-/raw/main/examples/SDS/inp/SDS-single1.gro",
    },
    {
        "name": "SDS",
        "fname": "SDS.itp",
        "ftype": "Surfactants",
        "url": "https://gitlab.com/simnavi/shapespyer/-/raw/main/examples/CTAB/equil0/toppar/SDS.itp",
    },
    {
        "name": "BRA",
        "fname": "BRA.gro",
        "ftype": "Ions",
        "url": "https://gitlab.com/simnavi/shapespyer/-/raw/main/examples/CTAB/equil0/toppar/single-ionBRA.gro",
    },
    {
        "name": "CLA",
        "fname": "CLA.gro",
        "ftype": "Ions",
        "url": "https://gitlab.com/simnavi/shapespyer/-/raw/main/examples/CTAB/equil0/toppar/single-ionCLA.gro",
    },
    {
        "name": "NAT",
        "fname": "NAT.gro",
        "ftype": "Ions",
        "url": "https://gitlab.com/simnavi/shapespyer/-/raw/main/examples/CTAB/equil0/toppar/single-ionNAT.gro",
    },
]


class FileManager:
    def __init__(self):
        self.app_path = platformdirs.user_data_dir("shapespyer", "SimNavi", roaming=True)
        self.path = os.path.join(self.app_path, "Assets")
        self.components_path = os.path.join(self.path, "Components")
        os.makedirs(self.components_path, exist_ok=True)
        self.ions_path = os.path.join(self.components_path, "Ions")
        os.makedirs(self.ions_path, exist_ok=True)
        self.lipids_path = os.path.join(self.components_path, "Lipids")
        os.makedirs(self.lipids_path, exist_ok=True)
        self.surfactants_path = os.path.join(self.components_path, "Surfactants")
        os.makedirs(self.surfactants_path, exist_ok=True)

        self.type_path_map = {
            "Ion": self.ions_path,
            "Lipid": self.lipids_path,
            "Surfactant": self.surfactants_path,
        }

        self._project = None

        self._retrieve_remote()

    def _subtype_path(self, name):
        return os.path.join(self.path, name)

    def _retrieve_remote(self):
        for file_data in REGISTRY:
            pooch.retrieve(
                url=file_data["url"],
                known_hash=None,
                fname=file_data["fname"],
                path=os.path.join(
                    self.components_path, file_data["ftype"], file_data["name"]
                ),
            )

    def locate(self, type_name):
        # TODO
        # How do I request an output from FM? nowing the type and name and project.
        # FM is instatiated for the project so it know the project path
        # I request with the object. figures out where the object is supposed to be stored.
        # If objects path is written in - makes sure it matches the calculated
        # expectations and the file exists . If it doesn't - just return the expected location.
        # Maybe even if the file location is in the object, it only gives a warning if they don't match.

        # TODO if this filemanager has a project, it locate should refer to project's path instead of general case

        # TODO think if it should reutrn dirname or full path. For now it's just dirname, figuring that name + ext is stored in objects themselves as outputoptions.
        if self._project is None:
            parent_path = self.app_path
        else:
            raise NotImplementedError

        type_path = os.path.join(parent_path, type_name)
        os.makedirs(type_path, exist_ok=True)
        return type_path

    def init_ionized(self, structure_path, sample_model_name):
        self.ionized_path = os.path.join(self.locate("SampleModel"), sample_model_name)
        os.makedirs(self.ionized_path, exist_ok=True)
        starting_structure = os.path.basename(structure_path)
        destination = os.path.join(self.ionized_path, starting_structure)
        shutil.copyfile(structure_path, destination)
        starting_root, _ = os.path.splitext(destination)
        return starting_root

    def locate_ionized(self, structure_path, amount):
        structure_root, _ = os.path.splitext(structure_path)
        return f"{structure_root}-ions{amount}"

    def finalize_solution(self, latest_root, sample_name, persist=True):
        ext = ".gro"
        latest_structure = f"{latest_root}-wTIP3{ext}"
        new_name = f"{sample_name}{ext}"
        destination = os.path.join(self.locate("SampleModel"), new_name)
        shutil.copyfile(latest_structure, destination)

        if not persist:
            # TODO purge all temporary ionized files at self.ionized_path
            raise NotImplementedError

        return destination

    def available_assets(self, type_name):
        assets = {}
        for subtype, path in self.type_path_map.items():
            assets[os.path.basename(path)] = tuple(
                (entry.name for entry in os.scandir(self.type_path_map[subtype]))
            )
        return assets

    def locate_component(self, component_type, component_name):
        # TODO in file manager make it so it scans not only directory names (user names)
        # but also files in them, building some kind of secondary map to lookup
        # both usernames and if it fails, residuenames
        structure_file_path = None
        topology_file_path = None

        type_path = self.type_path_map[component_type]
        entries_path = os.path.join(type_path, component_name)
        entries = os.listdir(entries_path)
        if len(entries) == 0:
            raise FileNotFoundError(
                f"'{component_name}' is registered in the Assets Archive, but structure"
                " and topology files were not found."
            )

        if len(entries) > 2:
            raise UserWarning(
                f"Found unexpected files for '{component_name}' in the Assets Archive."
            )

        for entry in entries:
            _, ext = os.path.splitext(entry)
            full_path = os.path.abspath(os.path.join(entries_path, entry))
            if ext in STRUCTURE_EXTENSIONS:
                structure_file_path = full_path
            elif ext == ".itp":
                topology_file_path = full_path

        return structure_file_path, topology_file_path

    def save(self, type_name, structure_file_path, topology_file_path):
        save_path = os.path.join(self.components_path, type_name)
        if os.path.exists(save_path):
            os.rmdir(save_path)
        os.makedirs(save_path)

        if os.path.isfile(structure_file_path):
            base_name = os.path.basename(structure_file_path)
            destination = os.path.join(save_path, base_name)
            shutil.copyfile(structure_file_path, destination)
            structure_file_path = destination
        else:
            raise FileNotFoundError(
                f"Structure file {structure_file_path} does not exist"
            )

        if os.path.isfile(topology_file_path):
            base_name = os.path.basename(topology_file_path)
            destination = os.path.join(save_path, base_name)
            shutil.copyfile(topology_file_path, destination)
            topology_file_path = destination

        return structure_file_path, topology_file_path
