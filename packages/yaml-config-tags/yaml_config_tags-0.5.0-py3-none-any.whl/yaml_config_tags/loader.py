"""Custom YAML loader with support for Jinja templates, environment variables, and file includes."""

import json
import os
from collections.abc import Callable
from pathlib import Path
from typing import Any, BinaryIO, TextIO, TypeVar, overload

import yaml
from jinja2 import Environment
from jinja2.nativetypes import NativeEnvironment

T = TypeVar("T")


class ConfigLoader(yaml.SafeLoader):
    """Custom YAML loader to parse configuration files with support for Jinja, ENV, and Includes."""

    def __init__(  # noqa: PLR0913
        self,
        stream: str | bytes | TextIO | BinaryIO,
        base_path: str | Path,
        *,
        context: dict[str, Any] | None = None,
        jinja_settings: dict[str, Any] | None = None,
        jinja_filters: dict[str, Callable] | None = None,
        parse_only: bool = False,
    ) -> None:

        super().__init__(stream)
        # Store configurations
        self.base_path = Path(base_path)
        self.jinja_context = context or {}
        self.jinja_settings = jinja_settings or {}
        self.text_env = Environment(autoescape=True, **(self.jinja_settings))
        self.native_env = NativeEnvironment(**(self.jinja_settings))
        if jinja_filters:
            for name, func in jinja_filters.items():
                self.text_env.filters[name] = func
                self.native_env.filters[name] = func
        self.env_vars: set[str] = set()
        self.parse_only = parse_only

    def construct_str_jinja(self, node: yaml.nodes.Node) -> str:
        """Parse `!jinja` and `!jinja:str` tag, rendering Jinja template as text."""
        if not isinstance(node, yaml.nodes.ScalarNode):
            raise yaml.constructor.ConstructorError(
                None,
                None,
                f"expected a scalar node, but found {node.tag}",
                node.start_mark,
            )
        txt = self.construct_scalar(node)
        template = self.text_env.from_string(txt)
        return txt if self.parse_only else template.render(**self.jinja_context)

    def construct_obj_jinja(self, node: yaml.nodes.Node) -> Any:  # noqa: ANN401
        """Parse `!jinja:obj` tag, rendering Jinja template to native Python objects."""
        if not isinstance(node, yaml.nodes.ScalarNode):
            raise yaml.constructor.ConstructorError(
                None,
                None,
                f"expected a scalar node, but found {node.tag}",
                node.start_mark,
            )
        txt = self.construct_scalar(node)
        template = self.native_env.from_string(txt)
        return txt if self.parse_only else template.render(**self.jinja_context)

    def construct_multi_jinja(self, suffix: str, node: yaml.nodes.Node) -> Any:  # noqa: ANN401
        """Parse `!jinja:<suffix>` tag, rendering Jinja template based on the suffix."""
        if suffix == "str":
            return self.construct_str_jinja(node)
        if suffix == "obj":
            return self.construct_obj_jinja(node)

        raise yaml.constructor.ConstructorError(
            None,
            None,
            f"expected 'obj' or 'str' suffix, but found {suffix}",
            node.start_mark,
        )

    # adapted from
    # https://github.com/waylan/pyyaml-env-tag/blob/master/yaml_env_tag.py
    def env_constructor(
        self, node: yaml.nodes.Node, suffix: str | None = None
    ) -> Any:  # noqa: ANN401
        """Parse `!env` tag, fetching values from environment variables.

        Supports fallback variables and default values using list syntax:

        ```yaml
        - !env [VAR_NAME]
        - !env [VAR_NAME, FALLBACK_1_VAR_NAME, ...,  FALLBACK_n_VAR_NAME, DEFAULT_VALUE]
        ```

        DEFAULT_VALUE can be any YAML value, and will be resolved using YAML's implicit types.
        """
        default = None
        has_default = False
        if isinstance(node, yaml.nodes.ScalarNode):
            variables = [self.construct_scalar(node)]

        elif isinstance(node, yaml.nodes.SequenceNode):
            child_nodes = node.value
            if len(child_nodes) > 1:
                # default is resolved using YAML's (implicit) types.
                default = self.construct_object(child_nodes[-1])
                has_default = True
                child_nodes = child_nodes[:-1]
            # Env Vars are resolved as string values, ignoring (implicit) types.
            variables = [self.construct_scalar(child) for child in child_nodes]
        else:
            raise yaml.constructor.ConstructorError(
                None,
                None,
                f"expected a scalar or sequence node, but found {node.tag}",
                node.start_mark,
            )

        self.env_vars.update(variables)
        if self.parse_only:
            return f"{variables}"

        for var in variables:
            if var in os.environ:
                value = os.environ[var]
                if suffix:
                    # Resolve value to Python type using YAML's implicit resolvers
                    tag = f"tag:yaml.org,2002:{suffix}"
                else:
                    # Resolve value to Python type using YAML's implicit resolvers
                    tag = self.resolve(yaml.nodes.ScalarNode, value, (True, False))
                return self.construct_object(yaml.nodes.ScalarNode(tag, value))

        if not has_default:
            raise yaml.constructor.ConstructorError(
                None,
                None,
                f"environment variable(s) {variables} not found and no default value provided",
                node.start_mark,
            )
        return default

    def construct_multi_env(self, suffix: str, node: yaml.nodes.Node) -> Any:  # noqa: ANN401
        """Parse `!env:<suffix>` tag, converting environment variable to fixed type."""
        valid = ["str", "int", "float", "bool", "timestamp"]
        if suffix not in valid:
            raise yaml.constructor.ConstructorError(
                None,
                None,
                f"expected {valid}, but found {suffix}",
                node.start_mark,
            )

        return self.env_constructor(node, suffix)

    def include_constructor(self, node: yaml.nodes.Node) -> Any:  # noqa: ANN401
        """Parse `!include` tag, including another YAML file."""
        return self.multi_include_constructor("yaml", node)

    def multi_include_constructor(self, suffix: str, node: yaml.nodes.Node) -> Any:  # noqa: ANN401
        """Parse `!include:<suffix>` tag, including another YAML file based on the suffix."""
        if not isinstance(node, yaml.nodes.ScalarNode):
            raise yaml.constructor.ConstructorError(
                None,
                None,
                f"expected a scalar node, but found {node.tag}",
                node.start_mark,
            )

        if suffix not in ["yaml", "json", "txt"]:
            raise yaml.constructor.ConstructorError(
                None,
                None,
                f"expected 'yaml', 'json', 'str' suffix, but found {suffix}",
                node.start_mark,
            )
        path = self.construct_scalar(node)

        if not isinstance(path, str):
            raise yaml.constructor.ConstructorError(
                None,
                None,
                f"expected a string, but found {path}",
                node.start_mark,
            )

        if self.parse_only:
            return f"{path}"

        # check if it is a glob pattern
        is_glob = "*" in path or "?" in path or "[" in path
        # check if it is a relative path
        root = Path("/") if path.startswith("/") else self.base_path

        files = [root / path] if not is_glob else root.glob(path)

        results = []
        for file in files:
            if not file.exists():
                raise yaml.constructor.ConstructorError(
                    None,
                    None,
                    f"file {file} does not exist",
                    node.start_mark,
                )

            if suffix == "yaml":
                results.append(
                    config_load(
                        file, context=self.jinja_context, jinja_settings=self.jinja_settings
                    )
                )

            if suffix == "json":
                with open(file, encoding="utf-8") as fp:
                    try:
                        data = json.load(fp)
                    except json.JSONDecodeError as exc:
                        raise yaml.constructor.ConstructorError(
                            None,
                            None,
                            f"failed to parse JSON file {path}: {exc.msg}",
                            node.start_mark,
                        ) from exc
                    results.append(data)
            if suffix == "txt":
                with open(file, encoding="utf-8") as fp:
                    try:
                        data = fp.read()
                    except Exception as exc:
                        raise yaml.constructor.ConstructorError(
                            None,
                            None,
                            f"failed to read file {path}",
                            node.start_mark,
                        ) from exc
                    results.append(data)

        return results if is_glob else results[0]


ConfigLoader.add_constructor("!env", ConfigLoader.env_constructor)
ConfigLoader.add_multi_constructor("!env:", ConfigLoader.construct_multi_env)
ConfigLoader.add_constructor("!jinja", ConfigLoader.construct_str_jinja)
ConfigLoader.add_multi_constructor("!jinja:", ConfigLoader.construct_multi_jinja)
ConfigLoader.add_constructor("!include", ConfigLoader.include_constructor)
ConfigLoader.add_multi_constructor("!include:", ConfigLoader.multi_include_constructor)


@overload
def config_load(
    path: str | Path,
    context: dict[str, Any] | None = None,
    jinja_settings: dict[str, Any] | None = None,
    jinja_filters: dict[str, Callable] | None = None,
    *,
    constructor: type[T],
) -> T: ...


@overload
def config_load(
    path: str | Path,
    context: dict[str, Any] | None = None,
    jinja_settings: dict[str, Any] | None = None,
    jinja_filters: dict[str, Callable] | None = None,
    *,
    constructor: None = None,
) -> Any: ...  # noqa: ANN401


def config_load(
    path: str | Path,
    context: dict[str, Any] | None = None,
    jinja_settings: dict[str, Any] | None = None,
    jinja_filters: dict[str, Callable] | None = None,
    *,
    constructor: type[Any] | None = None,
) -> Any:
    """Load configuration from YAML file, with support for Jinja, ENV and Includes.

    Args:
        path: Path to the YAML configuration file
        context: Context variables for Jinja template rendering
        jinja_settings: Settings for Jinja environment
        jinja_filters: Custom Jinja filters
        constructor: Optional class constructor to create typed instances

    Returns:
        `Any` if no constructor is provided, otherwise an instance of the constructor type.

    Note:
        The constructor can be any Python class that accepts keyword arguments,
        including regular classes, dataclasses, NamedTuples, Pydantic models, etc.
        The loaded YAML data must be a dictionary to be passed as keyword arguments.
    """
    path = Path(path)

    with open(path, encoding="utf-8") as stream:
        loader = ConfigLoader(
            stream,
            path.parent.absolute(),
            context=context,
            jinja_settings=jinja_settings,
            jinja_filters=jinja_filters,
        )
        try:
            data = loader.get_single_data()

            if constructor:
                if not isinstance(data, dict):
                    raise ValueError("Data is not a dictionary, cannot construct object")
                return constructor(**data)

            return data
        finally:
            loader.dispose()


def config_get_env(
    path: str | Path,
    jinja_settings: dict[str, Any] | None = None,
    jinja_filters: dict[str, Callable] | None = None,
) -> set[str]:
    """Load configuration YAML file, parses it and return list of referenced ENV variables."""
    path = Path(path)

    with open(path, encoding="utf-8") as stream:
        loader = ConfigLoader(
            stream,
            path.parent.absolute(),
            context=None,
            jinja_settings=jinja_settings,
            jinja_filters=jinja_filters,
            parse_only=True,
        )
        try:
            loader.get_single_data()
        finally:
            loader.dispose()

        return loader.env_vars
