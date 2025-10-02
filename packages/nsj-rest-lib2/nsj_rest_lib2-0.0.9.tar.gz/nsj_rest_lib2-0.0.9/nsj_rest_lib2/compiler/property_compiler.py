import ast
import re

from nsj_rest_lib2.compiler.compiler_structures import (
    IndexCompilerStructure,
    PropertiesCompilerStructure,
)
from nsj_rest_lib2.compiler.edl_model.entity_model import EntityModel
from nsj_rest_lib2.compiler.edl_model.primitives import (
    CardinalityTypes,
    PrimitiveTypes,
    REGEX_EXTERNAL_REF,
    REGEX_INTERNAL_REF,
)
from nsj_rest_lib2.compiler.edl_model.property_meta_model import PropertyMetaModel
from nsj_rest_lib2.compiler.util.str_util import CompilerStrUtil
from nsj_rest_lib2.compiler.util.type_naming_util import (
    compile_dto_class_name,
    compile_entity_class_name,
    compile_namespace_keys,
)
from nsj_rest_lib2.compiler.util.type_util import TypeUtil

# TODO pattern
# TODO lowercase
# TODO uppercase
# TODO Adicionar o nome da entidade, no nome das classes de enum (para evitar conflitos no caso das traits)


class EDLPropertyCompiler:
    def compile(
        self,
        properties_structure: PropertiesCompilerStructure,
        map_unique_by_property: dict[str, IndexCompilerStructure],
        entity_model: EntityModel,
        entity_models: dict[str, EntityModel],
    ) -> tuple[
        list[ast.stmt],
        list[ast.stmt],
        list[str],
        list[ast.stmt],
        list[tuple[str, str, str]],
    ]:

        # TODO Criar opção de campo calculado?

        # Descobrindo os atributos marcados como PK (e recuperando a chave primária)
        # pk_keys = []
        # for pkey in properties_structure.properties:
        #     prop = properties_structure.properties[pkey]

        #     if isinstance(prop.type, PrimitiveTypes):
        #         if prop.pk:
        #             pk_keys.append(pkey)

        # if len(pk_keys) > 1:
        #     raise Exception(
        #         f"Entidade '{entity_model.id}' possui mais de uma chave primária (ainda não suportado): {pk_keys}"
        #     )
        # elif len(pk_keys) == 0:
        #     raise Exception(
        #         f"Entidade '{entity_model.id}' não tem nenhuma chave primária (ainda não suportado)"
        #     )

        # pk_key = pk_keys[0]

        # Instanciando as listas de retorno
        ast_dto_attributes = []
        ast_entity_attributes = []
        props_pk = []
        enum_classes = []
        related_imports = []

        if properties_structure.properties is None:
            return (ast_dto_attributes, ast_entity_attributes, props_pk, enum_classes)

        for pkey in properties_structure.properties:
            prop = properties_structure.properties[pkey]

            # DTO
            ## Tratando propriedade simples (não array, não object)
            if isinstance(prop.type, PrimitiveTypes):
                self.compile_simple_property(
                    properties_structure,
                    map_unique_by_property,
                    entity_model,
                    ast_dto_attributes,
                    ast_entity_attributes,
                    props_pk,
                    enum_classes,
                    pkey,
                    prop,
                )

            elif isinstance(prop.type, str):
                external_match = re.match(REGEX_EXTERNAL_REF, prop.type)

                if external_match:
                    # Resolvendo o id da entidade
                    related_entity_id = external_match.group(2)

                    # Resolvendo o nome das classes de DTO e Entity
                    related_dto_class_name = compile_dto_class_name(related_entity_id)
                    related_entity_class_name = compile_entity_class_name(
                        related_entity_id
                    )

                    # Resolvendo o caminho do import
                    related_entity_key = external_match.group(0)

                    related_entity = entity_models.get(related_entity_key)
                    if not related_entity:
                        raise Exception(
                            f"Entidade '{entity_model.id}' possui uma referência externa para uma entidade inexistente: '{related_entity_key}', por meio da propriedade: '{pkey}'."
                        )

                    tenant = related_entity.tenant
                    grupo_empresarial = related_entity.grupo_empresarial
                    grupo_key, tenant_key, default_key = compile_namespace_keys(
                        tenant, grupo_empresarial
                    )

                    if (
                        tenant
                        and tenant != 0
                        and grupo_empresarial
                        and grupo_empresarial != "00000000-0000-0000-0000-000000000000"
                    ):
                        related_import = grupo_key
                    elif tenant and tenant != 0:
                        related_import = tenant_key
                    else:
                        related_import = default_key

                    related_imports.append(
                        (
                            related_import,
                            related_dto_class_name,
                            related_entity_class_name,
                        )
                    )

                    # Instanciando o ast
                    if prop.cardinality == CardinalityTypes.C1_N:
                        # Para relacionamentos 1_N
                        keywords = [
                            ast.keyword(
                                arg="dto_type",
                                value=ast.Name(
                                    id=related_dto_class_name, ctx=ast.Load()
                                ),
                            ),
                            ast.keyword(
                                arg="entity_type",
                                value=ast.Name(
                                    id=related_entity_class_name, ctx=ast.Load()
                                ),
                            ),
                        ]

                        # Resolvendo a coluna usada no relacionamento
                        if (
                            not properties_structure.entity_properties
                            or pkey not in properties_structure.entity_properties
                            or not properties_structure.entity_properties[
                                pkey
                            ].relation_column
                        ):
                            raise Exception(
                                f"Propriedade '{pkey}' possui um relacionamento, mas nenhuma coluna de relacioanamento foi apontada na propriedade correspondente no repository."
                            )

                        relation_column = properties_structure.entity_properties[
                            pkey
                        ].relation_column

                        keywords.append(
                            ast.keyword(
                                arg="related_entity_field",
                                value=ast.Constant(value=relation_column),
                            )
                        )

                        ast_attr = ast.AnnAssign(
                            target=ast.Name(
                                id=CompilerStrUtil.to_snake_case(pkey), ctx=ast.Store()
                            ),
                            annotation=ast.Name(
                                id="list",
                                ctx=ast.Load(),
                            ),
                            value=ast.Call(
                                func=ast.Name(id="DTOListField", ctx=ast.Load()),
                                args=[],
                                keywords=keywords,
                            ),
                            simple=1,
                        )

                        ast_dto_attributes.append(ast_attr)
                    else:
                        # TODO
                        pass

                elif re.match(REGEX_INTERNAL_REF, prop.type):
                    # TODO
                    pass
                else:
                    raise Exception(f"Tipo de propriedade não suportado: {prop.type}")

        return (
            ast_dto_attributes,
            ast_entity_attributes,
            props_pk,
            enum_classes,
            related_imports,
        )

    def compile_simple_property(
        self,
        properties_structure,
        map_unique_by_property,
        entity_model,
        ast_dto_attributes,
        ast_entity_attributes,
        props_pk,
        enum_classes,
        pkey,
        prop,
    ):
        enum_class_name = None
        keywords = []

        if prop.pk:
            keywords.append(ast.keyword(arg="pk", value=ast.Constant(True)))
            props_pk.append(pkey)

        if prop.key_alternative:
            keywords.append(ast.keyword(arg="candidate_key", value=ast.Constant(True)))

        if (
            properties_structure.main_properties
            and pkey in properties_structure.main_properties
        ):
            keywords.append(ast.keyword(arg="resume", value=ast.Constant(True)))

        if properties_structure.required and pkey in properties_structure.required:
            keywords.append(ast.keyword(arg="not_null", value=ast.Constant(True)))

        if (
            properties_structure.partition_data
            and pkey in properties_structure.partition_data
        ):
            keywords.append(ast.keyword(arg="partition_data", value=ast.Constant(True)))

        if pkey in map_unique_by_property:
            unique = map_unique_by_property[pkey].index_model
            keywords.append(
                ast.keyword(
                    arg="unique",
                    value=ast.Constant(unique.name),
                )
            )

        if (
            prop.default
        ):  # TODO Verificar esse modo de tratar valores default (principalmente expressões)
            keywords.append(
                ast.keyword(
                    arg="default_value",
                    value=ast.Name(str(prop.default), ctx=ast.Load()),
                )
            )

        if prop.trim:
            keywords.append(ast.keyword(arg="strip", value=ast.Constant(True)))

        max = None
        min = None
        if prop.type in [PrimitiveTypes.STRING, PrimitiveTypes.EMAIL]:
            if prop.max_length:
                max = prop.max_length
            elif prop.min_length:
                min = prop.min_length
        elif prop.type in [PrimitiveTypes.INTEGER, PrimitiveTypes.NUMBER]:
            if prop.minimum:
                min = prop.minimum
            elif prop.maximum:
                max = prop.maximum

        if max:
            keywords.append(ast.keyword(arg="max", value=ast.Constant(prop.max_length)))
        if min:
            keywords.append(ast.keyword(arg="min", value=ast.Constant(prop.min_length)))

        if (
            properties_structure.search_properties
            and pkey in properties_structure.search_properties
        ):
            keywords.append(ast.keyword(arg="search", value=ast.Constant(True)))
        else:
            keywords.append(ast.keyword(arg="search", value=ast.Constant(False)))

        if (
            properties_structure.metric_label
            and pkey in properties_structure.metric_label
        ):
            keywords.append(ast.keyword(arg="metric_label", value=ast.Constant(True)))

        if prop.type == PrimitiveTypes.CPF and not prop.validator:
            keywords.append(
                ast.keyword(
                    arg="validator",
                    value=ast.Attribute(
                        value=ast.Call(
                            func=ast.Name(id="DTOFieldValidators", ctx=ast.Load()),
                            args=[],
                            keywords=[],
                        ),
                        attr="validate_cpf",
                        ctx=ast.Load(),
                    ),
                )
            )
        elif prop.type == PrimitiveTypes.CNPJ and not prop.validator:
            keywords.append(
                ast.keyword(
                    arg="validator",
                    value=ast.Attribute(
                        value=ast.Call(
                            func=ast.Name(id="DTOFieldValidators", ctx=ast.Load()),
                            args=[],
                            keywords=[],
                        ),
                        attr="validate_cnpj",
                        ctx=ast.Load(),
                    ),
                )
            )
        elif prop.type == PrimitiveTypes.CPF_CNPJ and not prop.validator:
            keywords.append(
                ast.keyword(
                    arg="validator",
                    value=ast.Attribute(
                        value=ast.Call(
                            func=ast.Name(id="DTOFieldValidators", ctx=ast.Load()),
                            args=[],
                            keywords=[],
                        ),
                        attr="validate_cpf_or_cnpj",
                        ctx=ast.Load(),
                    ),
                )
            )
        elif prop.type == PrimitiveTypes.EMAIL and not prop.validator:
            keywords.append(
                ast.keyword(
                    arg="validator",
                    value=ast.Attribute(
                        value=ast.Call(
                            func=ast.Name(id="DTOFieldValidators", ctx=ast.Load()),
                            args=[],
                            keywords=[],
                        ),
                        attr="validate_email",
                        ctx=ast.Load(),
                    ),
                )
            )
        elif prop.validator:
            keywords.append(
                ast.keyword(
                    arg="validator",
                    value=ast.Name(prop.validator, ctx=ast.Load()),
                )
            )

        if prop.immutable:
            keywords.append(ast.keyword(arg="read_only", value=ast.Constant(True)))

        if prop.on_save:
            keywords.append(
                ast.keyword(
                    arg="convert_to_entity",
                    value=ast.Name(prop.on_save, ctx=ast.Load()),
                )
            )

        if prop.on_retrieve:
            keywords.append(
                ast.keyword(
                    arg="convert_from_entity",
                    value=ast.Name(id=prop.on_retrieve, ctx=ast.Load()),
                )
            )

        if prop.domain_config:
            result = self._compile_domain_config(pkey, prop, entity_model)
            if not result:
                raise Exception(f"Erro desconhecido ao compilar a propriedade {pkey}")

            enum_class_name, ast_enum_class = result
            enum_classes.append(ast_enum_class)

        # Resolvendo o nome da propriedade no Entity
        if (
            properties_structure.entity_properties
            and pkey in properties_structure.entity_properties
        ):
            entity_field_name = properties_structure.entity_properties[pkey].column
        else:
            entity_field_name = pkey

        # Escrevendo, se necessário, o alias para o nome da entity
        if entity_field_name != pkey:
            keywords.append(
                ast.keyword(
                    arg="entity_field",
                    value=ast.Constant(value=entity_field_name),
                )
            )

        # Instanciando o atributo AST
        if enum_class_name:
            prop_type = enum_class_name
        else:
            prop_type = TypeUtil.property_type_to_python_type(prop.type)

        ast_attr = ast.AnnAssign(
            target=ast.Name(id=CompilerStrUtil.to_snake_case(pkey), ctx=ast.Store()),
            annotation=ast.Name(
                id=prop_type,
                ctx=ast.Load(),
            ),
            value=ast.Call(
                func=ast.Name(id="DTOField", ctx=ast.Load()),
                args=[],
                keywords=keywords,
            ),
            simple=1,
        )

        ast_dto_attributes.append(ast_attr)

        # Entity
        ast_entity_attr = ast.AnnAssign(
            target=ast.Name(
                id=CompilerStrUtil.to_snake_case(entity_field_name),
                ctx=ast.Store(),
            ),
            annotation=ast.Name(
                id=TypeUtil.property_type_to_python_type(prop.type),
                ctx=ast.Load(),
            ),
            value=ast.Constant(value=None),
            simple=1,
        )

        ast_entity_attributes.append(ast_entity_attr)

    def _compile_domain_config(
        self,
        pkey: str,
        prop: PropertyMetaModel,
        entity_model: EntityModel,
    ) -> tuple[str, ast.stmt] | None:
        if not prop.domain_config:
            return None

        # Verificando se deveria usar o mapped_value
        use_mapped_value = False
        for value in prop.domain_config:
            if value.mapped_value:
                use_mapped_value = True
                break

        # Compilando as opções do enum
        ast_values = []
        for value in prop.domain_config:
            value_name = CompilerStrUtil.to_snake_case(value.value).upper()

            if use_mapped_value and value.mapped_value is None:
                raise Exception(
                    f"Propriedade '{pkey}' possui domain_config com value '{value.value}' mas sem mapped_value"
                )

            if value.mapped_value is not None:
                ast_value = ast.Assign(
                    targets=[ast.Name(id=value_name, ctx=ast.Store())],
                    value=ast.Tuple(
                        elts=[
                            ast.Constant(value=value.value),
                            ast.Constant(value=value.mapped_value),
                        ],
                        ctx=ast.Load(),
                    ),
                )
            else:
                ast_value = ast.Assign(
                    targets=[ast.Name(id=value_name, ctx=ast.Store())],
                    value=ast.Constant(value=value.value),
                )

            ast_values.append(ast_value)

        # Instanciando o atributo AST
        enum_class_name = f"{CompilerStrUtil.to_pascal_case(entity_model.escopo)}{CompilerStrUtil.to_pascal_case(entity_model.id)}{CompilerStrUtil.to_pascal_case(pkey)}Enum"
        ast_enum_class = ast.ClassDef(
            name=enum_class_name,
            bases=[
                ast.Attribute(
                    value=ast.Name(id="enum", ctx=ast.Load()),
                    attr="Enum",
                    ctx=ast.Load(),
                )
            ],
            keywords=[],
            decorator_list=[],
            body=ast_values,
        )

        return enum_class_name, ast_enum_class
