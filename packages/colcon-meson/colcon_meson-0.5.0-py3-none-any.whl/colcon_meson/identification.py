# Copyright 2024 Christian Rauch
# Licensed under the Apache License, Version 2.0

import os
import typing

# colcon
from colcon_core.logging import colcon_logger
from colcon_core.package_descriptor import PackageDescriptor
from colcon_core.package_identification import PackageIdentificationExtensionPoint
# meson
from mesonbuild import mesonlib
from mesonbuild.ast import IntrospectionInterpreter
from mesonbuild.interpreter import primitives
from mesonbuild.interpreterbase.baseobjects import InterpreterObject, mparser

logger = colcon_logger.getChild(__name__)


class CustomInterpreter(IntrospectionInterpreter):
    """A custom interpreter to parse metadata for Meson projects."""

    def __init__(self, source_root: str, subdir: str, backend: str,):
        """Initialise the interpreter and a data structure for metadata."""
        super().__init__(source_root, subdir, backend)

        self.holder_map.update({
            list: primitives.ArrayHolder,
            dict: primitives.DictHolder,
            int: primitives.IntegerHolder,
            bool: primitives.BooleanHolder,
            str: primitives.StringHolder,
        })

        self.data = {}
        self.data["dependencies"] = set()

    def evaluate_statement(self, cur: mparser.BaseNode) -> typing.Optional[InterpreterObject]:
        """Evaluate the statements in the Meson project file.

        Args:
            cur (mparser.BaseNode): a node in the project file

        Returns:
            typing.Optional[InterpreterObject]:
        """
        if isinstance(cur, mparser.FunctionNode):
            return self._function_call(cur)
        elif isinstance(cur, mparser.AssignmentNode):
            self._assignment(cur)
        elif isinstance(cur, mparser.StringNode):
            return self._holderify(cur.value)
        elif isinstance(cur, mparser.ArrayNode):
            return self._evaluate_arraystatement(cur)
        return None

    def _function_call(self, node: mparser.FunctionNode) -> typing.Optional[InterpreterObject]:
        node_func_name = f"{type(node.func_name).__module__}.{type(node.func_name).__qualname__}"
        if node_func_name == "builtins.str":
            # meson <= 1.2
            func_name = node.func_name
        elif node_func_name == "mesonbuild.mparser.IdNode":
            # meson >= 1.3
            func_name = node.func_name.value
        else:
            raise AttributeError("Cannot determine meson project name.")

        assert type(func_name) is str

        reduced_pos = [self.evaluate_statement(arg) for arg in node.args.arguments]
        reduced_pos = list(filter(None, reduced_pos))
        args = self._unholder_args(reduced_pos, {})[0]

        if func_name == "project":
            self.data["name"] = args[0]
        elif func_name == "dependency":
            self.data["dependencies"].update(args)
        elif func_name == "subdir":
            subpath = os.path.join(self.source_root, args[0])
            parser = CustomInterpreter(subpath, "", "")
            subdata = parser.parse()
            for k in subdata.keys():
                self.data[k].update(subdata[k])
        return None

    def _assignment(self, node: mparser.AssignmentNode) -> None:
        self.evaluate_statement(node.value)
        return None

    def _evaluate_arraystatement(self, cur: mparser.ArrayNode) -> InterpreterObject:
        arguments = [self.evaluate_statement(arg) for arg in cur.args.arguments]
        arguments = list(filter(None, arguments))
        return self._holderify(self._unholder_args(arguments, {})[0])

    def parse(self) -> dict:
        """Run the interpreter on a Meson project file.

        Returns:
            dict: extracted metadata
        """
        try:
            self.load_root_meson_file()
        except mesonlib.MesonException:
            return {}

        self.evaluate_codeblock(self.ast)
        return self.data


class MesonPackageIdentification(PackageIdentificationExtensionPoint):
    """Meson package identification."""

    def identify(self, desc: PackageDescriptor):
        """Identify a Meson project for colcon.

        Args:
            desc (PackageDescriptor): package description that will be updated
        """
        parser = CustomInterpreter(desc.path, "", "")
        data = parser.parse()

        if not data:
            return

        desc.type = 'meson'

        if desc.name is None:
            desc.name = data["name"]

        logger.info("'%s' dependencies: %s", desc.name, data['dependencies'])

        desc.dependencies['build'].update(data['dependencies'])
        desc.dependencies['run'].update(data['dependencies'])
