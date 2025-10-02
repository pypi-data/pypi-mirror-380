from pydantic import BaseModel, Field

from nsj_rest_lib2.compiler.edl_model.primitives import BasicTypes, PropertyType


class TraitPropertyMetaModel(BaseModel):
    type: PropertyType = Field(..., description="Tipo da propriedade.")
    value: BasicTypes = Field(
        ..., description="Valor fixo da propriedade de condicionamento do trait."
    )
