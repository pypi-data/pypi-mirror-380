from collections import defaultdict

from django.contrib.postgres.expressions import ArraySubquery
from django.db.models import CharField, F, OuterRef, Value
from django.db.models.expressions import CombinedExpression
from django.utils.translation import gettext as _

from arches.app.models.models import Language, ResourceInstance, TileModel
from arches_controlled_lists.datatypes.datatypes import ReferenceLabel
from arches_controlled_lists.models import ListItem

from arches_lingo.const import (
    SCHEMES_GRAPH_ID,
    TOP_CONCEPT_OF_NODE_AND_NODEGROUP,
    CLASSIFICATION_STATUS_NODEGROUP,
    CLASSIFICATION_STATUS_ASCRIBED_CLASSIFICATION_NODEID,
    CONCEPT_NAME_NODEGROUP,
    CONCEPT_NAME_CONTENT_NODE,
    CONCEPT_NAME_LANGUAGE_NODE,
    CONCEPT_NAME_TYPE_NODE,
    ALT_LABEL_VALUE,
    HIDDEN_LABEL_VALUE,
    PREF_LABEL_VALUE,
    SCHEME_NAME_NODEGROUP,
    SCHEME_NAME_CONTENT_NODE,
    SCHEME_NAME_LANGUAGE_NODE,
    SCHEME_NAME_TYPE_NODE,
)

from arches_lingo.query_expressions import JsonbArrayElements


TOP_CONCEPT_OF_LOOKUP = f"data__{TOP_CONCEPT_OF_NODE_AND_NODEGROUP}"
BROADER_LOOKUP = f"data__{CLASSIFICATION_STATUS_ASCRIBED_CLASSIFICATION_NODEID}"


class ConceptBuilder:
    def __init__(self):
        self.schemes = ResourceInstance.objects.none()

        # key=scheme resourceid (str) val=set of concept resourceids (str)
        self.top_concepts: dict[str, set[str]] = defaultdict(set)
        # key=concept resourceid (str) val=set of concept resourceids (str)
        self.narrower_concepts: dict[str, set[str]] = defaultdict(set)
        # key=resourceid (str) val=list of label dicts
        self.labels: dict[str, list[dict]] = defaultdict(set)

        # Maps representing a reverse (leaf-first) tree
        # key=resourceid (str) val=set of concept resourceids (str)
        self.broader_concepts: dict[str, set[str]] = defaultdict(set)
        # key=resourceid (str) val=set of scheme resourceids (str)
        self.schemes_by_top_concept: dict[str, set[str]] = defaultdict(set)

        self.top_concepts_map()
        self.narrower_concepts_map()
        self.populate_schemes()

        self.polyhierarchical_concepts = set()
        self.language_lookup = {lang.name: lang.code for lang in Language.objects.all()}

    @staticmethod
    def find_valuetype_id_from_value(value):
        if value == PREF_LABEL_VALUE:
            return "prefLabel"
        if value == ALT_LABEL_VALUE:
            return "altLabel"
        if value == HIDDEN_LABEL_VALUE:
            return "hidden"
        return "unknown"

    def find_language_id_from_value(self, value):
        return self.language_lookup.get(value, value)

    @staticmethod
    def resources_from_tiles(lookup_expression: str):
        return CombinedExpression(
            JsonbArrayElements(F(lookup_expression)),
            "->>",
            Value("resourceId"),
            output_field=CharField(),
        )

    @staticmethod
    def labels_subquery(label_nodegroup):
        if label_nodegroup == SCHEME_NAME_NODEGROUP:
            # Annotating a ResourceInstance
            outer = OuterRef("resourceinstanceid")
            nodegroup_id = SCHEME_NAME_NODEGROUP
            type_node = SCHEME_NAME_TYPE_NODE
            language_node = SCHEME_NAME_LANGUAGE_NODE
        else:
            # Annotating a Tile
            outer = OuterRef("resourceinstance_id")
            nodegroup_id = CONCEPT_NAME_NODEGROUP
            type_node = CONCEPT_NAME_TYPE_NODE
            language_node = CONCEPT_NAME_LANGUAGE_NODE

        return ArraySubquery(
            TileModel.objects.filter(
                resourceinstance_id=outer, nodegroup_id=nodegroup_id
            )
            .exclude(**{f"data__{type_node}": None})
            .exclude(**{f"data__{language_node}": None})
            .values("data")
        )

    def top_concepts_map(self):
        top_concept_of_tiles = (
            TileModel.objects.filter(nodegroup_id=TOP_CONCEPT_OF_NODE_AND_NODEGROUP)
            .annotate(top_concept_of=self.resources_from_tiles(TOP_CONCEPT_OF_LOOKUP))
            .annotate(labels=self.labels_subquery(CONCEPT_NAME_NODEGROUP))
            .values("resourceinstance_id", "top_concept_of", "labels")
        )
        for tile in top_concept_of_tiles:
            scheme_id = tile["top_concept_of"]
            top_concept_id = str(tile["resourceinstance_id"])
            self.top_concepts[scheme_id].add(top_concept_id)
            self.schemes_by_top_concept[top_concept_id].add(scheme_id)
            self.labels[top_concept_id] = tile["labels"]

    def narrower_concepts_map(self):
        broader_concept_tiles = (
            TileModel.objects.filter(nodegroup_id=CLASSIFICATION_STATUS_NODEGROUP)
            .annotate(broader_concept=self.resources_from_tiles(BROADER_LOOKUP))
            .annotate(labels=self.labels_subquery(CONCEPT_NAME_NODEGROUP))
            .values("resourceinstance_id", "broader_concept", "labels")
        )
        for tile in broader_concept_tiles.iterator():
            broader_concept_id = tile["broader_concept"]
            narrower_concept_id: str = str(tile["resourceinstance_id"])
            self.narrower_concepts[broader_concept_id].add(narrower_concept_id)
            self.broader_concepts[narrower_concept_id].add(broader_concept_id)
            self.labels[narrower_concept_id] = tile["labels"]

    def populate_schemes(self):
        self.schemes = ResourceInstance.objects.filter(
            graph_id=SCHEMES_GRAPH_ID
        ).annotate(labels=self.labels_subquery(SCHEME_NAME_NODEGROUP))

    def lookup_scheme(self, scheme_id: str):
        schemes = [scheme for scheme in self.schemes if str(scheme.pk) == scheme_id]
        return schemes[0] if schemes else None

    def serialize_scheme(self, scheme: ResourceInstance, *, children=True):
        scheme_id: str = str(scheme.pk)
        data = {
            "id": scheme_id,
            "labels": [self.serialize_scheme_label(label) for label in scheme.labels],
        }
        if children:
            data["top_concepts"] = [
                self.serialize_concept(concept_id)
                for concept_id in sorted(self.top_concepts[scheme_id])
            ]
        return data

    def serialize_scheme_label(self, label_tile: dict):
        scheme_name_type_labels = [
            ReferenceLabel(**label)
            for label in label_tile[SCHEME_NAME_TYPE_NODE][0]["labels"]
        ]
        valuetype_id = self.find_valuetype_id_from_value(
            ListItem.find_best_label_from_set(scheme_name_type_labels)
        )
        language_labels = [
            ReferenceLabel(**label)
            for label in label_tile[SCHEME_NAME_LANGUAGE_NODE][0]["labels"]
        ]
        language_id = self.find_language_id_from_value(
            ListItem.find_best_label_from_set(language_labels)
        )
        value = label_tile[SCHEME_NAME_CONTENT_NODE] or _("Unknown")
        return {
            "valuetype_id": valuetype_id,
            "language_id": language_id,
            "value": value,
        }

    def serialize_concept(self, conceptid: str, *, parents=False, children=True):
        data = {
            "id": conceptid,
            "labels": [
                self.serialize_concept_label(label) for label in self.labels[conceptid]
            ],
        }
        if children:
            data["narrower"] = [
                self.serialize_concept(child_id)
                for child_id in sorted(self.narrower_concepts[conceptid])
            ]
        if parents:
            paths = self.find_paths_to_root([conceptid], conceptid)
            if len(paths) > 1:
                self.polyhierarchical_concepts.add(conceptid)

            data["parents"] = []
            for scheme_id, *parent_concept_ids in paths:
                scheme_object = self.lookup_scheme(scheme_id)
                if scheme_object is None:
                    # skip any path whose scheme_id isn’t found
                    continue

                serialized_scheme = self.serialize_scheme(scheme_object, children=False)
                serialized_parent_concepts = [
                    self.serialize_concept(parent_concept_id, children=False)
                    for parent_concept_id in parent_concept_ids
                ]

                data["parents"].append([serialized_scheme] + serialized_parent_concepts)

            self_and_parent_ids = set()
            for path in paths:
                self_and_parent_ids |= set(path)
            data["polyhierarchical"] = bool(
                self_and_parent_ids.intersection(self.polyhierarchical_concepts)
            )

        return data

    def find_paths_to_root(self, working_path, conceptid) -> list[list[str]]:
        """Return an array of paths (path: an array of scheme & concept ids)."""
        concept_and_scheme_parents = sorted(self.broader_concepts[conceptid]) + sorted(
            self.schemes_by_top_concept[conceptid]
        )

        collected_paths = []
        for parent in concept_and_scheme_parents:
            forked_path = working_path[:]
            forked_path.insert(0, parent)
            collected_paths.extend(self.find_paths_to_root(forked_path, parent))

        if concept_and_scheme_parents:
            return collected_paths
        return [working_path]

    def serialize_concept_label(self, label_tile: dict):
        scheme_name_type_labels = [
            ReferenceLabel(**label)
            for label in label_tile[CONCEPT_NAME_TYPE_NODE][0]["labels"]
        ]
        valuetype_id = self.find_valuetype_id_from_value(
            ListItem.find_best_label_from_set(scheme_name_type_labels)
        )
        language_labels = [
            ReferenceLabel(**label)
            for label in label_tile[CONCEPT_NAME_LANGUAGE_NODE][0]["labels"]
        ]
        language_id = self.find_language_id_from_value(
            ListItem.find_best_label_from_set(language_labels)
        )
        value = label_tile[CONCEPT_NAME_CONTENT_NODE] or _("Unknown")
        return {
            "valuetype_id": valuetype_id,
            "language_id": language_id,
            "value": value,
        }
