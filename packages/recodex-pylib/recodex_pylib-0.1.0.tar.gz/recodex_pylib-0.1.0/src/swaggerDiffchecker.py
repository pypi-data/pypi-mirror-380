import yaml
import os
import sys
from deepdiff import DeepDiff
from pathlib import Path

from recodex_pylib.helpers.utils import camel_case_to_snake_case


class LineStatus:
    """Class that represents the diff lines of an object or list.
    Also holds whether the object introduced some changes on any level of nesting.
    """

    def __init__(self):
        self.lines: list[list | str] = []
        self.changed: bool = False

    def merge(self, other: 'LineStatus', set_added: bool = False, set_removed: bool = False):
        """Adds another diff to this one.

        Args:
            other (LineStatus): The other diff.
            set_added (bool, optional): Whether the lines of the other object should be marked as added.
                Defaults to False.
            set_removed (bool, optional): Whether the lines of the other object should be marked as removed.
                Defaults to False.
        """

        if set_added:
            self.__set_line_changed(other.lines, "+")
        if set_removed:
            self.__set_line_changed(other.lines, "-")
        self.lines.append(other.lines)
        self.changed = self.changed or other.changed

    def print(self):
        """Prints the lines to stdout.
        """

        self.__print(self.lines)

    def __print(self, lines: list[list | str]):
        for line in lines:
            if isinstance(line, str):
                print(line)
            else:
                self.__print(line)

    def get_print_lines(self):
        """Returns a single-level list of lines ready for printing.
        """

        print_lines = []
        self.__get_print_lines(self.lines, print_lines)
        return print_lines

    def __get_print_lines(self, lines: list[list | str], print_lines: list[str]):
        for line in lines:
            if isinstance(line, str):
                print_lines.append(line)
            else:
                self.__get_print_lines(line, print_lines)

    def __set_line_changed(self, lines: list, diff_char: str):
        for i in range(len(lines)):
            if isinstance(lines[i], str):
                chars = list(lines[i])
                chars[0] = diff_char
                lines[i] = "".join(chars)
            else:
                self.__set_line_changed(lines[i], diff_char)


def read_swagger(path: str):
    if not os.path.exists(path):
        raise Exception(f"The path '{path}' does not point to a file.")

    with open(path, "r") as file:
        content = yaml.safe_load(file)
        return content


def find_different_paths(old_swagger: dict, new_swagger: dict):
    diff = DeepDiff(old_swagger["paths"], new_swagger["paths"])
    return diff.affected_root_keys


def split_dict(d: dict):
    literals = []
    objects = []
    for key, value in d.items():
        if isinstance(value, dict) or isinstance(value, list):
            objects.append(key)
        else:
            literals.append(key)
    return (literals, objects)


def split_keys(old_keys: list[str], new_keys: list[str], old_dict: dict, new_dict: dict):
    key_stats = {}
    for key in old_keys:
        if key not in new_keys:
            key_stats[key] = "removed"
        elif old_dict[key] == new_dict[key]:
            key_stats[key] = "kept"
        else:
            key_stats[key] = "modified"
    for key in new_keys:
        if key not in old_keys:
            key_stats[key] = "added"
    return key_stats


def split_parameters(old_parameters: list[dict], new_parameters: list[dict]):
    old_names = []
    new_names = []
    for param in old_parameters:
        old_names.append(param["name"])
    for param in new_parameters:
        new_names.append(param["name"])

    param_stats = {}
    for name in old_names:
        if name not in new_names:
            param_stats[name] = "removed"
        else:
            param_stats[name] = "kept"
    for name in new_names:
        if name not in old_names:
            param_stats[name] = "added"
    return param_stats


def split_lists(old_list: list, new_list: list):
    removed = []
    added = []
    kept = []

    for value in old_list:
        if value in new_list:
            kept.append(value)
        else:
            removed.append(value)
    for value in new_list:
        if value not in old_list:
            added.append(value)

    return (removed, added, kept)


def print_indented_kept(line: str, indentation: int, diff: LineStatus):
    diff.lines.append(" " * (indentation + 2) + line)


def print_indented_added(line: str, indentation: int, diff: LineStatus):
    diff.lines.append("+" + " " * (indentation + 1) + line)
    diff.changed = True


def print_indented_removed(line: str, indentation: int, diff: LineStatus):
    diff.lines.append("-" + " " * (indentation + 1) + line)
    diff.changed = True


def get_param(params: list[dict], name: str):
    for param in params:
        if param["name"] == name:
            return param
    raise Exception(f"Parameter '{name}' not found")


def to_yaml_diff(label: str, old_obj: dict | list, new_obj: dict | list, indentation: int) -> LineStatus:
    diff = LineStatus()
    added = False
    removed = False

    # print the key under which the object is listed
    if bool(old_obj) and bool(new_obj):
        print_indented_kept(f"{label}:", indentation - 2, diff)
    elif not bool(old_obj):
        print_indented_added(f"{label}:", indentation - 2, diff)
        added = True
    else:
        print_indented_removed(f"{label}:", indentation - 2, diff)
        removed = True

    # check whether the objects are lists of dicts
    if isinstance(old_obj, list) or isinstance(new_obj, list):
        if not (isinstance(old_obj, list) and isinstance(new_obj, list)):
            raise Exception("Both parameters have to either be lists, or dicts")
        nested_diff = handle_lists(label, old_obj, new_obj, indentation)
    else:
        nested_diff = handle_dicts(old_obj, new_obj, indentation)

    if (not nested_diff.changed) and ((not added) and (not removed)):
        print_indented_kept("...", indentation, diff)
    else:
        diff.merge(nested_diff, set_added=added, set_removed=removed)

    return diff


def handle_lists(label: str, old_list: list, new_list: list, indentation: int) -> LineStatus:
    diff = LineStatus()

    # special case for parameters - a list of objects
    if label == "parameters":
        param_stats = split_parameters(old_list, new_list)
        for param in old_list:
            # parameters have a name
            name = param["name"]
            status = param_stats[name]
            if status == "kept":
                nested_diff = handle_dicts(param, get_param(new_list, name), indentation)
                # only print out parameters that have changes
                if nested_diff.changed:
                    print_indented_kept("-", indentation - 2, diff)
                    diff.merge(nested_diff)
            elif status == "removed":
                print_indented_removed("-", indentation - 2, diff)
                diff.merge(handle_dicts(param, {}, indentation))
        for param in new_list:
            name = param["name"]
            status = param_stats[name]
            if status == "added":
                print_indented_added("-", indentation - 2, diff)
                diff.merge(handle_dicts({}, param, indentation))
    # handle general lists
    else:
        removed, added, kept = split_lists(old_list, new_list)
        # print <empty list> if the list is empty
        if len(removed) == 0 and len(added) == 0 and len(kept) == 0:
            print_indented_kept("<empty list>", indentation, diff)

        for value in kept:
            print_indented_kept("-", indentation - 2, diff)
            print_indented_kept(value, indentation, diff)
        for value in removed:
            print_indented_removed("-", indentation - 2, diff)
            print_indented_removed(value, indentation, diff)
        for value in added:
            print_indented_added("-", indentation - 2, diff)
            print_indented_added(value, indentation, diff)

    return diff


def handle_dicts(old_dict: dict, new_dict: dict, indentation: int) -> LineStatus:
    diff = LineStatus()

    # split keys into literal and nested object keys
    old_literals, old_objects = split_dict(old_dict)
    new_literals, new_objects = split_dict(new_dict)

    # print an <empty object> string if there are no keys
    if len(old_literals) == 0 and len(old_objects) == 0 and len(new_literals) == 0 and len(new_objects) == 0:
        print_indented_kept("<empty object>", indentation, diff)

    # categorize literal keys by their changed status
    key_stats = split_keys(old_literals, new_literals, old_dict, new_dict)
    # kept literals and objects will be replaced by a single ellipsis
    some_kept = False
    for key, status in key_stats.items():
        if status == "kept":
            # special case for parameters in lists, make the object identifiable by name
            if key == "name" or key == "operationId":
                print_indented_kept(f"{key}: {old_dict[key]}", indentation, diff)
            # replace kept parameters with an ellipsis
            elif not some_kept:
                print_indented_kept("...", indentation, diff)
                some_kept = True
    for key, status in key_stats.items():
        if status == "removed":
            print_indented_removed(f"{key}: {old_dict[key]}", indentation, diff)
        elif status == "added":
            print_indented_added(f"{key}: {new_dict[key]}", indentation, diff)
        elif status == "modified":
            print_indented_removed(f"{key}: {old_dict[key]}", indentation, diff)
            print_indented_added(f"{key}: {new_dict[key]}", indentation, diff)

    # categorize object keys by their changed status
    obj_stats = split_keys(old_objects, new_objects, old_dict, new_dict)
    for key, status in obj_stats.items():
        if status == "kept":
            if isinstance(old_dict[key], dict):
                nested_diff = to_yaml_diff(key, old_dict[key], new_dict.get(key, {}), indentation + 2)
            else:
                nested_diff = to_yaml_diff(key, old_dict[key], new_dict.get(key, []), indentation + 2)

            # if the nested object holds no changes, replace it with an ellipsis
            if not nested_diff.changed:
                if not some_kept:
                    print_indented_kept("...", indentation, diff)
                    some_kept = True
            else:
                diff.merge(nested_diff)
        elif status == "removed" or status == "modified":
            if isinstance(old_dict[key], dict):
                diff.merge(to_yaml_diff(key, old_dict[key], new_dict.get(key, {}), indentation + 2))
            else:
                diff.merge(to_yaml_diff(key, old_dict[key], new_dict.get(key, []), indentation + 2))
        else:
            if isinstance(new_dict[key], dict):
                diff.merge(to_yaml_diff(key, {}, new_dict[key], indentation + 2))
            else:
                diff.merge(to_yaml_diff(key, [], new_dict[key], indentation + 2))

    return diff


def new_changes(old_swagger: dict, new_swagger: dict) -> bool:
    """Returns whether there are some changes in the swaggers.
    """

    return len(find_different_paths(old_swagger, new_swagger)) > 0


def get_operation_id(old_method_content: dict, new_method_content: dict):
    if "operationId" in new_method_content:
        return new_method_content["operationId"]
    return old_method_content["operationId"]


def get_diff_lines(old_swagger: dict, new_swagger: dict) -> list[str]:
    """Returns a list of lines representing the diff in markdown format
    """

    lines = []
    paths = find_different_paths(old_swagger, new_swagger)
    for path in paths:
        old_content: dict = old_swagger["paths"].get(path, {})
        new_content: dict = new_swagger["paths"].get(path, {})

        # aggregate all endpoint methods used
        method_set: set[str] = set()
        for old_method in old_content.keys():
            method_set.add(old_method)
        for new_method in new_content.keys():
            method_set.add(new_method)

        for method in method_set:
            old_method_content: dict = old_content.get(method, {})
            new_method_content: dict = new_content.get(method, {})

            diff = LineStatus()
            added = False
            removed = False
            if path in old_swagger["paths"] and path in new_swagger["paths"]:
                print_indented_kept(f"{path}:", -2, diff)
            elif path in new_swagger["paths"]:
                print_indented_added(f"{path}:", -2, diff)
                added = True
            else:
                print_indented_removed(f"{path}:", -2, diff)
                removed = True

            nested_diff = to_yaml_diff(method, old_method_content, new_method_content, 2)
            diff.merge(nested_diff, set_added=added, set_removed=removed)

            operation_id = get_operation_id(old_method_content, new_method_content)
            operation_id = camel_case_to_snake_case(operation_id)

            lines.append(f"### {operation_id}")
            lines.append("```diff")
            lines += diff.get_print_lines()
            lines.append("```")

    for i in range(len(lines)):
        lines[i] += "\n"

    return lines


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception(f"Expected 2 parameters (compared swagger paths), but {len(sys.argv) - 1} were provided.")

    old_swagger = read_swagger(sys.argv[1])
    new_swagger = read_swagger(sys.argv[2])
    # check if the swaggers changed
    if new_changes(old_swagger, new_swagger):
        changes_file_path = Path(__file__).parent.parent.joinpath("api-changes.md")
        # replace the API changes in the file
        with open(changes_file_path, "w") as file:
            lines = get_diff_lines(old_swagger, new_swagger)
            file.writelines(lines)
