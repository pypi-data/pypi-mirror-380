from typing import Union


def _update_transparency(
    transparency: Union[float, None],
    format: Union[str, None] = None
) -> Union[float, None]:
    """
    *For internal use only*

    Update the provided 'transparency' value,
    that must be a value in the [0.0, 1.0] range,
    if necessary.

    If the 'format' is provided:
    - Alpha format will force an opaque alpha
    transparency if it is None
    - Non-alpha format will force a None value
    if transparency is provided
    """
    return (
        # Alpha format, no transparency => opaque
        0.0
        if (
            transparency is None and
            format is not None and
            'a' in format 
        ) else
        # Non-alpha format but transparency => None
        None
        if (
            transparency is not None and
            format is not None and
            'a' not in format
        ) else
        # Lower than 0.0 limit
        0.0
        if (
            transparency is not None and
            transparency < 0.0
        ) else
        # Greater than 1.0 limit
        1.0
        if (
            transparency is not None and
            transparency > 1.0
        ) else
        transparency
    )