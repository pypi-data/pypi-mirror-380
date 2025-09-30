from __future__ import annotations
import sys
from pathlib import Path
import json
import typing as ty
import attrs
from neurodocker.reproenv import DockerRenderer
from frametree.xnat import XnatViaCS
from frametree.core.serialize import ClassResolver, ObjectListConverter
from frametree.core.store import Store
from pydra2app.core.image import App
from .command import XnatCommand


@attrs.define(kw_only=True)
class XnatApp(App):  # type: ignore[misc]

    PIP_DEPENDENCIES = (
        "pydra2app-xnat",
        "fileformats-medimage",
        "fileformats-medimage-extras",
    )

    commands: ty.List[XnatCommand] = attrs.field(
        converter=ObjectListConverter(  # type: ignore[misc]
            XnatCommand
        )  # Change the command type to XnatCommand subclass
    )

    @commands.validator
    def _validate_commands(
        self,
        attribute: attrs.Attribute[ty.List[XnatCommand]],
        commands: ty.List[XnatCommand],
    ) -> None:
        if not commands:
            raise ValueError("At least one command must be defined within that app")

    def construct_dockerfile(
        self,
        build_dir: Path,
        for_localhost: bool = False,
        **kwargs: ty.Any,
    ) -> DockerRenderer:
        """Creates a Docker image containing one or more XNAT commands ready
        to be installed in XNAT's container service plugin

        Parameters
        ----------
        build_dir : Path
            the directory to build the docker image within, i.e. where to write
            Dockerfile and supporting files to be copied within the image
        for_localhost : bool
            whether to create the container so that it will work with the test
            XNAT configuration (i.e. hard-coding the XNAT server IP)
        **kwargs:
            Passed on to super `construct_dockerfile` method

        Returns
        -------
        DockerRenderer
            the Neurodocker renderer
        Path
            path to build directory
        """

        dockerfile = super().construct_dockerfile(build_dir, **kwargs)

        # Copy the generated XNAT commands inside the container for ease of reference
        xnat_commands = self.copy_command_refs(dockerfile, build_dir)

        self.save_store_config(dockerfile, build_dir, for_localhost=for_localhost)

        # Convert XNAT command label into string that can by placed inside the
        # Docker label
        commands_label = json.dumps(xnat_commands).replace("$", r"\$")

        self.add_labels(
            dockerfile,
            {"org.nrg.commands": commands_label, "maintainer": self.authors[0].email},
        )

        return dockerfile

    def add_entrypoint(self, dockerfile: DockerRenderer, build_dir: Path) -> None:
        pass  # Don't need to add entrypoint as the command line is specified in the command JSON

    def copy_command_refs(
        self,
        dockerfile: DockerRenderer,
        build_dir: Path,
    ) -> ty.List[ty.Dict[str, ty.Any]]:
        """Copy the generated command JSON within the Docker image for future reference

        Parameters
        ----------
        dockerfile : DockerRenderer
            Neurodocker renderer to build
        xnat_command : ty.Dict[str, Any]
            XNAT command to write to file within the image for future reference
        build_dir : Path
            path to build directory

        Returns
        -------
        list[dict[str, Any]]
            the converted XNAT commands to install in the label
        """
        command_jsons_dir = build_dir / "xnat_commands"
        command_jsons_dir.mkdir(parents=True, exist_ok=True)
        xnat_commands = []
        for command in self.commands:
            xnat_command = command.make_json()
            with open(command_jsons_dir / f"{command.name}.json", "w") as f:
                json.dump(xnat_command, f, indent="    ")
            dockerfile.copy(
                source=[f"./xnat_commands/{command.name}.json"],
                destination=f"/xnat_commands/{command.name}.json",
            )
            xnat_commands.append(xnat_command)
        return xnat_commands

    def save_store_config(
        self, dockerfile: DockerRenderer, build_dir: Path, for_localhost: bool = False
    ) -> None:
        """Save a configuration for a XnatViaCS store.

        Parameters
        ----------
        dockerfile : DockerRenderer
            Neurodocker renderer to build
        build_dir : Path
            the build directory to save supporting files
        for_localhost : bool
            whether the target XNAT is using the local test configuration, in which
            case the server location will be hard-coded rather than rely on the
            XNAT_HOST environment variable passed to the container by the XNAT CS
        """
        xnat_cs_store_entry = {
            "class": "<" + ClassResolver.tostr(XnatViaCS, strip_prefix=False) + ">"
        }
        if for_localhost:
            if sys.platform == "linux":
                ip_address = "172.17.0.1"  # Linux + GH Actions
            else:
                ip_address = "host.docker.internal"  # Mac/Windows local debug
            xnat_cs_store_entry["server"] = "http://" + ip_address + ":8080"
        Store.save_configs(
            {"xnat-cs": xnat_cs_store_entry}, config_path=build_dir / "stores.yaml"
        )
        dockerfile.run(command="mkdir -p /root/.pydra2app")
        dockerfile.run(command=f"mkdir -p {str(XnatViaCS.CACHE_DIR)}")
        dockerfile.copy(
            source=["./stores.yaml"],
            destination=self.IN_DOCKER_FRAMETREE_HOME_DIR + "/stores.yaml",
        )
