import logging
from pathlib import Path

from pydantic import BaseModel
from sqlalchemy import text

import esgvoc.core.constants
import esgvoc.core.db.connection as db
import esgvoc.core.service as service
from esgvoc.core.data_handler import JsonLdResource
from esgvoc.core.db.connection import DBConnection, read_json_file, read_yaml_file
from esgvoc.core.db.models.mixins import TermKind
from esgvoc.core.db.models.project import PCollection, Project, PTerm
from esgvoc.core.exceptions import EsgvocDbError
from esgvoc.core.service.data_merger import DataMerger

_LOGGER = logging.getLogger(__name__)


def infer_term_kind(json_specs: dict) -> TermKind:
    if esgvoc.core.constants.PATTERN_JSON_KEY in json_specs:
        return TermKind.PATTERN
    elif esgvoc.core.constants.COMPOSITE_PARTS_JSON_KEY in json_specs:
        return TermKind.COMPOSITE
    else:
        return TermKind.PLAIN


def ingest_metadata_project(connection: DBConnection, git_hash):
    with connection.create_session() as session:
        project = Project(id=str(connection.file_path.stem), git_hash=git_hash, specs={})
        session.add(project)
        session.commit()


def get_data_descriptor_id_from_context(collection_context: dict) -> str:
    data_descriptor_url = collection_context[esgvoc.core.constants.CONTEXT_JSON_KEY][
        esgvoc.core.constants.DATA_DESCRIPTOR_JSON_KEY
    ]  # noqa E211
    return Path(data_descriptor_url).name


def instantiate_project_term(
    universe_term_json_specs: dict, project_term_json_specs_update: dict, pydantic_class: type[BaseModel]
) -> dict:
    term_from_universe = pydantic_class(**universe_term_json_specs)
    updated_term = term_from_universe.model_copy(update=project_term_json_specs_update, deep=True)
    return updated_term.model_dump()


def ingest_collection(collection_dir_path: Path, project: Project, project_db_session) -> None:
    collection_id = collection_dir_path.name
    collection_context_file_path = collection_dir_path.joinpath(esgvoc.core.constants.CONTEXT_FILENAME)
    try:
        collection_context = read_json_file(collection_context_file_path)
        data_descriptor_id = get_data_descriptor_id_from_context(collection_context)
    except Exception as e:
        msg = f"unable to read project context file {collection_context_file_path}"
        _LOGGER.fatal(msg)
        raise EsgvocDbError(msg) from e
    # [KEEP]
    collection = PCollection(
        id=collection_id,
        context=collection_context,
        project=project,
        data_descriptor_id=data_descriptor_id,
        term_kind="",
    )  # We ll know it only when we ll add a term
    # (hypothesis all term have the same kind in a collection) # noqa E116
    term_kind_collection = None

    for term_file_path in collection_dir_path.iterdir():
        _LOGGER.debug(f"found term path : {term_file_path}")
        if term_file_path.is_file() and term_file_path.suffix == ".json":
            try:
                locally_avail = {
                    "https://espri-mod.github.io/mip-cmor-tables": service.current_state.universe.local_path
                }
                json_specs = DataMerger(
                    data=JsonLdResource(uri=str(term_file_path)),
                    # locally_available={"https://espri-mod.github.io/mip-cmor-tables":".cache/repos/WCRP-universe"}).merge_linked_json()[-1]
                    locally_available=locally_avail,
                ).merge_linked_json()[-1]
                term_kind = infer_term_kind(json_specs)
                term_id = json_specs["id"]

                if term_kind_collection is None:
                    term_kind_collection = term_kind

            except Exception as e:
                _LOGGER.warning(
                    f"Unable to read term file {term_file_path} in collection '{collection_id}' "
                    + f"of project '{project.id}'. Skip.\n{str(e)}"
                )
                continue
            try:
                term = PTerm(
                    id=term_id,
                    specs=json_specs,
                    collection=collection,
                    kind=term_kind,
                )
                project_db_session.add(term)
            except Exception as e:
                # Enhanced error reporting for term validation failures
                _LOGGER.error(
                    f"Failed to create term '{term_id}' in collection '{collection_id}' "
                    + f"of project '{project.id}' from file '{term_file_path}': {str(e)}"
                )
                continue
    if term_kind_collection:
        collection.term_kind = term_kind_collection
    else:
        # If we couldn't determine a term kind, use PLAIN as default and log warning
        _LOGGER.warning(
            f"No term kind determined for collection '{collection_id}' in project '{project.id}'. "
            + "Using PLAIN as default. This might indicate empty collection or processing errors."
        )
        collection.term_kind = TermKind.PLAIN

    try:
        project_db_session.add(collection)
    except Exception as e:
        error_context = f"Failed to add collection '{collection_id}' to project '{project.id}'"
        _LOGGER.error(f"{error_context}: {str(e)}")
        raise EsgvocDbError(f"{error_context}: {str(e)}") from e


def ingest_project(project_dir_path: Path, project_db_file_path: Path, git_hash: str):
    try:
        project_connection = db.DBConnection(project_db_file_path)
    except Exception as e:
        msg = f"unable to read project SQLite file at {project_db_file_path}"
        _LOGGER.fatal(msg)
        raise EsgvocDbError(msg) from e

    with project_connection.create_session() as project_db_session:
        project_specs_file_path = project_dir_path.joinpath(esgvoc.core.constants.PROJECT_SPECS_FILENAME)
        drs_specs_file_path = project_dir_path.joinpath(esgvoc.core.constants.DRS_SPECS_FILENAME)
        catalog_specs_file_path = project_dir_path.joinpath(esgvoc.core.constants.CATALOG_SPECS_FILENAME)
        attr_specs_file_path = project_dir_path.joinpath(esgvoc.core.constants.ATTRIBUTES_SPECS_FILENAME)
        try:
            raw_project_specs = read_yaml_file(project_specs_file_path)
            project_id = raw_project_specs[esgvoc.core.constants.PROJECT_ID_JSON_KEY]
            raw_drs_specs = read_yaml_file(drs_specs_file_path)
            project_specs = raw_project_specs
            project_specs["drs_specs"] = raw_drs_specs
            if catalog_specs_file_path.exists():
                raw_catalog_specs = read_yaml_file(catalog_specs_file_path)
                project_specs["catalog_specs"] = raw_catalog_specs
            if attr_specs_file_path.exists():
                raw_attr_specs = read_yaml_file(attr_specs_file_path)
                project_specs["attr_specs"] = raw_attr_specs
        except Exception as e:
            msg = f"unable to read specs files in {project_dir_path}"
            _LOGGER.fatal(msg)
            raise EsgvocDbError(msg) from e

        project = Project(id=project_id, specs=project_specs, git_hash=git_hash)
        project_db_session.add(project)

        for collection_dir_path in project_dir_path.iterdir():
            # TODO maybe put that in settings
            if collection_dir_path.is_dir() and (collection_dir_path / "000_context.jsonld").exists():
                _LOGGER.debug(f"found collection dir : {collection_dir_path}")
                try:
                    ingest_collection(collection_dir_path, project, project_db_session)
                except Exception as e:
                    msg = f"unexpected error while ingesting collection {collection_dir_path}"
                    _LOGGER.fatal(msg)
                    raise EsgvocDbError(msg) from e
        project_db_session.commit()

        # Well, the following instructions are not data duplication. It is more building an index.
        # Read: https://sqlite.org/fts5.html
        try:
            sql_query = (
                "INSERT INTO pterms_fts5(pk, id, specs, kind, collection_pk) "  # noqa: S608
                + "SELECT pk, id, specs, kind, collection_pk FROM pterms;"
            )
            project_db_session.exec(text(sql_query))  # type: ignore
        except Exception as e:
            msg = f"unable to insert rows into pterms_fts5 table for {project_db_file_path}"
            _LOGGER.fatal(msg)
            raise EsgvocDbError(msg) from e
        project_db_session.commit()
        try:
            sql_query = (
                "INSERT INTO pcollections_fts5(pk, id, data_descriptor_id, context, "  # noqa: S608
                + "project_pk, term_kind) SELECT pk, id, data_descriptor_id, context, "
                + "project_pk, term_kind FROM pcollections;"
            )
            project_db_session.exec(text(sql_query))  # type: ignore
        except Exception as e:
            msg = f"unable to insert rows into pcollections_fts5 table for {project_db_file_path}"
            _LOGGER.fatal(msg)
            raise EsgvocDbError(msg) from e
        project_db_session.commit()
