from datetime import datetime
import json
import logging
import uuid

from collections import defaultdict
from django.db import connection
from django.db.models import OuterRef, Prefetch, Subquery
from django.db.models.functions import Coalesce
from django.utils.translation import gettext as _
from arches.app.datatypes.datatypes import DataTypeFactory
from arches.app.etl_modules.save import save_to_tiles
from arches.app.etl_modules.decorators import load_data_async
from arches.app.etl_modules.base_import_module import BaseImportModule
from arches.app.models import models
from arches.app.models.models import LoadStaging, NodeGroup, LoadEvent
from arches.app.models.system_settings import settings
import arches_lingo.tasks as tasks
from arches_lingo.const import (
    SCHEMES_GRAPH_ID,
    CONCEPTS_GRAPH_ID,
    TOP_CONCEPT_OF_NODE_AND_NODEGROUP,
    CLASSIFICATION_STATUS_NODEGROUP,
    CLASSIFICATION_STATUS_ASCRIBED_CLASSIFICATION_NODEID,
    CLASSIFICATION_STATUS_ASCRIBED_RELATION_NODEID,
    CLASSIFICATION_STATUS_TYPE_NODEID,
    CLASSIFICATION_STATUS_TYPE_METATYPE_NODEID,
    CLASSIFICATION_STATUS_ASSIGNMENT_ACTOR_NODEID,
    CLASSIFICATION_STATUS_ASSIGNMENT_OBJ_USED_NODEID,
    CLASSIFICATION_STATUS_ASSIGNMENT_TYPE_NODEID,
    CLASSIFICATION_STATUS_TIMESPAN_END_OF_END_NODEID,
    CLASSIFICATION_STATUS_TIMESPAN_BEGIN_OF_BEGIN_NODEID,
    CONCEPTS_PART_OF_SCHEME_NODEGROUP_ID,
)

logger = logging.getLogger(__name__)

details = {
    "etlmoduleid": "11cad3ca-e155-44b1-9910-c50b3def47f6",
    "name": "Migrate to Lingo",
    "description": "Migrate schemes and concepts from the RDM to Arches Lingo",
    "etl_type": "import",
    "component": "views/components/etl_modules/migrate-to-lingo",
    "componentname": "migrate-to-lingo",
    "modulename": "migrate_to_lingo.py",
    "classname": "RDMMtoLingoMigrator",
    "config": {"bgColor": "#ffa564", "circleColor": "#ffd2b1", "show": True},
    "icon": "fa fa-usb",
    "slug": "migrate-to-lingo",
    "helpsortorder": 6,
    "helptemplate": "migrate-to-lingo-help",
}


class RDMMtoLingoMigrator(BaseImportModule):
    def __init__(self, request=None, loadid=None):
        self.request = request if request else None
        self.userid = request.user.id if request else None
        self.moduleid = request.POST.get("module") if request else None
        self.loadid = request.POST.get("loadid") if request else loadid
        self.datatype_factory = DataTypeFactory()
        self.scheme_conceptid = request.POST.get("scheme") if request else None

    def get_schemes(self, request):
        schemes = (
            models.Concept.objects.filter(nodetype="ConceptScheme")
            .annotate(
                prefLabel=Coalesce(
                    Subquery(
                        models.Value.objects.filter(
                            valuetype_id="prefLabel",
                            concept_id=OuterRef("pk"),
                            language_id=settings.LANGUAGE_CODE,
                        ).values("value")[:1]
                    ),
                    Subquery(
                        models.Value.objects.filter(
                            valuetype_id="prefLabel",
                            concept_id=OuterRef("pk"),
                        )
                        .order_by("language_id")
                        .values("value")[:1]
                    ),
                )
            )
            .order_by("prefLabel")
        )
        schemes_json = list(schemes.values("conceptid", "prefLabel"))
        return {"success": True, "data": schemes_json}

    def etl_schemes(self, cursor, nodegroup_lookup, node_lookup, scheme_conceptid):
        schemes = []
        for concept in models.Concept.objects.filter(
            pk=scheme_conceptid
        ).prefetch_related(
            Prefetch("value_set", queryset=models.Value.objects.order_by("value"))
        ):
            scheme_to_load = {"type": "Scheme", "tile_data": []}
            for value in concept.value_set.all():
                scheme_to_load["resourceinstanceid"] = (
                    concept.pk
                )  # use old conceptid as new resourceinstanceid

                if (
                    value.valuetype_id == "prefLabel"
                    or value.valuetype_id == "altLabel"
                    or value.valuetype_id == "hiddenLabel"
                ):
                    appellative_status = {}
                    appellative_status["appellative_status_ascribed_name_content"] = (
                        value.value
                    )
                    appellative_status["appellative_status_ascribed_name_language"] = (
                        value.language.name
                    )
                    appellative_status["appellative_status_ascribed_relation"] = (
                        value.valuetype_id
                    )
                    scheme_to_load["tile_data"].append(
                        {"appellative_status": appellative_status}
                    )
                elif value.valuetype_id == "identifier":
                    identifier = {}
                    identifier["identifier_content"] = value.value
                    identifier["identifier_type"] = value.valuetype_id
                    scheme_to_load["tile_data"].append({"identifier": identifier})
                elif (
                    value.valuetype_id == "note"
                    or value.valuetype_id == "changeNote"
                    or value.valuetype_id == "definition"
                    or value.valuetype_id == "description"
                    or value.valuetype_id == "editorialNote"
                    or value.valuetype_id == "example"
                    or value.valuetype_id == "historyNote"
                    or value.valuetype_id == "scopeNote"
                ):
                    statement = {}
                    statement["statement_content_n1"] = value.value
                    statement["statement_type_n1"] = value.valuetype_id
                    statement["statement_language_n1"] = value.language.name
                    scheme_to_load["tile_data"].append({"statement": statement})
            schemes.append(scheme_to_load)
        self.populate_staging_table(cursor, schemes, nodegroup_lookup, node_lookup)

    def etl_concepts(self, cursor, nodegroup_lookup, node_lookup, concepts_to_migrate):
        concepts = []
        for concept in models.Concept.objects.filter(
            nodetype="Concept", pk__in=concepts_to_migrate
        ).prefetch_related(
            Prefetch("value_set", queryset=models.Value.objects.order_by("value"))
        ):
            concept_to_load = {"type": "Concept", "tile_data": []}
            for value in concept.value_set.all():
                concept_to_load["resourceinstanceid"] = (
                    concept.pk
                )  # use old conceptid as new resourceinstanceid

                if (
                    value.valuetype_id == "prefLabel"
                    or value.valuetype_id == "altLabel"
                    or value.valuetype_id == "hiddenLabel"
                ):
                    appellative_status = {}
                    appellative_status["appellative_status_ascribed_name_content"] = (
                        value.value
                    )
                    appellative_status["appellative_status_ascribed_name_language"] = (
                        value.language.name
                    )
                    appellative_status["appellative_status_ascribed_relation"] = (
                        value.valuetype_id
                    )
                    concept_to_load["tile_data"].append(
                        {"appellative_status": appellative_status}
                    )
                elif value.valuetype_id == "identifier":
                    identifier = {}
                    identifier["identifier_content"] = value.value
                    identifier["identifier_type"] = value.valuetype_id
                    concept_to_load["tile_data"].append({"identifier": identifier})
                elif (
                    value.valuetype_id == "note"
                    or value.valuetype_id == "changeNote"
                    or value.valuetype_id == "definition"
                    or value.valuetype_id == "description"
                    or value.valuetype_id == "editorialNote"
                    or value.valuetype_id == "example"
                    or value.valuetype_id == "historyNote"
                    or value.valuetype_id == "scopeNote"
                ):
                    statement = {}
                    statement["statement_content"] = value.value
                    statement["statement_type"] = value.valuetype_id
                    statement["statement_language"] = value.language.name
                    concept_to_load["tile_data"].append({"statement": statement})
            concepts.append(concept_to_load)
        self.populate_staging_table(cursor, concepts, nodegroup_lookup, node_lookup)

    def populate_staging_table(
        self, cursor, concepts_to_load, nodegroup_lookup, node_lookup
    ):
        tiles_to_load = []
        sortorder_counter = defaultdict(lambda: defaultdict(int))
        for concept_to_load in concepts_to_load:
            for mock_tile in concept_to_load["tile_data"]:
                resourceid = concept_to_load["resourceinstanceid"]
                nodegroup_alias = next(iter(mock_tile.keys()), None)
                nodegroup_id = node_lookup[nodegroup_alias]["nodeid"]
                nodegroup_depth = nodegroup_lookup[nodegroup_id]["depth"]
                tile_id = uuid.uuid4()
                parent_tile_id = None
                tile_value_json, passes_validation = self.create_tile_value(
                    cursor, mock_tile, nodegroup_alias, nodegroup_lookup, node_lookup
                )
                operation = "insert"
                sortorder = sortorder_counter[resourceid][nodegroup_id]
                sortorder_counter[resourceid][nodegroup_id] += 1
                tiles_to_load.append(
                    LoadStaging(
                        load_event=LoadEvent(self.loadid),
                        nodegroup=NodeGroup(nodegroup_id),
                        resourceid=resourceid,
                        tileid=tile_id,
                        parenttileid=parent_tile_id,
                        value=tile_value_json,
                        nodegroup_depth=nodegroup_depth,
                        source_description="{0}: {1}".format(
                            concept_to_load["type"], nodegroup_alias
                        ),  # source_description
                        passes_validation=passes_validation,
                        operation=operation,
                        sortorder=sortorder,
                    )
                )
        staged_tiles = LoadStaging.objects.bulk_create(tiles_to_load)

        cursor.execute(
            """CALL __arches_check_tile_cardinality_violation_for_load(%s)""",
            [self.loadid],
        )
        cursor.execute(
            """
                INSERT INTO load_errors (type, source, error, loadid, nodegroupid)
                SELECT 'tile', source_description, error_message, loadid, nodegroupid
                FROM load_staging
                WHERE loadid = %s AND passes_validation = false AND error_message IS NOT null
            """,
            [self.loadid],
        )

    def create_tile_value(
        self, cursor, mock_tile, nodegroup_alias, nodegroup_lookup, node_lookup
    ):
        tile_value = {}
        tile_valid = True
        for node_alias in mock_tile[nodegroup_alias].keys():
            try:
                nodeid = node_lookup[node_alias]["nodeid"]
                node_details = node_lookup[node_alias]
                datatype = node_details["datatype"]
                datatype_instance = self.datatype_factory.get_instance(datatype)
                source_value = mock_tile[nodegroup_alias][node_alias]
                config = node_details["config"]
                config["loadid"] = self.loadid
                config["nodeid"] = nodeid

                value, validation_errors = self.prepare_data_for_loading(
                    datatype_instance, source_value, config
                )
                valid = True if len(validation_errors) == 0 else False
                if not valid:
                    tile_valid = False
                error_message = ""
                for error in validation_errors:
                    error_message = error["message"]
                    cursor.execute(
                        """INSERT INTO load_errors (type, value, source, error, message, datatype, loadid, nodeid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (
                            "node",
                            source_value,
                            "",
                            error["title"],
                            error["message"],
                            datatype,
                            self.loadid,
                            nodeid,
                        ),
                    )

                tile_value[nodeid] = {
                    "value": value,
                    "valid": valid,
                    "source": source_value,
                    "notes": error_message,
                    "datatype": datatype,
                }
            except KeyError:
                pass

        return tile_value, tile_valid

    def build_concept_hierarchy(self, cursor, scheme_conceptid):
        cursor.execute(
            """
            with recursive collection_hierarchy as (
                select conceptidfrom as root_scheme,
                    conceptidto as child,
                    ARRAY[conceptidfrom] AS path,
                    0 as depth
                from relations
                where not exists (
                    select 1 from relations r2 where r2.conceptidto = relations.conceptidfrom
                ) and (relationtype = 'narrower' or relationtype = 'hasTopConcept')
                union all
                select ch.root_scheme,
                    r.conceptidto,
                    ch.path || r.conceptidfrom,
                    ch.depth + 1
                from collection_hierarchy ch
                join relations r on ch.child = r.conceptidfrom
                where relationtype = 'narrower' or relationtype = 'hasTopConcept'
            )
            select * 
            from collection_hierarchy
            where root_scheme = %s;
            """,
            (scheme_conceptid,),
        )
        results = cursor.fetchall()
        concept_hierarchy = []
        concepts_to_migrate = []
        for result in results:
            concept_dict = {
                "root_scheme": result[0],
                "concept": result[1],
                "path": result[2],
                "depth": result[3],
            }
            concepts_to_migrate.append(result[1])
            concept_hierarchy.append(concept_dict)
        return concept_hierarchy, concepts_to_migrate

    def init_relationships(
        self, cursor, loadid, concepts_to_migrate, concept_hierarchy
    ):
        # Create top concept of scheme relationships (derived from relations with 'hasTopConcept' relationtype)
        cursor.execute(
            """
           insert into load_staging(
                value,
                resourceid,
                tileid,
                passes_validation,
                nodegroup_depth,
                source_description,
                loadid,
                nodegroupid,
                operation,
                sortorder
            )
            select 
                distinct on (conceptidfrom, conceptidto)
                json_build_object(%s::uuid,
                    json_build_object(
                        'notes', '',
                        'valid', true,
                        'value', json_build_array(json_build_object('resourceId', conceptidfrom, 'ontologyProperty', '', 'resourceXresourceId', '', 'inverseOntologyProperty', '')),
                        'source', conceptidfrom,
                        'datatype', 'resource-instance'
                    )
                ) as value,
                conceptidto as resourceinstanceid, -- map target concept's new resourceinstanceid to its existing conceptid
                uuid_generate_v4() as tileid,
                true as passes_validation,
                0 as nodegroup_depth,
                'Scheme: top_concept_of' as source_description,
                %s::uuid as loadid,
                %s::uuid as nodegroupid,
                'insert' as operation,
                (rank() over (partition by conceptidfrom order by v.value)-1) as sortorter
            from relations r
            left join values v on r.conceptidto = v.conceptid
            where relationtype = 'hasTopConcept'
                and v.valuetype = 'prefLabel'
                and conceptidto = ANY(%s);
        """,
            (
                TOP_CONCEPT_OF_NODE_AND_NODEGROUP,
                loadid,
                TOP_CONCEPT_OF_NODE_AND_NODEGROUP,
                concepts_to_migrate,
            ),
        )

        # Create broader relationships (derived from relations with 'narrower' relationtype)
        cursor.execute(
            """
           insert into load_staging(
                value,
                resourceid,
                tileid,
                passes_validation,
                nodegroup_depth,
                source_description,
                loadid,
                nodegroupid,
                operation,
                sortorder
            )
            select 
                json_build_object(%s::uuid,
                    json_build_object(
                        'notes', '',
                        'valid', true,
                        'value', json_build_array(json_build_object('resourceId', conceptidfrom, 'ontologyProperty', '', 'resourceXresourceId', '', 'inverseOntologyProperty', '')),
                        'source', conceptidfrom,
                        'datatype', 'resource-instance-list'
                    ),
                    %s, null,
                    %s, null,
                    %s, null,
                    %s, null,
                    %s, null,
                    %s, null,
                    %s, null,
                    %s, null
                ) as value,
                conceptidto as resourceinstanceid, -- map target concept's new resourceinstanceid to its existing conceptid
                uuid_generate_v4() as tileid,
                true as passes_validation,
                0 as nodegroup_depth,
                'Scheme: top_concept_of' as source_description,
                %s::uuid as loadid,
                %s::uuid as nodegroupid,
                'insert' as operation,
                (rank() over (partition by conceptidto order by v.value)-1) as sortorter
            from relations r
            left join values v on r.conceptidto = v.conceptid
            where relationtype = 'narrower'
                and v.valuetype = 'prefLabel'
                and conceptidto = ANY(%s);
        """,
            (
                CLASSIFICATION_STATUS_ASCRIBED_CLASSIFICATION_NODEID,
                CLASSIFICATION_STATUS_ASCRIBED_RELATION_NODEID,
                CLASSIFICATION_STATUS_TYPE_NODEID,
                CLASSIFICATION_STATUS_TYPE_METATYPE_NODEID,
                CLASSIFICATION_STATUS_ASSIGNMENT_ACTOR_NODEID,
                CLASSIFICATION_STATUS_ASSIGNMENT_OBJ_USED_NODEID,
                CLASSIFICATION_STATUS_ASSIGNMENT_TYPE_NODEID,
                CLASSIFICATION_STATUS_TIMESPAN_END_OF_END_NODEID,
                CLASSIFICATION_STATUS_TIMESPAN_BEGIN_OF_BEGIN_NODEID,
                loadid,
                CLASSIFICATION_STATUS_NODEGROUP,
                concepts_to_migrate,
            ),
        )

        # Create Part of Scheme relationships - derived by recursively generating concept hierarchy & associating
        # concepts with their schemes
        part_of_scheme_tiles = []
        part_of_scheme_nodegroup = NodeGroup.objects.get(
            nodegroupid=CONCEPTS_PART_OF_SCHEME_NODEGROUP_ID
        )
        concepts_with_scheme = {}
        for concept in concept_hierarchy:
            root_scheme = str(concept["root_scheme"])
            resourceinstanceid = concept["concept"]

            concept_has_part_of_scheme = resourceinstanceid in concepts_with_scheme
            existing_scheme = concepts_with_scheme.get(resourceinstanceid)
            if not concept_has_part_of_scheme:
                concepts_with_scheme[resourceinstanceid] = root_scheme
            elif concept_has_part_of_scheme and existing_scheme == root_scheme:
                continue
            elif concept_has_part_of_scheme and existing_scheme != root_scheme:
                return {
                    "status": 400,
                    "success": False,
                    "title": "Concepts may only participate in one scheme",
                    "message": _(
                        "Concept {conceptid} cannot have multiple schemes: {current_scheme} and {existing_scheme}"
                    ).format(
                        {
                            "conceptid": resourceinstanceid,
                            "current_scheme": root_scheme,
                            "existing_scheme": concepts_with_scheme[resourceinstanceid],
                        }
                    ),
                }

            value_obj = {
                str(CONCEPTS_PART_OF_SCHEME_NODEGROUP_ID): {
                    "notes": "",
                    "valid": True,
                    "value": [
                        {
                            "resourceId": root_scheme,
                            "ontologyProperty": "",
                            "resourceXresourceId": "",
                            "inverseOntologyProperty": "",
                        }
                    ],
                    "source": root_scheme,
                    "datatype": "resource-instance",
                }
            }

            staging_tile = LoadStaging(
                value=value_obj,
                resourceid=resourceinstanceid,
                tileid=uuid.uuid4(),
                passes_validation=True,
                nodegroup_depth=0,
                source_description="Concept: Part of Scheme",
                load_event=LoadEvent(self.loadid),
                nodegroup=part_of_scheme_nodegroup,
                operation="insert",
                sortorder=0,
            )
            staging_tile.full_clean()
            part_of_scheme_tiles.append(staging_tile)

        LoadStaging.objects.bulk_create(part_of_scheme_tiles)

    def start(self, request):
        load_details = {"operation": "RDM to Lingo Migration"}
        cursor = connection.cursor()
        cursor.execute(
            """INSERT INTO load_event (
                loadid,
                complete,
                status,
                etl_module_id,
                load_details,
                load_start_time,
                user_id
                ) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                self.loadid,
                False,
                "running",
                self.moduleid,
                json.dumps(load_details),
                datetime.now(),
                self.userid,
            ),
        )
        message = "load event created"
        return {"success": True, "data": message}

    def write(self, request):
        self.loadid = request.POST.get("loadid")
        self.scheme_conceptid = request.POST.get("scheme")
        if models.Concept.objects.count() < 500000:
            response = self.run_load_task(
                self.userid, self.loadid, self.scheme_conceptid
            )
        else:
            response = self.run_load_task_async(request, self.loadid)
        message = "Schemes and Concept Migration to Lingo Models Complete"
        return {"success": True, "data": message}

    def run_load_task(self, userid, loadid, scheme_conceptid):
        self.loadid = loadid  # currently redundant, but be certain
        self.scheme_conceptid = scheme_conceptid

        with connection.cursor() as cursor:

            # Gather and load schemes and concepts
            schemes_nodegroup_lookup, schemes_nodes = self.get_graph_tree(
                SCHEMES_GRAPH_ID
            )
            schemes_node_lookup = self.get_node_lookup(schemes_nodes)
            self.etl_schemes(
                cursor, schemes_nodegroup_lookup, schemes_node_lookup, scheme_conceptid
            )

            concepts_nodegroup_lookup, concepts_nodes = self.get_graph_tree(
                CONCEPTS_GRAPH_ID
            )
            concepts_node_lookup = self.get_node_lookup(concepts_nodes)
            # Prefetch concept hierarchy to avoid building it multiple times
            concept_hierarchy, concepts_to_migrate = self.build_concept_hierarchy(
                cursor, self.scheme_conceptid
            )
            self.etl_concepts(
                cursor,
                concepts_nodegroup_lookup,
                concepts_node_lookup,
                concepts_to_migrate,
            )

            # Create relationships
            self.init_relationships(
                cursor, loadid, concepts_to_migrate, concept_hierarchy
            )

            # Validate and save to tiles
            validation = self.validate(loadid)
            if len(validation["data"]) == 0:
                cursor.execute(
                    """UPDATE load_event SET status = %s WHERE loadid = %s""",
                    ("validated", loadid),
                )
                response = save_to_tiles(userid, loadid)
                cursor.execute(
                    """CALL __arches_update_resource_x_resource_with_graphids();"""
                )
                cursor.execute("""SELECT __arches_refresh_spatial_views();""")
                refresh_successful = cursor.fetchone()[0]
                if not refresh_successful:
                    raise Exception("Unable to refresh spatial views")
                return response
            else:
                cursor.execute(
                    """UPDATE load_event SET status = %s, load_end_time = %s WHERE loadid = %s""",
                    ("failed", datetime.now(), loadid),
                )
                return {"success": False, "data": "failed"}

    @load_data_async
    def run_load_task_async(self, request):
        migrate_rdm_to_lingo_task = tasks.migrate_rdm_to_lingo_task.apply_async(
            (self.userid, self.loadid, self.scheme_conceptid),
        )
        with connection.cursor() as cursor:
            cursor.execute(
                """UPDATE load_event SET taskid = %s WHERE loadid = %s""",
                (migrate_rdm_to_lingo_task.task_id, self.loadid),
            )
