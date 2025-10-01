from typing import Literal, Type, Union, overload
from ..dtos.medical_service import (
    BasicMedicalServiceData,
    StandardMedicalServiceData,
    FullMedicalServiceData,
)
from ..enums.medical_service import Granularity


@overload
def get_data_model(
    granularity: Literal[Granularity.BASIC],
    /,
) -> Type[BasicMedicalServiceData]: ...
@overload
def get_data_model(
    granularity: Literal[Granularity.STANDARD],
    /,
) -> Type[StandardMedicalServiceData]: ...
@overload
def get_data_model(
    granularity: Literal[Granularity.FULL],
    /,
) -> Type[FullMedicalServiceData]: ...
def get_data_model(
    granularity: Granularity,
    /,
) -> Union[
    Type[BasicMedicalServiceData],
    Type[StandardMedicalServiceData],
    Type[FullMedicalServiceData],
]:
    if granularity is Granularity.BASIC:
        return BasicMedicalServiceData
    elif granularity is Granularity.STANDARD:
        return StandardMedicalServiceData
    elif granularity is Granularity.FULL:
        return FullMedicalServiceData
