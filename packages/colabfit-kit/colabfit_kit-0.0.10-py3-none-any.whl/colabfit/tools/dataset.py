import datetime
import warnings

import dateutil
#import pyspark.sql.functions as sf
#from pyspark.sql.types import StringType
from unidecode import unidecode

from colabfit import MAX_STRING_LENGTH
#from colabfit.tools.schema import dataset_schema
from colabfit.tools.utilities import ELEMENT_MAP, _empty_dict_from_schema, _hash

import numpy as np


class Dataset:
    """
    A dataset defines a group of configuration sets and computed properties, and
    aggregates information about those configuration sets and properties.

    Attributes:

        configuration_set_ids (list):
            A list of attached configuration sets

        property_ids (list):
            A list of attached properties

        name (str):
            The name of the dataset

        authors (list or str or None):
            The names of the authors of the dataset.

        links (list or str or None):
            External links (e.g., journal articles, Git repositories, ...)
            to be associated with the dataset.

        description (str or None):
            A human-readable description of the dataset.

        aggregated_info (dict):
            A dictionary of information that was aggregated rom all of the
            attached configuration sets and properties. Contains the following
            information:

                From the configuration sets:
                    nconfigurations
                    nsites
                    nelements
                    chemical_systems
                    elements
                    individual_elements_ratios
                    total_elements_ratios
                    configuration_labels
                    configuration_labels_counts
                    chemical_formula_reduced
                    chemical_formula_anonymous
                    chemical_formula_hill
                    nperiodic_dimensions
                    dimension_types

                From the properties:
                    property_types
                    property_fields
                    methods
                    methods_counts
                    property_labels
                    property_labels_counts

        data_license (str):
            License associated with the Dataset's data
    """

    def __init__(
        self,
        name: str,
        authors: list[str],
        publication_link: str,
        data_link: str,
        description: str,
        config_df,
        prop_df,
        property_definitions,
        other_links: list[str] = None,
        dataset_id: str = None,
        labels: list[str] = None,
        doi: str = None,
        configuration_set_ids: list[str] = [],
        data_license: str = "CC-BY-ND-4.0",
        publication_year: str = None,
        use_pg: bool = False,
    ):
        for auth in authors:
            if not "".join(auth.split(" ")[-1].replace("-", "")).isalpha():
                raise RuntimeError(
                    f"Bad author name '{auth}'. Author names "
                    "can only contain [a-z][A-Z]"
                )

        self.property_definitions = property_definitions
        self.name = name
        self.authors = authors
        self.publication_link = publication_link
        self.data_link = data_link
        self.other_links = other_links
        self.description = description
        self.data_license = data_license
        self.dataset_id = dataset_id
        self.doi = doi
        self.publication_year = publication_year
        self.configuration_set_ids = configuration_set_ids
        if self.configuration_set_ids is None:
            self.configuration_set_ids = []
        if use_pg:
            self.spark_row = self._from_pg(configs=config_df, props=prop_df)
        else:
            self.spark_row = self.to_spark_row(config_df=config_df, prop_df=prop_df)

        self.spark_row["id"] = self.dataset_id
        # if dataset_id is None:
        #     raise ValueError("Dataset ID must be provided")
        id_prefix = "__".join(
            [
                self.name,
                "-".join([unidecode(auth.split()[-1]) for auth in authors]),
            ]
        )
        if len(id_prefix) > (MAX_STRING_LENGTH - len(dataset_id) - 2):
            id_prefix = id_prefix[: MAX_STRING_LENGTH - len(dataset_id) - 2]
            warnings.warn(f"ID prefix is too long. Clipping to {id_prefix}")
        extended_id = f"{id_prefix}__{dataset_id}"
        self.spark_row["extended_id"] = extended_id
        self._hash = _hash(self.spark_row, ["extended_id"])
        self.spark_row["hash"] = str(self._hash)
        self.spark_row["labels"] = labels
        
    # aggregate stuff
    def _from_pg(self, configs, props):
        row_dict = {}
        row_dict["last_modified"] = dateutil.parser.parse(
            datetime.datetime.now(tz=datetime.timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            ))
        row_dict["nconfiguration_sets"] = len(self.configuration_set_ids)
        row_dict['nconfigurations'] = len(props)
        row_dict['nproperty_objects'] = len(props)
        nsites = 0
        nperiodic_dimensions = set()
        dimension_types = set()
        element_dict = {} 

        # TODO: Streamline this
        for p in props:
            co_id = p['configuration_id']
            

            for c in configs:
                if c['id'] == co_id:
                    nsites += c['nsites']
                    for e in c['atomic_numbers']:
                       e = ELEMENT_MAP[e] 
                       if e in element_dict:
                            element_dict[e] += 1
                       else:
                            element_dict[e] = 1
                    nperiodic_dimensions.add(c['nperiodic_dimensions'])
                    dimension_types.add(str(c['dimension_types']))

        sorted_elements = sorted(list(element_dict.keys()))

        row_dict['nsites'] = nsites
        row_dict['nelements'] = len(sorted_elements)
        row_dict['elements'] = sorted_elements
        row_dict['total_elements_ratio'] = [element_dict[e] / nsites for e in sorted_elements]
        row_dict['nperiodic_dimensions'] = list(nperiodic_dimensions)
        row_dict['dimension_types'] = list(dimension_types)

        forces = 0
        stress = 0
        energy = 0
        energies = []
        
        # TODO: Below
        prop_def_map = {}
        prop_counts = {}
        # find available props from PD table
        for pd in self.property_definitions:
            # grab first property key name
            for k,v in pd.items():
                if k not in ['property-id', 'property-name', 'property-title', 'property-description']:
                    prop_def_map[f"{pd['property-name'].replace('-','_')}_{k.replace('-','_')}"] = pd['property-name']
                    prop_counts[f"{pd['property-name'].replace('-','_')}_{k.replace('-','_')}"] = 0
                    break

        for p in props:
            for k in p.keys():
                if str(k) in prop_counts:
                    if p[str(k)] is not None:
                        prop_counts[str(k)] += 1
            if p["atomic_forces_forces"] is not None:
                forces += 1
            if p["cauchy_stress_stress"] is not None:
                stress += 1
            if p["energy_energy"] is not None:
                energy += 1
                energies.append(p["energy_energy"])
        # TODO: iterate over counts if >0 add to available_properties
        available_props = []
        for k,v in prop_counts.items():
            if v > 0:
                available_props.append(prop_def_map[k])
        print (available_props)
        row_dict['available_properties'] = available_props
        row_dict['energy_mean'] = np.mean(energies)
        row_dict['energy_variance'] = np.var(energies)
        row_dict['atomic_forces_count'] = forces
        row_dict['cauchy_stress_count'] = stress
        row_dict['energy_count'] = energy
        row_dict["authors"] = self.authors
        row_dict["description"] = self.description
        row_dict["license"] = self.data_license
        row_dict["links"] = str(
            {
                "source-publication": self.publication_link,
                "source-data": self.data_link,
                "other": self.other_links,
            }
        )
        row_dict["name"] = self.name
        row_dict["publication_year"] = self.publication_year
        row_dict["doi"] = self.doi

        return row_dict

    def to_spark_row(self, config_df, prop_df):
        """"""
        row_dict = _empty_dict_from_schema(dataset_schema)
        row_dict["last_modified"] = dateutil.parser.parse(
            datetime.datetime.now(tz=datetime.timezone.utc).strftime(
                "%Y-%m-%dT%H:%M:%SZ"
            )
        )
        row_dict["nconfiguration_sets"] = len(self.configuration_set_ids)
        config_df = (
            config_df.withColumnRenamed("id", "configuration_id")
            .withColumnRenamed("hash", "config_hash")
            .select(
                "configuration_id",
                "elements",
                "atomic_numbers",
                "nsites",
                "nperiodic_dimensions",
                "dimension_types",
                # "labels",
            )
        )
        nproperty_objects = prop_df.count()
        # co_po_df = prop_df.select(
        #     "configuration_id",
        #     # "multiplicity",
        #     "atomization_energy",
        #     "atomic_forces_00",
        #     "adsorption_energy",
        #     "electronic_band_gap",
        #     "cauchy_stress",
        #     "formation_energy",
        #     "energy",
        # ).join(config_df, on="configuration_id", how="inner")
        # print(co_po_df.columns)
        # print(co_po_df.count())
        # print(co_po_df.first())
        # co_po_df = co_po_df.withColumn(
        #     "nsites_multiple", sf.col("nsites") * sf.col("multiplicity")
        # )
        # row_dict["nsites"] = co_po_df.agg({"nsites_multiple": "sum"}).first()[0]
        row_dict["nsites"] = config_df.agg({"nsites": "sum"}).first()[0]
        row_dict["nproperty_objects"] = nproperty_objects
        row_dict["elements"] = sorted(
            config_df.withColumn("exploded_elements", sf.explode("elements"))
            .agg(sf.collect_set("exploded_elements").alias("exploded_elements"))
            .select("exploded_elements")
            .take(1)[0][0]
        )
        row_dict["nelements"] = len(row_dict["elements"])
        atomic_ratios_df = (
            config_df.select("atomic_numbers")
            #     co_po_df.select("atomic_numbers", "multiplicity")
            #     .withColumn(
            #         "repeated_numbers",
            #         sf.expr(
            #            "transform(atomic_numbers, x -> array_repeat(x, multiplicity))"
            #         ),
            #     )
            # .withColumn("single_element", sf.explode(sf.flatten("repeated_numbers")))
            .withColumn("single_element", sf.explode("atomic_numbers"))
        )
        total_elements = atomic_ratios_df.count()
        assert total_elements == row_dict["nsites"]
        atomic_ratios_df = atomic_ratios_df.groupBy("single_element").count()
        atomic_ratios_df = atomic_ratios_df.withColumn(
            "ratio", sf.col("count") / total_elements
        )

        atomic_ratios_coll = (
            atomic_ratios_df.withColumn(
                "element",
                sf.udf(lambda x: ELEMENT_MAP[x], StringType())(
                    sf.col("single_element")
                ),
            )
            .select("element", "ratio")
            .collect()
        )
        row_dict["total_elements_ratios"] = [
            x[1] for x in sorted(atomic_ratios_coll, key=lambda x: x["element"])
        ]

        row_dict["nperiodic_dimensions"] = config_df.agg(
            sf.collect_set("nperiodic_dimensions")
        ).collect()[0][0]

        row_dict["dimension_types"] = config_df.agg(
            sf.collect_set("dimension_types")
        ).collect()[0][0]

        for prop in [
            "atomization_energy",
            "atomic_forces_00",
            "adsorption_energy",
            "electronic_band_gap",
            "cauchy_stress",
            "formation_energy",
            "energy",
        ]:
            row_dict[f"{prop}_count"] = (
                prop_df.select(prop).where(f"{prop} is not null").count()
            )
        row_dict["atomic_forces_count"] = row_dict.pop("atomic_forces_00_count")

        prop = "energy"
        row_dict[f"{prop}_variance"] = (
            prop_df.select(prop).where(f"{prop} is not null").agg(sf.variance(prop))
        ).first()[0]
        row_dict[f"{prop}_mean"] = (
            prop_df.select(prop).where(f"{prop} is not null").agg(sf.mean(prop))
        ).first()[0]

        row_dict["nconfigurations"] = prop_df.count()
        row_dict["authors"] = self.authors
        row_dict["description"] = self.description
        row_dict["license"] = self.data_license
        row_dict["links"] = str(
            {
                "source-publication": self.publication_link,
                "source-data": self.data_link,
                "other": self.other_links,
            }
        )
        row_dict["name"] = self.name
        row_dict["publication_year"] = self.publication_year
        row_dict["doi"] = self.doi

        return row_dict

    # @staticmethod
    # def __hash__(self):
    #     sha = sha512()
    #     sha.update(self.name.encode("utf-8"))
    #     return int(sha.hexdigest(), 16)

    def __str__(self):
        return (
            f"Dataset(description='{self.description}', "
            f"nconfiguration_sets={len(self.spark_row['configuration_sets'])}, "
            f"nproperty_objects={self.spark_row['nproperty_objects']}, "
            f"nconfigurations={self.spark_row['nconfigurations']}"
        )

    def __repr__(self):
        return str(self)
