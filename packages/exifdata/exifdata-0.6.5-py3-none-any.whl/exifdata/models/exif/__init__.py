from __future__ import annotations

import os
import json
import io

from exifdata.logging import logger

from exifdata.framework import (
    Metadata,
    Namespace,
    Structure,
    Value,
    Type,
)

from exifdata.models.exif.framework.field import Field

from exifdata.models.exif.enumerations import (
    TagType,
)

from exifdata.models.exif.types import (
    Byte,
    ASCII,
    Short,
    Long,
    Rational,
    ByteSigned,
    Undefined,
    ShortSigned,
    LongSigned,
    RationalSigned,
    Float,
    Double,
    UTF8,
    String,
)

from exifdata.models.exif.structures import (
    IFD,
    IFDTag,
)

from deliciousbytes import (
    ByteOrder,
    Encoding,
)


logger = logger.getChild(__name__)


class EXIF(Metadata):
    _namespaces: dict[str, Namespace] = {}
    _structures: dict[str, Structure] = {}
    _aliases: dict[str, str] = {}
    _encodings: list[str] = ["UTF-8", "Unicode", "ASCII"]
    _types: dict[str, type] = {}
    _setup: bool = False

    def __new__(cls):
        """Initialize the model's namespaces from the schema configuration file once."""

        # If the setup has already been performed previously, return immediately
        if cls._setup is True:
            return super().__new__(cls)

        with open(
            os.path.join(os.path.dirname(__file__), "data", "schema.json"), "r"
        ) as handle:
            # Ensure the model configuration file is valid
            if not isinstance(namespacesdata := json.load(handle), dict):
                raise TypeError("The EXIF schema.json dictionary isn't valid!")

            # Dynamically create the model namespaces based on the provided configuration
            for namespaceid, namespacedata in namespacesdata.items():
                if not isinstance(namespaceid, str):
                    raise TypeError("All namespace dictionary keys must be strings!")

                if namespaceid.startswith("@"):
                    # If any top-level aliases have been specified, capture those now
                    if namespaceid == "@aliases" and isinstance(namespacedata, dict):
                        cls._aliases = namespacedata
                    continue

                if not isinstance(namespacedata, dict):
                    raise TypeError(
                        "All model schema top-level values must be dictionaries!"
                    )

                if structuresdata := namespacedata.get("structures"):
                    for structureid, structuredata in structuresdata.items():
                        cls._structures[structuredata.get("name")] = Structure(
                            identifier=structureid,
                            **structuredata,
                        )

                # Then add the name-spaced fields under the model, first creating the namespace
                if fieldsdata := namespacedata.pop("fields"):
                    cls._namespaces[namespacedata.get("name")] = namespace = Namespace(
                        identifier=namespaceid,
                        # metadata=self,  # Set later via Metadata.__getattr__()
                        **namespacedata,
                    )

                    # Now iterate over the fields and add them to the relevant namespace
                    for fieldid, fielddata in fieldsdata.items():
                        namespace.field = field = Field(
                            namespace=namespace,
                            identifier=fieldid,
                            **fielddata,
                        )

                        # If the namespace has been marked for unwrapping, make its fields
                        # available on the top-level metadata object as well as through the
                        # namespace object itself, via its field name and any aliases:
                        if namespace.unwrap is True:
                            if field.name in cls._aliases:
                                raise KeyError(
                                    f"The field alias, '{field.name}', has already been used!"
                                )

                            cls._aliases[field.name] = f"{namespace.id}:{field.name}"

                            for alias in field.aliases:
                                if alias in cls._aliases:
                                    raise KeyError(
                                        f"The field alias, '{alias}', has already been used!"
                                    )

                                cls._aliases[alias] = f"{namespace.id}:{field.name}"

        cls._setup = True

        return super().__new__(cls)

    def encode(self, order: ByteOrder = ByteOrder.MSB) -> bytes | None:
        """Provides support for encoding the assigned EXIF metadata field values into
        the binary representation needed for embedding into an image file."""

        encoded: bytearray = bytearray()

        if not isinstance(order, ByteOrder):
            raise TypeError(
                "The 'order' argument must reference a ByteOrder enumeration option!"
            )

        if len(self._values) == 0:
            logger.info(
                "No EXIF metadata fields were assigned values, so there is nothing to encode."
            )
            return None

        ifd = IFD()

        for namespace in self._namespaces.values():
            for identifier, field in namespace._fields.items():
                if isinstance(value := self._values.get(field.identifier), Value):
                    count: int = len(value) if isinstance(value, list) else 1

                    if field.multiple is True and not count in field.count:
                        raise ValueError(
                            "The value count (%d) does not match one of the field counts (%s) for %s!"
                            % (
                                count,
                                field.count,
                                field.identifier,
                            )
                        )

                    data: bytearray = bytearray()

                    if isinstance(value, list):
                        for value in value:
                            data += value.encode(order=order)
                    else:
                        data += value.encode(order=order)

                    ifd.tag = IFDTag(
                        id=field.tagid,
                        type=TagType.reconcile(value.type).value,
                        count=count,
                        data=bytes(data),
                    )

        encoded += ifd.encode()

        return bytes(encoded) if len(encoded) > 0 else None

    @classmethod
    def decode(
        cls,
        value: bytes | io.BytesIO,
        order: ByteOrder = ByteOrder.MSB,
    ) -> EXIF:
        """Provides support for decoding the provided EXIF metadata payload into its
        corresponding EXIF metadata fields which can then be accessed for use."""

        logger.debug(
            "%s.decode(value: %d, format: %s, order: %s)",
            cls.__name__,
            len(value),
            format,
            order,
        )

        if not isinstance(value, bytes):
            value = io.BytesIO(value)
        elif isinstance(value, io.BytesIO):
            pass
        else:
            raise TypeError("The 'value' argument must have a bytes or BytesIO value!")

        # TODO: Complete implementation of EXIF metadata parsing

        return None


EXIF.register_types(
    Byte,
    ASCII,
    Short,
    Long,
    Rational,
    ByteSigned,
    Undefined,
    ShortSigned,
    LongSigned,
    RationalSigned,
    Float,
    Double,
    UTF8,
    String,
)
