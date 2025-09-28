from pathlib import Path
from typing import Any, Dict

from datamodel_code_generator import load_yaml_from_path
from datamodel_code_generator.model import pydantic as pydantic_v1_model
from datamodel_code_generator.model import pydantic_v2 as pydantic_v2_model
from datamodel_code_generator.parser.jsonschema import (
    DataType,
    JsonSchemaObject,
    JsonSchemaParser,
    get_special_path,
)

# https://docs.pydantic.dev/1.10/usage/schema/#schema-customization
# https://docs.pydantic.dev/latest/concepts/json_schema/#using-json_schema_extra-with-a-dict
# https://docs.pydantic.dev/latest/concepts/json_schema/#field-level-customization


class PydanticV1Config(pydantic_v1_model.Config):
    # schema_extra: Optional[Dict[str, Any]] = None
    schema_extra: str = None


class PydanticV2Config(pydantic_v2_model.ConfigDict):
    # schema_extra: Optional[Dict[str, Any]] = None
    json_schema_extra: str = None


class OOLDJsonSchemaParser(JsonSchemaParser):
    """Custom parser for OO-LD schemas.
    You can use this class directly or monkey-patch the datamodel_code_generator module:
    `datamodel_code_generator.parser.jsonschema.JsonSchemaParser = OOLDJsonSchemaParser`
    """

    def set_additional_properties(self, name: str, obj: JsonSchemaObject) -> None:
        schema_extras = repr(obj.extras)  # keeps 'False' and 'True' boolean literals
        if self.data_model_type == pydantic_v1_model.BaseModel:
            self.extra_template_data[name]["config"] = PydanticV1Config(
                schema_extra=schema_extras
            )
        if self.data_model_type == pydantic_v2_model.BaseModel:
            self.extra_template_data[name]["config"] = PydanticV2Config(
                json_schema_extra=schema_extras
            )
        return super().set_additional_properties(name, obj)

    # fixes https://github.com/koxudaxi/datamodel-code-generator/issues/2403
    def parse_combined_schema(
        self,
        name: str,
        obj: JsonSchemaObject,
        path: list[str],
        target_attribute_name: str,
    ) -> list[DataType]:
        base_object = obj.dict(
            exclude={target_attribute_name}, exclude_unset=True, by_alias=True
        )
        # base_object["extras"] = obj.extras # rename to
        # '#-datamodel-code-generator-#-extras-#-special-#' by alias export
        # if "subprop0" in base_object["properties"]:
        #     base_object["properties"]["subprop0"]["extras"] = obj.extras
        combined_schemas: list[JsonSchemaObject] = []
        refs = []
        for index, target_attribute in enumerate(
            getattr(obj, target_attribute_name, [])
        ):
            if target_attribute.ref:
                combined_schemas.append(target_attribute)
                refs.append(index)
                # TODO: support partial ref
            else:
                # combined_schemas.append(
                #     self.SCHEMA_OBJECT_TYPE.parse_obj(
                #         self._deep_merge(
                #             base_object,
                #             target_attribute.dict(exclude_unset=True, by_alias=True)
                #         )
                #     )
                # )
                so = self.SCHEMA_OBJECT_TYPE.parse_obj(
                    self._deep_merge(
                        base_object,
                        target_attribute.dict(exclude_unset=True, by_alias=True),
                    )
                )
                if hasattr(so, "properties") and hasattr(obj, "properties"):
                    if so.properties is not None and obj.properties is not None:
                        for k, v in so.properties.items():
                            if k in obj.properties:
                                if obj.properties[k].extras:
                                    v.extras = self._deep_merge(
                                        v.extras, obj.properties[k].extras
                                    )
                            x_of_properties = getattr(
                                target_attribute, "properties", {}
                            )
                            if k in x_of_properties:
                                if x_of_properties[k].extras:
                                    v.extras = self._deep_merge(
                                        v.extras, x_of_properties[k].extras
                                    )
                combined_schemas.append(so)

        parsed_schemas = self.parse_list_item(
            name,
            combined_schemas,
            path,
            obj,
            singular_name=False,
        )
        common_path_keyword = f"{target_attribute_name}Common"
        return [
            self._parse_object_common_part(
                name,
                obj,
                [*get_special_path(common_path_keyword, path), str(i)],
                ignore_duplicate_model=True,
                fields=[],
                base_classes=[d.reference],
                required=[],
            )
            if i in refs and d.reference
            else d
            for i, d in enumerate(parsed_schemas)
        ]

    def parse_enum(
        self,
        name: str,
        obj: JsonSchemaObject,
        path: list[str],
        singular_name: bool = False,  # noqa: FBT001, FBT002
        unique: bool = True,  # noqa: FBT001, FBT002
    ) -> DataType:
        """Override to handle enum schemas - add enum descriptions as docstrings."""
        schema = super().parse_enum(name, obj, path, singular_name, unique)
        ref = schema.reference
        for r in self.results:
            if r.reference == ref:
                if "options" in obj.extras and "enum_titles" in obj.extras["options"]:
                    for i, v in enumerate(obj.extras["options"]["enum_titles"]):
                        if "description" not in r.fields[i].extras:
                            r.fields[i].extras["description"] = v
        return schema


class OOLDJsonSchemaParserFixedRefs(OOLDJsonSchemaParser):
    """Overwrite # overwrite the original `_get_ref_body_from_remote` function to fix
    wrongly composed paths. This issue occurs only when using this parser class directy
    and occurs not if used through mokey patching and
    `datamodel_code_generator.generate()`.
    Only relevant for schema refs in subdirs
    """

    def _get_ref_body_from_remote(self, resolved_ref: str) -> Dict[Any, Any]:
        # default behaviour:  full_path = self.base_path / resolved_ref
        # fix: merge the paths correctly:
        # resolved_ref:  'C:/Users/Example/Git/OO-LD/oold-python/src/oold/example/src/Bar.json' # noqa: E501
        # self.base_path 'C:/Users/Example/Git/OO-LD/oold-python/src/oold/example/src'
        # => full_path:  'C:/Users/Example/Git/OO-LD/oold-python/src/oold/example/src/Bar.json' # noqa: E501
        # resolved_ref:  'C:/Users/Example/Git/OO-LD/oold-python/src/oold/example/src/Users/Example/Git/OO-LD/oold-python/src/oold/example/src/bar2/Bar2.json' # noqa: E501
        # self.base_path 'C:/Users/Example/Git/OO-LD/oold-python/src/oold/example/src'
        # => full_path:  'C:/Users/Example/Git/OO-LD/oold-python/src/oold/example/src/bar2/Bar2.json' # noqa: E501

        # get path without drive and scheme, so that it works on Windows and Linux
        resolved_ref = Path(resolved_ref).as_posix()  # remove drive and scheme
        resolved_ref = resolved_ref.split(self.base_path.as_posix().split(":", 1)[-1])[
            -1
        ].lstrip(
            "/"
        )  # remove base path, leading '/'
        full_path = self.base_path / Path(resolved_ref)
        return self.remote_object_cache.get_or_put(
            str(full_path),
            default_factory=lambda _: load_yaml_from_path(full_path, self.encoding),
        )
