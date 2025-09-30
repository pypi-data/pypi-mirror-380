"""Defines soil.data() async version"""

import uuid
from typing import (
    Any,
    Dict,
    Optional,
    Type,
    cast,
    overload,
)

from soil.aio.api import get_alias, get_result, upload_data
from soil.data_structure import DataStructure, get_data_structure_name_and_serialize
from soil.types import DataObject, SerializableDataStructure


@overload
async def data(
    data_object: str,
    metadata: None = None,
    *,
    return_type: None = None,
) -> DataStructure: ...


@overload
async def data[G: SerializableDataStructure](
    data_object: str,
    metadata: None = None,
    *,
    return_type: Type[G],
) -> G: ...


@overload
async def data[D: DataObject](
    data_object: D,
    metadata: dict[str, Any] | None = None,
    *,
    return_type: None = None,
) -> DataStructure[D]: ...


@overload
async def data[G: SerializableDataStructure](
    data_object: DataObject,
    metadata: dict[str, Any] | None = None,
    *,
    return_type: Type[G],
) -> G: ...


async def data[D: DataObject, G: SerializableDataStructure](  # pyright: ignore[reportInconsistentOverload]
    data_object: str | D,
    metadata: dict[str, Any] | None = None,
    *,
    return_type: Type[G] | None = None,
) -> G | DataStructure | DataStructure[D]:
    """Load data from the cloud or mark it as uploadable"""
    cast_return_type = DataStructure if return_type is None else return_type
    if isinstance(data_object, str):
        try:
            # Check if the id is a uuid
            uuid.UUID(data_object)
            return cast(cast_return_type, await _load_data_id(data_object))  # pyright: ignore
        except ValueError:
            alias_data = await get_alias(data_object)
            return cast(
                cast_return_type,  # pyright: ignore
                await _load_datastructure(
                    did=alias_data["result"]["_id"],
                    dtype=alias_data["result"]["type"],
                    metadata=alias_data["result"]["metadata"],
                ),
            )

    return cast(
        cast_return_type,  # pyright: ignore
        await _upload_data(data_object, metadata),
    )


async def _upload_data(
    data_object: Any, metadata: Optional[Dict[str, Any]] = None
) -> DataStructure:
    ds_name, serialized = get_data_structure_name_and_serialize(data_object)
    result = await upload_data(ds_name, serialized, metadata)
    ds = DataStructure(result["_id"], dstype=result["type"])
    return ds


async def _load_datastructure(
    did: str, dtype: str, metadata: dict[str, Any] | None = None
) -> DataStructure:
    # TODO: dynamically load a data structure
    return DataStructure(did, dstype=dtype, metadata=metadata)


async def _load_data_id(data_id: str) -> DataStructure:
    result = await get_result(data_id)
    return await _load_datastructure(
        result["_id"], result["type"], metadata=result["metadata"]
    )
