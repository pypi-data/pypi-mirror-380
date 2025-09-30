import json
from pathlib import Path
from typing import Any, Dict, Optional, Union
from argparse import ArgumentParser
from wowool.build.docstrings.json_visitor import DocstringVisitor
from logging import getLogger
from re import compile as re_compile

logger = getLogger(__name__)


TOC_PATTERN = re_compile("@@TOC(.*?)TOC@@")


class MarkdownVisitor(DocstringVisitor):
    """Visitor that generates Markdown documentation from the JSON structure."""

    def __init__(self, include_toc: bool = True, include_examples: bool = True, include_notes: bool = True, initial_level: int = 0):
        self.markdown_lines = []
        self.include_toc = include_toc
        self.include_examples = include_examples
        self.include_notes = include_notes
        self.toc_entries = {}
        self.initial_level = initial_level
        self.module_name = None

    def _generate_anchor(self, text: str) -> str:
        """Generate a GitHub-style markdown anchor from heading text.

        Args:
            text (str): The heading text to convert to an anchor.

        Returns:
            str: The anchor string suitable for GitHub markdown links.
        """
        import re

        # Convert to lowercase
        anchor = text.lower()

        # Replace spaces with hyphens
        anchor = anchor.replace(" ", "-")

        # Remove or replace special characters, keeping only alphanumeric, hyphens, and underscores
        # This matches GitHub's anchor generation rules
        anchor = re.sub(r"[^\w\-_]", "", anchor)

        # Remove consecutive hyphens
        anchor = re.sub(r"-+", "-", anchor)

        # Remove leading/trailing hyphens
        anchor = anchor.strip("-")

        return anchor

    def _add_line(self, line: str = ""):
        """Add a line to the markdown output."""
        self.markdown_lines.append(line)

    def _add_heading(self, text: str, level: int = 1, anchor: str | None = None, toc_entries: list[str] | None = None):
        """Add a heading with the specified level."""

        level_ = self.initial_level + level
        if anchor:
            html_anchor = f"<a id='{anchor}'></a>\n"
            self._add_line(html_anchor)
        heading = "#" * level_ + " " + text
        self._add_line(heading)
        self._add_line()

        # Add to TOC if enabled
        if self.include_toc and level <= 3:
            indent = "  " * (level - 1)
            if anchor is None:
                anchor = self._generate_anchor(text)
            if toc_entries is not None:
                toc_entries.append(f"{indent}- [{text}](#{anchor})")

    def _format_code_block(self, code: str, language: str = "python") -> str:
        """Format code as a code block."""
        return f"```{language}\n{code}\n```"

    def _format_inline_code(self, code: str) -> str:
        """Format code as inline code."""
        return f"`{code}`"

    def _format_type(self, type_str: str) -> str:
        """Format a type string."""
        if not type_str:
            return ""
        return f"`{type_str}`"

    def get_markdown(self) -> str:
        """Get the complete markdown output."""
        result = []

        idx = 0
        # Replace @@TOC{uuid}TOC@@ with the actual TOC entries
        while idx < len(self.markdown_lines):
            line = self.markdown_lines[idx]
            if m := TOC_PATTERN.match(line):
                toc_uuid = m.group(1)
                if toc_uuid in self.toc_entries:
                    # result.extend(self.toc_entries[toc_uuid])
                    self.markdown_lines[idx : idx + 1] = self.toc_entries[toc_uuid]
                    idx += len(self.toc_entries[toc_uuid]) - 1
            idx += 1

        return "\n".join(self.markdown_lines)

    def on_module(self, module_data: Dict[str, Any]) -> Any:
        self.module_name = module_data.get("module", "")
        file_path = module_data.get("file", "")

        # self._add_heading(f"Module: {self.module_name}", 1)
        # self._add_line(f"**File:** `{file_path}`")
        self._add_line()

        return module_data

    def on_module_complete(self, module_data: Dict[str, Any]) -> Any:
        return module_data

    def on_class(self, class_data: Dict[str, Any], module_name: str) -> Any:
        class_name = class_data.get("name", "")
        short_desc = class_data.get("description", "")
        long_desc = class_data.get("long_description", "")
        bases = class_data.get("bases", [])
        anchor = class_data.get("id")
        toc_uuid = f"{module_name}.{class_name}"

        self._add_heading(f"Class: {class_name}", 1, anchor=anchor)
        if self.include_toc and toc_uuid not in self.toc_entries:
            self.toc_entries[toc_uuid] = []

        self._add_line(f"Module: **{module_name}**\n")
        self._add_line(f"@@TOC{toc_uuid}TOC@@")
        self._add_line()

        if bases:
            # base_list = ", ".join([self._format_inline_code(base) for base in bases])
            base_list = ", ".join(bases)
            self._add_line(f"**Inherits from:** {base_list}")
            self._add_line()

        if short_desc:
            self._add_line(short_desc)
            self._add_line()

        if long_desc:
            self._add_line(long_desc)
            self._add_line()

        # Add class examples if available
        if self.include_examples and class_data.get("examples"):
            self._add_line("**Examples:**")
            self._add_line()
            for example in class_data["examples"]:
                self.visit_example(example, "", class_name, module_name)

        # Add class notes if available
        if self.include_notes and class_data.get("notes"):
            self._add_line("### Notes")
            self._add_line()
            for note in class_data["notes"]:
                self._add_line(f"> {note}")
                self._add_line()

        return class_data

    def on_class_complete(self, class_data: Dict[str, Any], module_name: str) -> Any:
        self._add_line("---")
        self._add_line()
        return class_data

    def on_interface(self, interface_data: Dict[str, Any], module_name: str) -> Any:
        interface_name = interface_data.get("name", "")
        short_desc = interface_data.get("description", "")
        long_desc = interface_data.get("long_description", "")
        anchor = interface_data.get("id")
        toc_uuid = f"{module_name}.{interface_name}"

        self._add_heading(f"Interface: {interface_name}", 1, anchor=anchor)
        if self.include_toc and toc_uuid not in self.toc_entries:
            self.toc_entries[toc_uuid] = []

        self._add_line(f"Module: **{module_name}**\n")
        self._add_line(f"@@TOC{toc_uuid}TOC@@")
        self._add_line()

        if short_desc:
            self._add_line(short_desc)
            self._add_line()

        if long_desc:
            self._add_line(long_desc)
            self._add_line()

        # Add class examples if available
        if self.include_examples and interface_data.get("examples"):
            self._add_line("**Examples:**")
            self._add_line()
            for example in interface_data["examples"]:
                self.visit_example(example, "", interface_name, module_name)

        # Add class notes if available
        if self.include_notes and interface_data.get("notes"):
            self._add_line("### Notes")
            self._add_line()
            for note in interface_data["notes"]:
                self._add_line(f"> {note}")
                self._add_line()

        return interface_data

    def on_interface_complete(self, interface_data: Dict[str, Any], module_name: str) -> Any:
        self._add_line("---")
        self._add_line()
        return interface_data

    def on_method(self, method_data: Dict[str, Any], class_name: Optional[str], module_name: str, method_type: str) -> Any:
        method_name = method_data.get("name", "")
        short_desc = method_data.get("description", "")
        long_desc = method_data.get("long_description", "")

        # Determine method type
        if class_name:
            if method_type == "static":
                method_type = "Static Method"
            elif method_name in ["__init__", "__new__"]:
                method_type = "Constructor"
            elif method_name.startswith("__") and method_name.endswith("__"):
                method_type = "Special Method"
            else:
                method_type = "Method"
            heading = f"{method_type}: {self._format_inline_code(method_name)}"
        else:
            heading = f"Function: {self._format_inline_code(method_name)}"

        anchor = method_data.get("id")
        toc_uuid = f"{module_name}.{class_name}" if class_name else f"{module_name}"
        toc_entries = self.toc_entries.get(toc_uuid) if self.include_toc else None
        self._add_heading(heading, 2, anchor=anchor, toc_entries=toc_entries)

        if short_desc:
            self._add_line(short_desc)
            self._add_line()

        if long_desc:
            self._add_line(long_desc)
            self._add_line()

        # Add parameters section
        params = method_data.get("params", [])
        if params:
            self._add_line("**Parameters:**")
            self._add_line()
            for param in params:
                self.visit_param(param, method_name="", class_name=class_name, module_name=module_name)

            self._add_line()

        # Add returns section
        returns = method_data.get("returns")
        if returns:
            self.visit_returns(returns, method_name, class_name, module_name)

        # Add raises section
        raises = method_data.get("raises", [])
        if raises:
            self.visit_raises(raises, method_name, class_name, module_name)

        # Add examples section
        if self.include_examples and method_data.get("examples"):
            self._add_line("**Examples:**")
            self._add_line()
            for example in method_data["examples"]:
                self.visit_example(example, method_name, class_name, module_name)

        # Add notes section
        if self.include_notes and method_data.get("notes"):
            self._add_line("**Notes:**")
            self._add_line()
            for note in method_data["notes"]:
                self._add_line(f"> {note}")
                self._add_line()

        return method_data

    def on_property(self, property_data: Dict[str, Any], class_name: str, module_name: str) -> Any:
        property_name = property_data.get("name", "")
        short_desc = property_data.get("description", "")
        long_desc = property_data.get("long_description", "")

        self._add_heading(f"Property: {self._format_inline_code(property_name)}", 2)

        if short_desc:
            self._add_line(short_desc)
            self._add_line()

        if long_desc:
            self._add_line(long_desc)
            self._add_line()

        # Add returns section for property
        returns = property_data.get("returns")
        if returns:
            self.visit_returns(returns, property_name, class_name, module_name)
        return_type = property_data.get("type", "")
        if return_type:
            self._add_line(f"**Type:** {self._format_type(return_type)}")
            self._add_line()

        # Add raises section for property
        raises = property_data.get("raises", [])
        if raises:
            self.visit_raises(raises, property_name, class_name, module_name)

        # Add examples section for property
        if self.include_examples and property_data.get("examples"):
            self._add_line("**Examples:**")
            self._add_line()
            for example in property_data["examples"]:
                self.visit_example(example, property_name, class_name, module_name)

        # Add notes section for property
        if self.include_notes and property_data.get("notes"):
            self._add_line("**Notes:**")
            self._add_line()
            for note in property_data["notes"]:
                self._add_line(f"> {note}")
                self._add_line()

        return property_data

    def on_param(self, param_data: Dict[str, Any], method_name: str, class_name: Optional[str], module_name: str) -> Any:
        # Parameters are handled in on_method
        arg_name = param_data.get("name", "")
        arg_type = param_data.get("type", "")
        description = param_data.get("description", "")
        default = param_data.get("default", "")

        param_line = f"- **{arg_name}**"
        if arg_type:
            param_line += f" ({self._format_type(arg_type)})"
        if default:
            param_line += f", default: `{default}`"
        param_line += f": {description}" if description else ""

        self._add_line(param_line)
        return param_data

    def on_attribute(self, attribute_data: Dict[str, Any], method_name: str, class_name: Optional[str], module_name: str) -> Any:
        # Parameters are handled in on_method
        arg_name = attribute_data.get("name", "")
        arg_type = attribute_data.get("type", "")
        description = attribute_data.get("description", "")
        default = attribute_data.get("default", "")

        param_line = f"- att **{arg_name}**"
        if arg_type:
            param_line += f" ({self._format_type(arg_type)})"
        if default:
            param_line += f", default: `{default}`"
        param_line += f": {description}" if description else ""

        self._add_line(param_line)
        return attribute_data

    def on_returns(self, returns_data: Dict[str, Any], method_name: str, class_name: Optional[str], module_name: str) -> Any:
        return_type = returns_data.get("type", "")
        return_desc = returns_data.get("description", "")

        self._add_line("**Returns:**")
        self._add_line()
        return_line = ""
        if return_type:
            return_line += f"{self._format_type(return_type)}"
        if return_desc:
            return_line += f": {return_desc}" if return_type else return_desc
        self._add_line(f"- {return_line}")
        self._add_line()
        return returns_data

    def on_raises(self, raises_data: Dict[str, Any], method_name: str, class_name: Optional[str], module_name: str) -> Any:
        self._add_line("**Raises:**")
        self._add_line()
        for raise_info in raises_data:
            exception_type = raise_info.get("type", "")
            description = raise_info.get("description", "")

            raise_line = ""
            if exception_type:
                raise_line += f"{self._format_type(exception_type)}"
            if description:
                raise_line += f": {description}" if exception_type else description
            self._add_line(f"- {raise_line}")
        self._add_line()
        return raises_data

    def on_example(self, example: str, method_name: str, class_name: Optional[str], module_name: str) -> Any:
        # Examples are handled in on_method
        if "```" in example:
            self._add_line(example)
        else:
            self._add_line(self._format_code_block(example))
        self._add_line()

        return example

    def on_note(self, note: str, method_name: str, class_name: Optional[str], module_name: str) -> Any:
        # Notes are handled in on_method
        return note

    def on_type(self, type_data: Dict[str, Any], module_name: str) -> Any:
        """Called when visiting a type."""
        type_name = type_data.get("name", "")
        anchor = type_data.get("id")
        toc_uuid = f"{module_name}.{type_name}"
        self._add_heading(f"Type: {type_name}", 1, anchor=anchor)
        if self.include_toc and toc_uuid not in self.toc_entries:
            self.toc_entries[toc_uuid] = []

    def on_type_complete(self, type_data: Dict[str, Any], module_name: str) -> Any:
        """Called when type traversal is complete."""
        self._add_line()
        return type_data

    def on_type_alias(self, alias: list[str], type_data: Dict[str, Any], module_name: str = "") -> Any:
        """Visit an alias value."""
        # This method can be overridden by subclasses if needed
        if alias:
            for value in alias:
                if isinstance(value, str):
                    self._add_line(f" * *Alias:* {self._format_type(value)}")
                else:
                    logger.warning(f"Unexpected alias value type: {type(value)} in {type_data.get('name', '')}")
        return alias


def visit_json_file(file_path: Union[str, Path], visitor: DocstringVisitor) -> Any:
    """Load a JSON file and visit it with the given visitor."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return visitor.visit(data)


def parse_arguments():
    """
    Parses the command line arguments.
    """
    parser = ArgumentParser(prog="extract docstrings")
    parser.add_argument("-f", "--file", nargs="+", required=True, help="files to process.")
    parser.add_argument(
        "-r",
        "--root",
        required=False,
        help="root directory to use for relative module names (default: current directory)",
    )
    parser.add_argument("-o", "--output", required=True, help="output folder to write the Markdown results")
    return parser.parse_args()


def to_markdown(filename: Path, root: Path, output: Path, markdown_visitor: MarkdownVisitor | None = None):
    md_fn = Path(filename).with_suffix(".md")
    if output.is_dir():
        md_fn = md_fn.relative_to(root) if root else md_fn
        md_fn = output / md_fn
    else:
        md_fn = output
    logger.debug(f"Converting JSON to Markdown: {md_fn}")
    markdown_visitor = markdown_visitor or MarkdownVisitor()
    visit_json_file(filename, markdown_visitor)
    markdown_output = markdown_visitor.get_markdown()
    # Optionally save to file
    md_fn.parent.mkdir(parents=True, exist_ok=True)
    md_fn.write_text(markdown_output)


def main():

    args = parse_arguments()
    args.file = [Path(f) for f in args.file]
    for fn in args.file:
        if not fn.exists():
            raise FileNotFoundError(f"File {fn} does not exist.")
        root = Path(args.root) if args.root else Path.cwd()
        to_markdown(filename=fn, root=root, output=Path(args.output))


if __name__ == "__main__":
    main()
