from __future__ import annotations
from typing import Union, Dict, Tuple
import typing as ty
import shutil
import re
import yaml
import tempfile
from pathlib import Path
import attrs
import pytest
import docker
from pydra2app.core.image import App

from pydra2app.core.cli import (
    make,
    make_docs,
    bootstrap,
)
from frametree.core.utils import show_cli_trace


# @pytest.mark.xfail(reason="Need to fix a couple of things after syntax changes")
def test_deploy_make_cli(
    command_spec: dict[str, ty.Any],
    cli_runner: ty.Callable[..., ty.Any],
    work_dir: Path,
) -> None:

    DOCKER_ORG = "testorg"
    DOCKER_REGISTRY = "test.registry.org"
    IMAGE_GROUP_NAME = "testpkg"

    concatenate_spec = {
        "title": "a test image spec",
        "commands": {"test-command": command_spec},
        "version": "1.0",
        "packages": {
            "system": ["vim", "git"],  # just to test it out
            "pip": {"pydra": None, "pydra2app": None},  # just to test it out
        },
        "authors": [{"name": "Some One", "email": "some.one@an.email.org"}],
        "docs": {
            "info_url": "http://concatenate.readthefakedocs.io",
        },
    }

    build_dir = work_dir / "build"
    build_dir.mkdir()
    spec_path = work_dir / DOCKER_ORG
    sub_dir = spec_path / IMAGE_GROUP_NAME
    sub_dir.mkdir(parents=True)
    with open(sub_dir / "concatenate.yml", "w") as f:
        yaml.dump(concatenate_spec, f)

    result = cli_runner(
        make,
        [
            "common:App",
            str(spec_path),
            "--build-dir",
            str(build_dir),
            "--registry",
            DOCKER_REGISTRY,
            "--loglevel",
            "warning",
            "--use-local-packages",
            "--install-extras",
            "test",
            "--raise-errors",
            "--for-localhost",
            "--dont-check-registry",
            "--stream-logs",
        ],
    )
    assert result.exit_code == 0, show_cli_trace(result)
    tag = result.output.strip().splitlines()[-1]
    assert tag == f"{DOCKER_REGISTRY}/{DOCKER_ORG}/{IMAGE_GROUP_NAME}.concatenate:1.0"

    # Clean up the built image
    dc = docker.from_env()
    dc.images.remove(tag)


# @pytest.mark.xfail(reason="Need to fix the test handle invalid docker tag name used")
def test_deploy_remake_cli(command_spec, local_docker_registry, cli_runner, run_prefix):
    """Tests the check to see whether"""

    IMAGE_GROUP_NAME = "testpkg-rebuild" + run_prefix

    def build_spec(spec, **kwargs):
        work_dir = Path(tempfile.mkdtemp())
        build_dir = work_dir / "build"
        build_dir.mkdir()
        spec_path = work_dir / "testorg"
        sub_dir = spec_path / IMAGE_GROUP_NAME
        sub_dir.mkdir(parents=True)
        with open(sub_dir / "concatenate.yml", "w") as f:
            yaml.dump(spec, f)

        result = cli_runner(
            make,
            [
                "common:App",
                str(spec_path),
                "--build-dir",
                str(build_dir),
                "--registry",
                local_docker_registry,
                "--loglevel",
                "warning",
                "--use-local-packages",
                "--install-extras",
                "test",
                "--raise-errors",
                "--check-registry",
                "--for-localhost",
            ],
            **kwargs,
        )
        return result

    concatenate_spec = {
        "title": "a test image",
        "commands": {"test-command": command_spec},
        "version": "1.0",
        "packages": {"system": ["vim", "git"], "pip": ["pydra2app"]},
        "name": "test_deploy_rebuild_cli",
        "authors": [{"name": "Some One", "email": "some.one@an.email.org"}],
        "docs": {"info_url": "http://concatenate.readthefakedocs.io"},
    }

    # Build a basic image
    result = build_spec(concatenate_spec)
    assert result.exit_code == 0, show_cli_trace(result)
    assert result.output
    tag = result.output.strip().splitlines()[-1]
    try:
        dc = docker.from_env()
        dc.api.push(tag)

        # FIXME: Need to ensure that logs are captured properly then we can test this
        # result = build_spec(concatenate_spec)
        # assert "Skipping" in result.output

        # Modify the spec so it doesn't match the original that has just been
        # built (but don't increment the version number -> image tag so there
        # is a clash)
        concatenate_spec["packages"] = {"system": ["vim", "git"]}

        result = build_spec(concatenate_spec, catch_exceptions=False)

        # Check that the image was rebuilt with an incremented tag
        assert result.exit_code == 0, show_cli_trace(result)
        rebuilt_tag = result.output.strip().splitlines()[-1]
        assert rebuilt_tag.split(":")[-1] == "1.0-post1"
        dc.images.remove(rebuilt_tag)
    finally:
        # Clean up the built images
        dc.images.remove(tag)


@attrs.define
class DocsFixture:

    yaml_src: str
    markdown: str
    licenses_to_provide: ty.List[str] = attrs.field(factory=list)


docs_fixtures = {
    "simple": DocsFixture(
        """
title: a simple app
version: &package_version '0.16.1'
authors:
  - name: author_name
    email: author@email.org
base_image:
  name: abc
  tag: *package_version
  package_manager: apt
docs:
  info_url: https://example.com
  description: >-
    a test of the YAML join functionality
commands:
  identity-task:
    task: pydra2app.testing.tasks:IdentityTextFile
    operates_on: sample
    """.strip(),
        """
---
source_file: spec.yaml
title: package.spec
weight: 10

---

## Package Info
|Key|Value|
|---|-----|
|Name|package.spec|
|Title|a simple app|
|Version|0.16.1|
|Base image|`abc:0.16.1`|
|Maintainer|author_name (author@email.org)|
|Info URL|https://example.com|

a test of the YAML join functionality

## Commands
|Key|Value|
|---|-----|
|Task|pydra2app.testing.tasks:IdentityTextFile|
|Operates on|sample|
#### Inputs
|Name|Data-type(s)|Required|Description|
|----|------------|--------|-----------|
|`in_file`|<span data-toggle="tooltip" data-placement="bottom" title="text/text-file" aria-label="text/text-file">text/text-file</span>|Y|the input text file|

#### Outputs
|Name|Data-type(s)|Always generated|Description|
|----|------------|----------------|-----------|
|`out_file`|<span data-toggle="tooltip" data-placement="bottom" title="text/text-file" aria-label="text/text-file">text/text-file</span>|Y|the output text file|

#### Parameters
|Name|Data-type(s)|Default|Description|
|----|------------|-------|-----------|
""".strip(),
    ),
    #     "full": DocsFixture(
    #         """
    # title: a more involved image spec
    # version: &package_version '0.16.1'
    # authors:
    #   - name: author_name
    #     email: author@email.org
    # base_image:
    #   name: abc
    #   tag: *package_version
    #   package_manager: yum
    # docs:
    #   info_url: https://example.com
    #   description: >-
    #     a longer description
    #   known_issues:
    #     - description: Memory overrun on large file paths
    #       url: https://github.com/myorg/mypackage/issues/644
    # packages:
    #   system:
    #     vim: 99.1
    #     git:
    #   pip:
    #     - pydra
    #     - pydra-tasks-dcm2niix
    #   neurodocker:
    #     dcm2niix: v1.0.20201102
    # licenses:
    #   freesurfer:
    #     destination: /opt/freesurfer/license.txt
    #     description: >
    #       license description
    #     info_url: http://path.to.license.provider.org/licenses
    # commands:
    #   bids-task:
    #     task: bids:bids_app
    #     inputs:
    #       T1w:
    #         configuration:
    #           path: anat/T1w
    #         datatype: medimage/nifti-gz-x
    #         help: "T1-weighted anatomical scan"
    #         column_defaults:
    #           datatype: medimage/dicom-series
    #       T2w:
    #         configuration:
    #           path: anat/T2w
    #         datatype: medimage/nifti-gz-x
    #         help: "T2-weighted anatomical scan"
    #         column_defaults:
    #           datatype: medimage/dicom-series
    #       fMRI:
    #         datatype: medimage/nifti-gz-x
    #         help: "functional MRI"
    #         configuration:
    #           path: func/bold/task=rest
    #         column_defaults:
    #           datatype: medimage/dicom-series
    #     outputs:
    #       mriqc:
    #         datatype: generic/directory
    #         help: "MRIQC output directory"
    #         configuration:
    #           path: mriqc
    #     parameters:
    #       fmriprep_flags:
    #         field: flags
    #         datatype: field/text
    #         help: description of flags param
    #     row_frequency: medimage/session
    #     configuration:
    #       executable: /usr/local/miniconda/bin/mriqc
    #       dataset: /work/bids-dataset
    #       app_output_dir: /work/bids-app-output
    #     """.strip(),
    #         """
    # ---
    # source_file: /var/folders/mz/yn83q2fd3s758w1j75d2nnw80000gn/T/tmp47_dxmyq/specs/spec.yaml
    # title: package.spec
    # weight: 10
    # ---
    # ## Package Info
    # |Key|Value|
    # |---|-----|
    # |Name|package.spec|
    # |Title|a more involved image spec|
    # |Version|0.16.1|
    # |Base image|`abc:0.16.1`|
    # |Maintainer|author_name (author@email.org)|
    # |Info URL|https://example.com|
    # |Known issues|Memory overrun on large file paths (https://github.com/myorg/mypackage/issues/644)|
    # a longer description
    # ### Required licenses
    # |Name|URL|Description|
    # |----|---|-----------|
    # |freesurfer|`http://path.to.license.provider.org/licenses`|license description|
    # ## Commands
    # |Key|Value|
    # |---|-----|
    # |Task|bids:bids_app|
    # |Operates on|session|
    # #### Inputs
    # |Name|Required data-type|Default column data-type|Description|
    # |----|------------------|------------------------|-----------|
    # |`T1w`|<span data-toggle="tooltip" data-placement="bottom" title="medimage/nifti-gz-x" aria-label="medimage/nifti-gz-x">medimage/nifti-gz-x</span>|<span data-toggle="tooltip" data-placement="bottom" title="medimage/dicom-series" aria-label="medimage/dicom-series">medimage/dicom-series</span>|T1-weighted anatomical scan|
    # |`T2w`|<span data-toggle="tooltip" data-placement="bottom" title="medimage/nifti-gz-x" aria-label="medimage/nifti-gz-x">medimage/nifti-gz-x</span>|<span data-toggle="tooltip" data-placement="bottom" title="medimage/dicom-series" aria-label="medimage/dicom-series">medimage/dicom-series</span>|T2-weighted anatomical scan|
    # |`fMRI`|<span data-toggle="tooltip" data-placement="bottom" title="medimage/nifti-gz-x" aria-label="medimage/nifti-gz-x">medimage/nifti-gz-x</span>|<span data-toggle="tooltip" data-placement="bottom" title="medimage/dicom-series" aria-label="medimage/dicom-series">medimage/dicom-series</span>|functional MRI|
    # #### Outputs
    # |Name|Required data-type|Default column data-type|Description|
    # |----|------------------|------------------------|-----------|
    # |`mriqc`|<span data-toggle="tooltip" data-placement="bottom" title="generic/directory" aria-label="generic/directory">generic/directory</span>|<span data-toggle="tooltip" data-placement="bottom" title="generic/directory" aria-label="generic/directory">generic/directory</span>|MRIQC output directory|
    # #### Parameters
    # |Name|Data type|Description|
    # |----|---------|-----------|
    # |`fmriprep_flags`|`str`|description of flags param|
    # """.strip(),
    #         ["freesurfer"],
    #     ),
}


@pytest.mark.parametrize("fixture", docs_fixtures.items(), ids=lambda x: x[0])
def test_make_docs_cli(
    cli_runner, run_prefix, work_dir: Path, fixture: Tuple[str, DocsFixture]
):
    fixture_name, fixture_content = fixture

    # TODO handle multiple 'files' in a fixture
    print(f"Processing fixture: {fixture_name!r}")
    output = _make_docs(cli_runner, work_dir, fixture_content.yaml_src)

    strip_source_file_re = re.compile(r"source_file:.*")

    stripped_output = strip_source_file_re.sub("", output)
    stripped_reference = strip_source_file_re.sub("", fixture_content.markdown)

    assert (
        stripped_output == stripped_reference
    ), f"Fixture {fixture_name!r} didn't match output"


def _make_docs(
    cli_runner,
    work_dir: Path,
    docs: Union[str, Dict[str, str]],
    *args,
    flatten: ty.Optional[bool] = None,
) -> Union[str, Dict[str, str]]:
    out_dir = work_dir / "out"
    org_dir = work_dir / "org"
    specs_dir = org_dir / "package"
    if specs_dir.exists():
        shutil.rmtree(specs_dir)
    specs_dir.mkdir(parents=True)

    if type(docs) is str:
        (specs_dir / "spec.yaml").write_text(docs)
    else:
        for name, content in docs.items():
            path = specs_dir / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)

    result = cli_runner(
        make_docs,
        [
            specs_dir.as_posix(),
            out_dir.as_posix(),
            "--spec-root",
            str(work_dir),
            "--default-axes",
            "samples",
        ]
        + (["--flatten" if flatten else "--no-flatten"] if flatten is not None else [])
        + list(args),
    )

    assert result.exit_code == 0, show_cli_trace(result)

    if type(docs) is str:
        return (out_dir / "org" / "package.spec.md").read_text().strip()
    else:
        return {
            file.relative_to(out_dir).as_posix(): file.read_text().strip()
            for file in out_dir.glob("*.md")
        }


def test_bootstrap(cli_runner: ty.Callable[..., ty.Any], work_dir: Path) -> None:

    out_yaml = work_dir / "out-spec.yaml"

    result = cli_runner(
        bootstrap,
        [
            str(out_yaml),
            "--author",
            "An Author",
            "$an.author@a.institution",
            "--version",
            "7.1.1",
            "--base-image",
            "name",
            "vnmd/freesurfer_7.1.1",
            "--base-image",
            "tag",
            "20211216",
            "--base-image",
            "package_manager",
            "apt",
            "--packages-pip",
            "fileformats-medimage-extras==0.8.0",
            "--packages-neurodocker",
            "dcm2niix==v1.0.20201102",
            "--command-task",
            "shell::mri_convert <head:medimage/nifti-gz> <brain:medimage/nifti-gz>",
            # "--command-input",
            # "head",
            # "datatype=medimage/nifti-gz,configuration.position=-2,configuration.argstr=''",
            # "--command-output",
            # "brain",
            # "datatype=medimage/nifti-gz,configuration.position=-1,configuration.argstr=''",
            # "--command-configuration",
            # "executable",
            # "mri_convert",
            "--title",
            "MRI Convert",
            "--license",
            "freesurfer",
            "/opt/freesurfer/license.txt",
            "https://surfer.nmr.mgh.harvard.edu/registration.html",
            "The freesurfer license that is required to run any tool within the package",
        ],
    )

    assert result.exit_code == 0, show_cli_trace(result)

    # Check that the YAML loads properly
    App.load(out_yaml)
