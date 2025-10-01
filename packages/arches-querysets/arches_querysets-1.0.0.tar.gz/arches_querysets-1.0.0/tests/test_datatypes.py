import json
from unittest.mock import Mock

from arches_querysets.models import ResourceTileTree
from arches_querysets.utils.tests import GraphTestCase


class DatatypeRepresentationTests(GraphTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        resources = ResourceTileTree.get_tiles(
            "datatype_lookups", as_representation=True
        )
        cls.resource_42 = resources.get(pk=cls.resource_42.pk)
        cls.resource_none = resources.get(pk=cls.resource_none.pk)
        cls.datatype_1 = cls.resource_42.aliased_data.datatypes_1
        cls.datatype_n = cls.resource_42.aliased_data.datatypes_n
        cls.datatype_1_none = cls.resource_none.aliased_data.datatypes_1
        cls.datatype_n_none = cls.resource_none.aliased_data.datatypes_n

    def test_as_representation_display_values(self):
        display_values = {
            # Start with the tile representation.
            **self.sample_data_1,
            # Some representations are different.
            # Boolean resolves to a string.
            "boolean": str(self.sample_data_1["boolean"]),
            # Number resolves to a string. TODO: localize?
            "number": str(self.sample_data_1["number"]),
            # String resolves to active language.
            "string": "forty-two",
            # Resource Instance{list} resolves to localized name.
            "resource-instance": "Resource referencing 42",
            "resource-instance-list": "Resource referencing 42",
            # Concept{list} resolves to concept value.
            "concept": "Arches",
            "concept-list": "Arches",
            # Node value resolves to node value.
            "node-value": self.sample_data_1["date"],
            # URL resolves to the stringified dictionary.
            "url": json.dumps(self.sample_data_1["url"]),
            # File-list resolves to urls joined with " | ".
            "file-list": self.sample_data_1["file-list"][0]["url"],
        }

        # The representation is available on the nodegroup .aliased_data.
        for datatype, representation in display_values.items():
            node_alias = datatype.replace("-", "_") + "_alias"
            for resource_data, resource_data_none, cardinality in [
                (self.datatype_1.aliased_data, self.datatype_1_none.aliased_data, "1"),
                (
                    self.datatype_n[0].aliased_data,
                    self.datatype_n_none[0].aliased_data,
                    "n",
                ),
            ]:
                with self.subTest(datatype=datatype, cardinality=cardinality):
                    lookup = node_alias if cardinality == "1" else node_alias + "_n"
                    value = getattr(resource_data, lookup)
                    self.assertEqual(value.get("display_value"), representation)
                    value = getattr(resource_data_none, lookup)
                    self.assertEqual(value.get("display_value"), "")

    def test_as_representation_details(self):
        detail_values = {
            # Resource Instance & list details both resolve to an array of objects.
            "resource-instance": [
                {
                    "resource_id": str(self.resource_42.pk),
                    "display_value": self.resource_42.descriptors["en"]["name"],
                    # This can be extended as necessary via get_details()
                }
            ],
            "resource-instance-list": [
                {
                    "resource_id": str(self.resource_42.pk),
                    "display_value": self.resource_42.descriptors["en"]["name"],
                }
            ],
            # Same with concept & concept-list.
            "concept": [
                {
                    "valueid": "d8c60bf4-e786-11e6-905a-b756ec83dad5",
                    "concept_id": "00000000-0000-0000-0000-000000000001",
                    "valuetype_id": "prefLabel",
                    "value": "Arches",
                    "language_id": "en",
                }
            ],
            "concept-list": [
                {
                    "valueid": "d8c60bf4-e786-11e6-905a-b756ec83dad5",
                    "concept_id": "00000000-0000-0000-0000-000000000001",
                    "valuetype_id": "prefLabel",
                    "value": "Arches",
                    "language_id": "en",
                }
            ],
        }

        # The details are available on the nodegroup .aliased_data.
        for datatype, details in detail_values.items():
            node_alias = datatype.replace("-", "_") + "_alias"
            for resource_data, resource_data_none, cardinality in [
                (self.datatype_1.aliased_data, self.datatype_1_none.aliased_data, "1"),
                (
                    self.datatype_n[0].aliased_data,
                    self.datatype_n_none[0].aliased_data,
                    "n",
                ),
            ]:
                lookup = node_alias if cardinality == "1" else node_alias + "_n"
                if lookup == "node_value_alias_n":
                    details = self.sample_data_n["node-value"]
                with self.subTest(lookup=lookup):
                    value = getattr(resource_data, lookup)
                    self.assertEqual(value.get("details"), details)
                    value = getattr(resource_data_none, lookup)
                    if value.get("details") is not None:
                        self.assertEqual(value.get("details"), [])


class DatatypePythonTests(GraphTestCase):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        resources = ResourceTileTree.get_tiles(
            "datatype_lookups", as_representation=False
        )
        cls.resource = resources.get(pk=cls.resource_42.pk)
        cls.resource_none = resources.get(pk=cls.resource_none.pk)
        cls.datatype_1 = cls.resource.aliased_data.datatypes_1
        cls.datatype_n = cls.resource.aliased_data.datatypes_n
        cls.datatype_1_none = cls.resource_none.aliased_data.datatypes_1
        cls.datatype_n_none = cls.resource_none.aliased_data.datatypes_n

    def test_python_values(self):
        python_values = {
            # Start with the tile representation.
            **self.sample_data_1,
            # Some python values are different.
            # Resource Instances become model instances
            "resource-instance": self.resource_42,
            "resource-instance-list": [self.resource_42],
            # Concepts become concept value model instances
            "concept": self.concept_value,
            "concept-list": [self.concept_value],
        }

        # The python value is available on the nodegroup .aliased_data.
        for datatype, python_value in python_values.items():
            node_alias = datatype.replace("-", "_") + "_alias"
            for resource_data, resource_data_none, cardinality in [
                (self.datatype_1.aliased_data, self.datatype_1_none.aliased_data, "1"),
                (
                    self.datatype_n[0].aliased_data,
                    self.datatype_n_none[0].aliased_data,
                    "n",
                ),
            ]:
                lookup = node_alias if cardinality == "1" else node_alias + "_n"
                if lookup == "node_value_alias_n":
                    python_value = self.sample_data_n["node-value"]
                with self.subTest(lookup=lookup):
                    value = getattr(resource_data, lookup)
                    self.assertEqual(value, python_value)
                    value = getattr(resource_data_none, lookup)
                    self.assertIsNone(value, datatype)


class DatatypeMethodTests(GraphTestCase):
    def test_transform_value_for_tile(self):
        test_values = {
            # TODO - add more datatypes tests here.
            "file-list": [
                {
                    "input": "commma-separated-list.png,from-bulk-data-manager.jpg",
                    "output": [
                        {
                            "status": "uploaded",
                            "name": "commma-separated-list.png",
                            "type": "image/png",
                            "file_id": "b503428b-1e04-4c79-8188-f70837461a07",
                            "url": "/files/b503428b-1e04-4c79-8188-f70837461a07",
                            "accepted": True,
                            "renderer": "5e05aa2e-5db0-4922-8938-b4d2b7919733",
                        },
                        {
                            "status": "uploaded",
                            "name": "from-bulk-data-manager.jpg",
                            "type": "image/jpeg",
                            "file_id": "35a11db0-3796-4b25-becd-b369096a0942",
                            "url": "/files/35a11db0-3796-4b25-becd-b369096a0942",
                            "accepted": True,
                            "renderer": "5e05aa2e-5db0-4922-8938-b4d2b7919733",
                        },
                    ],
                    "equality_test": lambda list1, list2: list1[0].keys()
                    == list2[0].keys(),
                },
                {
                    "input": [
                        {
                            "status": "uploaded",
                            "name": "commma-separated-list.png",
                            "type": "image/png",
                            "file_id": "b503428b-1e04-4c79-8188-f70837461a07",
                            "url": "/files/b503428b-1e04-4c79-8188-f70837461a07",
                            "accepted": True,
                            "renderer": "5e05aa2e-5db0-4922-8938-b4d2b7919733",
                            "altText": {
                                "en": {
                                    "value": "Replaceable alt text",
                                    "direction": "ltr",
                                }
                            },
                            "attribution": {
                                "en": {
                                    "value": "",
                                    "direction": "ltr",
                                }
                            },
                            "description": {
                                "en": {
                                    "value": "",
                                    "direction": "ltr",
                                }
                            },
                            "title": {
                                "en": {
                                    "value": "",
                                    "direction": "ltr",
                                }
                            },
                        },
                        {
                            "status": "uploaded",
                            "name": "from-bulk-data-manager.jpg",
                            "type": "image/jpeg",
                            "file_id": "35a11db0-3796-4b25-becd-b369096a0942",
                            "url": "/files/35a11db0-3796-4b25-becd-b369096a0942",
                            "accepted": True,
                            "renderer": "5e05aa2e-5db0-4922-8938-b4d2b7919733",
                            "altText": {
                                "en": {
                                    "value": "Replaceable alt text",
                                    "direction": "ltr",
                                }
                            },
                            "attribution": {
                                "en": {
                                    "value": "",
                                    "direction": "ltr",
                                }
                            },
                            "description": {
                                "en": {
                                    "value": "",
                                    "direction": "ltr",
                                }
                            },
                            "title": {
                                "en": {
                                    "value": "",
                                    "direction": "ltr",
                                }
                            },
                        },
                    ],
                    "output": [
                        {
                            "status": "uploaded",
                            "name": "commma-separated-list.png",
                            "type": "image/png",
                            "file_id": "b503428b-1e04-4c79-8188-f70837461a07",
                            "url": "/files/b503428b-1e04-4c79-8188-f70837461a07",
                            "accepted": True,
                            "renderer": "5e05aa2e-5db0-4922-8938-b4d2b7919733",
                            "altText": {
                                "en": {
                                    "value": "Replaceable alt text",
                                    "direction": "ltr",
                                }
                            },
                            "attribution": {
                                "en": {
                                    "value": "",
                                    "direction": "ltr",
                                }
                            },
                            "description": {
                                "en": {
                                    "value": "",
                                    "direction": "ltr",
                                }
                            },
                            "title": {
                                "en": {
                                    "value": "",
                                    "direction": "ltr",
                                }
                            },
                        },
                        {
                            "status": "uploaded",
                            "name": "from-bulk-data-manager.jpg",
                            "type": "image/jpeg",
                            "file_id": "35a11db0-3796-4b25-becd-b369096a0942",
                            "url": "/files/35a11db0-3796-4b25-becd-b369096a0942",
                            "accepted": True,
                            "renderer": "5e05aa2e-5db0-4922-8938-b4d2b7919733",
                            "altText": {
                                "en": {
                                    "value": "Replaceable alt text",
                                    "direction": "ltr",
                                }
                            },
                            "attribution": {
                                "en": {
                                    "value": "",
                                    "direction": "ltr",
                                }
                            },
                            "description": {
                                "en": {
                                    "value": "",
                                    "direction": "ltr",
                                }
                            },
                            "title": {
                                "en": {
                                    "value": "",
                                    "direction": "ltr",
                                }
                            },
                        },
                    ],
                    "equality_test": lambda list1, list2: list1[0].keys()
                    == list2[0].keys(),
                },
            ],
            "resource-instance": [
                {
                    "input": self.resource_42.pk,  # test as uuid
                    "output": [
                        {
                            "resourceId": str(self.resource_42.pk),
                            "ontologyProperty": "",
                            "inverseOntologyProperty": "",
                        }
                    ],
                },
                {
                    "input": str(self.resource_42.pk),  # test as string
                    "output": [
                        {
                            "resourceId": str(self.resource_42.pk),
                            "ontologyProperty": "",
                            "inverseOntologyProperty": "",
                        }
                    ],
                },
                {
                    "input": self.resource_42,  # test as model instance
                    "output": [
                        {
                            "resourceId": str(self.resource_42.pk),
                            "ontologyProperty": "",
                            "inverseOntologyProperty": "",
                        }
                    ],
                },
                {
                    "input": json.dumps(
                        [
                            {  # test as stringified dict
                                "resourceId": str(self.resource_42.pk),
                                "ontologyProperty": "testProperty",
                                "inverseOntologyProperty": "testInverseProperty",
                            }
                        ]
                    ),
                    "output": [
                        {
                            "resourceId": str(self.resource_42.pk),
                            "ontologyProperty": "testProperty",
                            "inverseOntologyProperty": "testInverseProperty",
                        }
                    ],
                },
                {
                    "input": [
                        {  # test as dict
                            "resourceId": str(self.resource_42.pk),
                            "ontologyProperty": "testProperty",
                            "inverseOntologyProperty": "testInverseProperty",
                        }
                    ],
                    "output": [
                        {
                            "resourceId": str(self.resource_42.pk),
                            "ontologyProperty": "testProperty",
                            "inverseOntologyProperty": "testInverseProperty",
                        }
                    ],
                },
            ],
            "resource-instance-list": [
                {
                    "input": [self.resource_42.pk],
                    "output": [
                        {
                            "resourceId": str(self.resource_42.pk),
                            "ontologyProperty": "",
                            "inverseOntologyProperty": "",
                        }
                    ],
                }
            ],
        }

        for datatype, cases in test_values.items():
            for value in cases:
                with self.subTest(datatype=datatype, value=value["input"]):
                    datatype_instance = self.datatype_factory.get_instance(
                        datatype=datatype
                    )
                    transformed_value = datatype_instance.transform_value_for_tile(
                        value["input"], is_existing_tile=False
                    )
                    if equality_test := value.get("equality_test"):
                        self.assertTrue(
                            equality_test(transformed_value, value["output"])
                        )
                    else:
                        self.assertEqual(transformed_value, value["output"])
