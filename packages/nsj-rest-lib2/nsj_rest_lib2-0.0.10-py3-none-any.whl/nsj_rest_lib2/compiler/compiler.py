import re
from typing import Any

from nsj_rest_lib2.compiler.compiler_structures import (
    IndexCompilerStructure,
    PropertiesCompilerStructure,
)
from nsj_rest_lib2.compiler.dto_compiler import DTOCompiler
from nsj_rest_lib2.compiler.edl_model.primitives import REGEX_EXTERNAL_REF
from nsj_rest_lib2.compiler.edl_model.repository_model import RepositoryModel
from nsj_rest_lib2.compiler.entity_compiler import EntityCompiler
from nsj_rest_lib2.compiler.property_compiler import EDLPropertyCompiler

from nsj_rest_lib2.compiler.edl_model.entity_model import EntityModel

from nsj_rest_lib2.settings import get_logger

# TODO Autenticação nas rotas
# TODO Carregar, dinamicamente, em memória, o código compilado das dependÊncias por relacionamento
# TODO Atualizar o status da entidade pelo worker de compilação (e talvez parar uma compilação, quando se delete uma entidade)
# TODO Relacionamentos
# TODO Classes Abstratas
# TODO Partial Classes
# TODO Migrations
# TODO Adicionar autenticação aos endpoints dinâmicos
# TODO Criar imagem docker base para as aplicações, usando venv (para poderem atualizar o pydantic)


class CompilerResult:
    def __init__(self):
        self.dto_class_name: str | None = None
        self.dto_code: str | None = None
        self.entity_class_name: str | None = None
        self.entity_code: str | None = None
        self.api_expose: bool | None = None
        self.api_resource: str | None = None
        self.api_verbs: list[str] | None = None


class EDLCompiler:
    def __init__(self) -> None:
        self._properties_compiler = EDLPropertyCompiler()
        self._dto_compiler = DTOCompiler()
        self._entity_compiler = EntityCompiler()

    def compile_models(
        self, entity_models: dict[str, EntityModel]
    ) -> list[CompilerResult]:

        compiler_results = []
        for entity_model_id in entity_models:
            entity_model = entity_models[entity_model_id]
            if not entity_model.abstract:
                compiler_result = self._compile_model(entity_model, entity_models)
                compiler_results.append(compiler_result)

        return compiler_results

    def compile_model_from_edl(
        self,
        edl_json: dict[str, Any],
        dependencies_edls: list[dict[str, Any]],
    ) -> CompilerResult:
        entity_model = EntityModel(**edl_json)

        entity_models = []
        for dependency_edl in dependencies_edls:
            dependency_entity_model = EntityModel(**dependency_edl)
            entity_models.append(dependency_entity_model)

        return self.compile_model(entity_model, entity_models)

    def compile_model(
        self,
        entity_model: EntityModel,
        dependencies_models: list[EntityModel],
    ) -> CompilerResult:
        entity_models = {}
        for dependency_entity_model in dependencies_models:
            complete_entity_id = (
                f"{dependency_entity_model.escopo}/{dependency_entity_model.id}"
            )
            entity_models[complete_entity_id] = dependency_entity_model

        return self._compile_model(entity_model, entity_models)

    def _compile_model(
        self,
        entity_model: EntityModel,
        entity_models: dict[str, EntityModel],
    ) -> CompilerResult:

        # Criando um mapa de índices por nome de property
        # TODO Implementar tratamento dos índices de apoio às query (não de unicidade)
        map_indexes_by_property: dict[str, list[IndexCompilerStructure]] = {}
        map_unique_by_property: dict[str, IndexCompilerStructure] = {}
        self._make_unique_map_by_property(
            map_indexes_by_property, map_unique_by_property, entity_model, entity_models
        )

        # Criando uma cópia das coleções necessárias à compilação das properties
        # (a ideia é ser possível alterar as coleções sem afetar a entidade modelo,
        # o que será necessário para o tratamento de traits, etc - os quais serão
        # uma classe nova, resultado da união dessas propriedades).
        properties_structure = PropertiesCompilerStructure()
        self._make_properties_structures(
            properties_structure, entity_model, entity_models
        )

        # Criando a lista de atributos do DTO e da Entity; e recuperando as chaves primarias
        (
            ast_dto_attributes,
            ast_entity_attributes,
            props_pk,
            enum_classes,
            related_imports,
        ) = self._properties_compiler.compile(
            properties_structure,
            map_unique_by_property,
            entity_model,
            entity_models,
        )

        # Gerando o código do DTO
        dto_class_name, code_dto = self._dto_compiler.compile(
            entity_model, ast_dto_attributes, enum_classes, related_imports
        )

        # Gerando o código da Entity
        entity_class_name, code_entity = self._entity_compiler.compile(
            entity_model, ast_entity_attributes, props_pk
        )

        # Construindo o resultado
        compiler_result = CompilerResult()
        compiler_result.entity_class_name = entity_class_name
        compiler_result.entity_code = code_entity
        compiler_result.dto_class_name = dto_class_name
        compiler_result.dto_code = code_dto

        # Compilando questões das APIs
        compiler_result.api_expose = entity_model.api.expose
        compiler_result.api_resource = entity_model.api.resource
        compiler_result.api_verbs = entity_model.api.verbs

        return compiler_result

    def _make_properties_structures(
        self,
        properties_structure: PropertiesCompilerStructure,
        entity_model: EntityModel,
        entity_models: dict[str, EntityModel],
    ):
        if not entity_model:
            return

        # Populando com as propriedades do trait
        if entity_model.trait_from:
            trait_model = entity_models[entity_model.trait_from]

            self._make_properties_structures(
                properties_structure,
                trait_model,
                entity_models,
            )

        # Populando com as propriedades da entidade atual
        properties_structure.properties.update(entity_model.properties)
        if entity_model.main_properties:
            properties_structure.main_properties.extend(entity_model.main_properties)
        if entity_model.required:
            properties_structure.required.extend(entity_model.required)
        if entity_model.partition_data:
            properties_structure.partition_data.extend(entity_model.partition_data)
        if entity_model.search_properties:
            properties_structure.search_properties.extend(
                entity_model.search_properties
            )
        if entity_model.metric_label:
            properties_structure.metric_label.extend(entity_model.metric_label)

        if entity_model.trait_properties:
            properties_structure.trait_properties.update(entity_model.trait_properties)

        if entity_model.repository.properties:
            properties_structure.entity_properties.update(
                entity_model.repository.properties
            )

    def _make_unique_map_by_property(
        self,
        map_indexes_by_property: dict[str, list[IndexCompilerStructure]],
        map_unique_by_property: dict[str, IndexCompilerStructure],
        entity_model: EntityModel,
        entity_models: dict[str, EntityModel],
        deep: int = 1,
    ):

        if not entity_model:
            return

        # Varrendo e organizando os índices
        if entity_model.repository.indexes:
            for index in entity_model.repository.indexes:
                for pkey in index.columns:
                    if index.unique:
                        if pkey in map_unique_by_property:
                            if deep > 1:
                                get_logger().warning(
                                    f"Propriedade '{pkey}' possui mais de um índice de unicidade (sendo um herdado). Por isso a replicação (herdada) será ignorada."
                                )
                                continue
                            else:
                                raise Exception(
                                    f"Propriedade '{pkey}' possui mais de um índice de unicidade."
                                )  # TODO Verificar esse modo de tratar erros

                        map_unique_by_property[pkey] = IndexCompilerStructure(
                            index, deep > 1
                        )
                    else:
                        list_index = map_indexes_by_property.setdefault(pkey, [])
                        list_index.append(IndexCompilerStructure(index, deep > 1))

        # Populando com as propriedades do trait
        if entity_model.trait_from:
            trait_model = entity_models[entity_model.trait_from]

            self._make_unique_map_by_property(
                map_indexes_by_property,
                map_unique_by_property,
                trait_model,
                entity_models,
                deep=deep + 1,
            )

    def list_dependencies(
        self, edl_json: dict[str, Any]
    ) -> tuple[list[str], EntityModel]:
        entity_model = EntityModel(**edl_json)

        return (self._list_dependencies(entity_model), entity_model)

    def _list_dependencies(self, entity_model: EntityModel) -> list[str]:
        entities: list[str] = []

        if entity_model.trait_from:
            entities.append(entity_model.trait_from)

        # Populando com as dependências de propriedades de relacionamento 1_N
        for pkey in entity_model.properties:
            prop = entity_model.properties[pkey]

            if isinstance(prop.type, str):
                external_match = re.match(REGEX_EXTERNAL_REF, prop.type)
                if external_match:
                    external_dependency = external_match.group(0)
                    entities.append(external_dependency)

        return entities


def get_files_from_directory(directory):
    files = []
    for file in os.listdir(directory):
        if file.endswith(".json") or file.endswith(".yml") or file.endswith(".yaml"):
            files.append(os.path.join(directory, file))
    return files


if __name__ == "__main__":
    import argparse
    import json
    import os
    import yaml

    parser = argparse.ArgumentParser(
        description="Compila arquivos EDL para classes Python"
    )
    parser.add_argument(
        "-d",
        "--directory",
        help="Diretório com arquivos .json para compilar",
        type=str,
        required=True,
    )
    args = parser.parse_args()

    files = get_files_from_directory(args.directory)

    entities = {}
    for file in files:
        with open(file, "r") as f:
            if file.endswith(".json"):
                edl = json.load(f)
            else:
                edl = yaml.safe_load(f)

        # Instanciando o objeto de modelo de entidade a partir do JSON,
        # e já realizando as validações básicas de tipo e estrutura.
        print(f"Validando arquivo: {file}")
        entity_model = EntityModel(**edl)

        complete_entity_id = f"{entity_model.escopo}/{entity_model.id}"
        entities[complete_entity_id] = entity_model

    compiler = EDLCompiler()
    compiler_results = compiler.compile_models(entities)

    for compiler_result in compiler_results:
        print("==========================================================")
        print(f"Entity: {compiler_result.entity_class_name}")
        print(f"{compiler_result.entity_code}")
        print("\n")
        print("==========================================================")
        print(f"DTO: {compiler_result.dto_class_name}")
        print(f"{compiler_result.dto_code}")
        print("\n")

        print("==========================================================")
        print("API Expose: ", compiler_result.api_expose)
        print("API Route Path: ", compiler_result.api_resource)
        print("API Verbs: ", compiler_result.api_verbs)
        print("==========================================================")
        print("\n")
