from importlib import metadata

package = __package__ or "lightning-cv"

_data: dict[str, str] = dict(metadata.metadata(package))  # type: ignore


def try_get(data: dict[str, str], key: str, default: str = ""):
    is_upper = key.istitle()

    maybe_value = data.get(key, None)

    if maybe_value is None:
        if is_upper:
            key = key.lower()
        else:
            key = key.title()

        maybe_value = data.get(key, default)

    return maybe_value


__title__: str = try_get(_data, "name", package)
__description__: str = try_get(_data, "summary", "Unknown description")
__version__: str = metadata.version(package)
__author__: str = try_get(_data, "Author-email", "Unknown author")
__license__: str = try_get(_data, "license", "MIT License")
