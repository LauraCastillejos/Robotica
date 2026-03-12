import roboticstoolbox as rtb
import numpy as np
import importlib.metadata as metadata


def version_of(module, name):
    try:
        return getattr(module, "__version__")
    except Exception:
        try:
            return metadata.version(name)
        except metadata.PackageNotFoundError:
            return "desconocida"


print(f"roboticstoolbox versión: {version_of(rtb, 'roboticstoolbox')}")
print(f"numpy versión: {np.__version__}")
