#!/usr/bin/env python3
"""Build the C++ tangency backend shared library."""

from __future__ import annotations

import sys
import sysconfig
from pathlib import Path
from typing import Iterable

try:  # pragma: no cover - import guard is environment dependent
    from setuptools import Distribution, Extension
    from setuptools.command.build_ext import build_ext
except ModuleNotFoundError as exc:  # pragma: no cover - helpful guidance for users
    raise RuntimeError(
        "setuptools is required to build the C++ backend. "
    ) from exc

_LIB_NAME = "_tangency_cpp_impl"


def _library_suffix() -> str:
    suffix = sysconfig.get_config_var("SHLIB_SUFFIX")
    if suffix:
        return suffix
    if sys.platform.startswith("win"):
        return ".dll"
    if sys.platform == "darwin":
        return ".dylib"
    return ".so"


def _source_path() -> Path:
    return Path(__file__).resolve().parent / "src" / "ellphi" / f"{_LIB_NAME}.cpp"


def _output_path() -> Path:
    return _source_path().with_suffix(_library_suffix())


def _ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


class _TangencyExtension(Extension):
    def __init__(self) -> None:
        super().__init__(
            name=_LIB_NAME,
            sources=[str(_source_path())],
            language="c++",
        )


class _BuildTangency(build_ext):
    c_opts = {
        "msvc": ["/std:c++17", "/O2", "/EHsc"],
        "unix": ["-std=c++17", "-O3", "-fPIC"],
    }
    l_opts = {"msvc": [], "unix": ["-lstdc++"]}

    if sys.platform == "darwin":
        c_opts["unix"].append("-mmacosx-version-min=10.15")

    def build_extension(self, ext: Extension) -> None:  # type: ignore[override]
        compiler = self.compiler
        if compiler is None:  # pragma: no cover - setuptools invariant
            raise RuntimeError("Compiler was not initialized")

        ctype = compiler.compiler_type
        compile_opts = list(self.c_opts.get(ctype, []))
        link_opts = list(self.l_opts.get(ctype, []))

        objects = compiler.compile(
            ext.sources,  # type: ignore[arg-type]
            output_dir=self.build_temp,
            include_dirs=ext.include_dirs,
            extra_postargs=compile_opts,
            depends=ext.depends,
        )

        suffix = _library_suffix()
        target = Path(self.build_lib) / f"{_LIB_NAME}{suffix}"
        _ensure_parent(target)

        compiler.link_shared_object(
            objects,
            str(target),
            extra_postargs=link_opts,
            libraries=self.get_libraries(ext),
            library_dirs=ext.library_dirs,
        )

        self._built_objects = getattr(self, "_built_objects", [])
        self._built_objects.append(target)

    def get_outputs(self) -> Iterable[str]:  # type: ignore[override]
        for path in getattr(self, "_built_objects", []):
            yield str(path)


def build() -> Path:
    source = _source_path()
    output = _output_path()

    if not source.exists():
        raise FileNotFoundError(f"C++ source not found: {source}")

    if output.exists() and output.stat().st_mtime >= source.stat().st_mtime:
        return output

    dist = Distribution()
    dist.ext_modules = [_TangencyExtension()]
    dist.cmdclass = {"build_ext": _BuildTangency}

    build_cmd = dist.get_command_obj("build_ext")
    assert isinstance(build_cmd, _BuildTangency)
    build_cmd.build_temp = str(Path("build") / "tangency")
    build_cmd.build_lib = str(source.parent)
    build_cmd.ensure_finalized()
    build_cmd.run()

    outputs = list(build_cmd.get_outputs())
    if not outputs:
        raise RuntimeError("Tangency backend build produced no outputs")
    return Path(outputs[0])


if __name__ == "__main__":
    path = build()
    print(f"Built tangency backend: {path}")
