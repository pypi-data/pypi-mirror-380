import json
import hashlib
import os
from toposkg.converter.rml import toposkg_lib_triples_map
from toposkg.converter.rml import toposkg_lib_mapping_builder
from shapely.geometry import shape
from typing import Any, Dict

class GeoJSONMappingGenerator():
    def __init__(self, ontology_uri, resource_uri):
        self.ontology_uri = ontology_uri
        self.resource_uri = resource_uri
        self.generated_id = None
        self.parent_id = None
        self.intermediate_file = None
        self.data = None
        self.map_counter=0
        self.maps = []

    def _load(self) -> Any:
        """Load JSON content from file."""
        try:
            with open(self.intermediate_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {self.intermediate_file}: {e}")

    def add_ids_to_json(self, input_file: str):
        """Adds an incremental ID field to every dict in the JSON file,
        stores parent ID in each child, replaces any GeoJSON geometry dict
        (found under the 'geometry' key) with its WKT string, 
        and saves a new JSON file with a hashed prefix."""

        # Compute 16-byte hash (blake2b for consistency)
        base_name = os.path.basename(input_file)
        file_hash = hashlib.blake2b(base_name.encode("utf-8"), digest_size=16).hexdigest()
        output_file = os.path.join(
            os.path.dirname(input_file),
            f"_{file_hash}{base_name}"
        )

        # Load JSON
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        # Incremental ID counter
        counter = {"id": 0}

        def walk(node, parent_id=None):
            if isinstance(node, dict):
                # Assign ID
                current_id = counter["id"]
                node[self.generated_id] = current_id
                if parent_id is not None:
                    node[self.parent_id] = parent_id
                counter["id"] += 1

                # If node has a "geometry", replace it with WKT string
                if "geometry" in node and isinstance(node["geometry"], dict):
                    try:
                        geom = shape(node["geometry"])
                        node["geometry"] = geom.wkt
                    except Exception:
                        pass  # Leave unchanged if invalid geometry

                # Recurse into children
                for k, v in node.items():
                    if isinstance(v, (dict, list)):
                        walk(v, parent_id=current_id)

            elif isinstance(node, list):
                for v in node:
                    if isinstance(v, (dict, list)):
                        walk(v, parent_id=parent_id)

        # Walk and modify JSON
        walk(data)

        # Save updated JSON
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        return output_file
    
    def parse(self):
        features = self.data["features"]

        featuresMap = toposkg_lib_triples_map.TriplesMap(self.ontology_uri,self.resource_uri,"FeatureMap")
        featuresMap.add_logical_source(self.intermediate_file,"ql:JSONPath","$.features[*]")
        featuresMap.add_subject_map(self.generated_id)
        featuresMap.add_predicate_object_map_with_template("hasGeometry",self.resource_uri+"Geometry{_pyrml_mapper_generated_id}","ogc")

        geometriesMap = toposkg_lib_triples_map.TriplesMap("http://www.opengis.net/ont/geosparql#",self.resource_uri+"Geometry","GeometryMap")
        geometriesMap.add_logical_source(self.intermediate_file,"ql:JSONPath","$.features[*]")
        geometriesMap.add_subject_map(self.generated_id)
        geometriesMap.add_predicate_object_map("asWKT","geometry","wkt","ogc")
        self.maps += [geometriesMap]

        properties = []
        for feature_dict in features:
            properties += [feature_dict.get("properties", None)]

        childMap = self.list_pass(properties,"properties","$.features[*].properties")
        featuresMap.add_predicate_object_map_on_join("propertiesLink",childMap,self.generated_id,self.parent_id)
        self.maps += [featuresMap]
        self.maps += [childMap]
            



    #Helper methods
    def recursive_dict_pass(self, _dict : dict, key : str, iterator: str):
        #Initialize map for current pass
        name = key
        if name is not None:
            name = f"{key}{self.map_counter}"
            self.map_counter += 1

        triplesMap = toposkg_lib_triples_map.TriplesMap(self.ontology_uri, self.resource_uri, name)
        if iterator==None:
            iterator="$"
        triplesMap.add_logical_source(self.intermediate_file,"ql:JSONPath",iterator)
        triplesMap.add_subject_map(self.generated_id,key)

        for k,v in _dict.items():
            if k!="geometry":
                if isinstance(v, dict):
                    childMap = self.recursive_dict_pass(v, k, iterator + "." + k)
                    triplesMap.add_predicate_object_map_on_join(k,childMap,self.generated_id, self.parent_id)
                    self.maps += [childMap]
                elif isinstance(v, list):
                    childMap = self.list_pass(v, k, iterator + "." + k + "[*]")
                    if childMap!=None:
                        triplesMap.add_predicate_object_map_on_join(k,childMap,self.generated_id, self.parent_id)
                        self.maps += [childMap]
                #Literal case
                else:
                    triplesMap.add_predicate_object_map(k,k,v)

        return triplesMap

                    
    def list_pass(self, l : list, key : str, iterator: str):
        if not l:
            return None

        #Initialize map for current pass
        name = key
        if name is not None:
            name = f"{key}{self.map_counter}"
            self.map_counter += 1

        triplesMap = toposkg_lib_triples_map.TriplesMap(self.ontology_uri, self.resource_uri, name)
        if iterator==None:
            iterator="$[*]"
        triplesMap.add_logical_source(self.intermediate_file,"ql:JSONPath",iterator)
        triplesMap.add_subject_map(self.generated_id,key)
            
        common=set()
        for v in l:
            cur=set()
            if isinstance(v, dict):
                for inner_key,inner_value in v.items():
                    if inner_key!="geometry":
                        if isinstance(inner_value,list):
                            childMap = self.list_pass(inner_value, inner_key, iterator + "." + inner_key + "[*]")
                            if childMap!=None:
                                triplesMap.add_predicate_object_map_on_join(inner_key,childMap,self.generated_id, self.parent_id)
                                self.maps += [childMap]
                        elif isinstance(inner_value,dict):
                            childMap = self.recursive_dict_pass(inner_value, inner_key, iterator + "." + inner_key)
                            triplesMap.add_predicate_object_map_on_join(inner_key,childMap,self.generated_id, self.parent_id)
                            self.maps += [childMap]
                        else:
                            cur.add(inner_key)
                if not bool(common):
                    common = cur
                else:
                    common &= cur
            elif isinstance(v, list):
                childMap = self.list_pass(v, key, iterator + "." + key + "[*]")
                triplesMap.add_predicate_object_map_on_join(key,childMap,self.generated_id, self.parent_id)
                self.maps += [childMap]
            else:
                return None
            
        if not bool(common):
            return None
        else:
            for k in common:
                triplesMap.add_predicate_object_map(k,k,None)
        
        return triplesMap


    #Function to generate mapping
    def generate_default_mapping(self, input_data_source):
        base_name = os.path.basename(input_data_source)
        file_hash = hashlib.blake2b(base_name.encode("utf-8"), digest_size=16).hexdigest()
        self.generated_id = file_hash + "_pyrml_mapper_generated_id"
        self.parent_id = file_hash + "_pyrml_mapper_parent_id"

        self.intermediate_file = self.add_ids_to_json(input_data_source)
        self.data = self._load()
        self.parse()
        self.maps.reverse()
        builder = toposkg_lib_mapping_builder.RMLBuilder(self.ontology_uri,self.resource_uri,self.maps)
        return builder.export_as_string()