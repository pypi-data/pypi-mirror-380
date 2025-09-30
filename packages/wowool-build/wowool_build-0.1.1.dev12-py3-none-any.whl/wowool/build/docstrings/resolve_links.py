from argparse import ArgumentParser
from pathlib import Path
import json
from dataclasses import dataclass
from logging import getLogger
from re import sub, compile, Pattern as RegexPattern


logger = getLogger(__name__)


def parse_arguments():
    """
    Parses the command line arguments.
    """
    parser = ArgumentParser(prog="extract docstrings")
    parser.add_argument("-f", "--file", nargs="+", required=True, help="the json files to process.")
    parser.add_argument("-p", "--prefix", required=False, help="prefix when resolving links", default="{{url}}#")
    parser.add_argument("-o", "--output", required=False, help="output file to write the JSON result")
    parser.add_argument(
        "-s",
        "--search_and_replace",
        nargs="+",
        help="list of search and replace patterns in the format old=new, e.g. m1.dataclass=m2.dataclass",
    )
    return parser.parse_args()


@dataclass
class LinkInfo:
    id: str
    filename: Path


def _generate_anchor(text: str) -> str:
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


def load_files(files: list[Path], prefix: str, root: Path | None = None) -> dict:
    data = {}
    for file in files:
        fn = file.relative_to(root) if root else file
        module = json.loads(file.read_text())
        for item in module.get("classes", []):
            id = f"{prefix}{item['id']}"
            li = LinkInfo(id=id, filename=fn.with_suffix(".md"))
            data[item["name"]] = li
            data[id] = li

            for method in item.get("methods", []):

                mid = f"{id}.{method['name']}"
                li = LinkInfo(id=mid, filename=fn.with_suffix(".md"))
                data[method["name"]] = li
                data[mid] = li
    return data


def substitute_links(file: Path, text: str, data: dict, pattern: RegexPattern[str]) -> str:
    """
    Substitute class names in backticks with their full qualified names.

    Args:
        text (str): The text to process
        data (dict): Dictionary mapping class names to their full qualified names

    Returns:
        str: Text with substituted links
    """
    if not text:
        return text

    # pattern = compile(r"(:?" + pattern_values + r")")

    def replace_match(match):
        matched_text = match.group(0)
        # Remove backticks from the matched text to get the class name
        class_name = match.group(1)
        # Get the full qualified name(s) for this class
        li = data.get(class_name)
        if not li:
            return matched_text
        full_name = li.id
        if "{{markdown_filename}}" in full_name:
            if li.filename.stem == file.stem:
                # If the filename matches, use the current file's name
                full_name = full_name.replace("{{markdown_filename}}", "")
            else:
                full_name = full_name.replace("{{markdown_filename}}", str(li.filename).replace("/", "_"))
        relative_offset = match.regs[0][0]
        offset_begin = match.regs[1][0] - relative_offset
        offset_end = match.regs[1][1] - relative_offset
        retval = matched_text[:offset_begin] + f"[{class_name}]({full_name})" + matched_text[offset_end:]
        return retval

    return sub(pattern, replace_match, text)


def substitute_links_in_method(file: Path, method, data, pattern: RegexPattern[str]):
    if "long_description" in method and method["long_description"]:
        original = method["long_description"]
        substituted = substitute_links(file, original, data, pattern)
        if original != substituted:
            print(f"    Method {method['name']}: substituted links")
            method["long_description"] = substituted

    if "description" in method and method["description"]:
        original = method["description"]
        substituted = substitute_links(file, original, data, pattern)
        if original != substituted:
            method["description"] = substituted

    if returns := method.get("returns"):
        original = returns.get("type", "")
        if not original:
            return
        substituted = substitute_links(file, original, data, pattern)
        if original != substituted:
            returns["type"] = substituted

    if original := method.get("type"):
        if not original:
            return
        substituted = substitute_links(file, original, data, pattern)
        if original != substituted:
            method["type"] = substituted

    if params := method.get("params"):
        for param in params:
            original = param.get("type", "")
            if not original:
                return
            substituted = substitute_links(file, original, data, pattern)
            if original != substituted:
                param["type"] = substituted


def resolve_links(
    files: list[Path],
    output: Path,
    prefix: str = "{{url}}#",
    root: Path | None = None,
    search_and_replace: list[tuple[str, str]] | None = None,
):

    data = load_files(files, prefix, root)
    # for key, values in data.items():
    #     print(f"  {key}: {values}")
    # Create pattern to match class names in backticks
    keys = [f"{key}" for key in data.keys() if key]
    pattern_values = f'{"|".join(keys)}'
    pattern = compile(r"(?:\[|\b)(" + pattern_values + r")(?:\]|\b)")

    # Process each file and substitute links
    for file in files:
        # print(f"\nProcessing file: {file}")
        json_text = file.read_text(encoding="utf-8")
        if search_and_replace:
            for old, new in search_and_replace:
                json_text = json_text.replace(old, new)
                logger.debug(f"Replaced {old} with {new} in file {file}")
        module = json.loads(json_text)

        # Process classes and their methods
        if "classes" in module:
            for class_info in module["classes"]:
                if bases := class_info.get("bases"):
                    for i, base in enumerate(bases):
                        original = base
                        substituted = substitute_links(file, original, data, pattern)
                        if original != substituted:
                            logger.debug(f"  Class {class_info['name']}: substituted base type")
                            bases[i] = substituted

                if description := class_info.get("description"):
                    original = description
                    substituted = substitute_links(file, description, data, pattern)
                    if original != substituted:
                        logger.debug(f"  Class {class_info['name']}: substituted description")
                        class_info["description"] = substituted

                if params := class_info.get("params"):
                    for param in params:
                        original = param.get("type", "")
                        if not original:
                            continue
                        substituted = substitute_links(file, original, data, pattern)
                        if original != substituted:
                            logger.debug(f"  Class {class_info['name']}: substituted parameter type")
                            param["type"] = substituted
                # Process methods
                if "attributes" in class_info:
                    for arg in class_info["attributes"]:
                        original = arg["type"]
                        substituted = substitute_links(file, original, data, pattern)
                        if original != substituted:
                            logger.debug(f"  Class {class_info['name']}: substituted attribute type")
                            arg["type   "] = substituted

                if "methods" in class_info:
                    for method in class_info["methods"]:
                        substitute_links_in_method(file, method, data, pattern)
                if "properties" in class_info:
                    for method in class_info["properties"]:
                        substitute_links_in_method(file, method, data, pattern)
                if "static_methods" in class_info:
                    for method in class_info["static_methods"]:
                        substitute_links_in_method(file, method, data, pattern)

        # Process module-level methods
        if "methods" in module:
            for method in module["methods"]:
                substitute_links_in_method(file, method, data, pattern)

        # Write the updated module
        if output:
            if output.is_dir():
                ofn = file.relative_to(root) if root else file
                ofn = str(ofn).replace("/", "_")
                output_file = Path(output) / ofn
                output_file.parent.mkdir(parents=True, exist_ok=True)
            else:
                output_file = output
            output_file.write_text(json.dumps(module, indent=2))

            logger.info(f"Resolved: {output_file}")
        else:
            print(f"    Updated JSON:\n{json.dumps(module, indent=2)}")


def main():
    args = parse_arguments()
    args.file = [Path(f) for f in args.file]
    resolve_links(
        args.file,
        args.output,
        args.prefix,
        search_and_replace=[r.split("=") for r in args.search_and_replace] if args.search_and_replace else None,
    )


if __name__ == "__main__":
    main()
