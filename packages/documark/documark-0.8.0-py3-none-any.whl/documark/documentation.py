
import os
import re
import operator as _op
from types import MethodType
from collections.abc import Iterable


def document_namespaces(
    namespaces: Iterable[type],
    docs_root: str,
) -> None:
    r"""
    """
    #[
    for n in namespaces:
        print(f"Documenting {n.__name__}", )
        document_namespace(n, docs_root, )
    #]


def document_namespace(
    namespace: type,
    docs_root: str,
) -> None:
    """
    """
    namespace_docs_path = os.path.join(docs_root, *namespace._documark_path, )
    docstring = _remove_visual_divider(namespace.__doc__, )
    if namespace._documark_categories:
        attributes = _collect_documented_attributes_from_class(namespace, )
        properties = _collect_documented_properties_from_class(namespace, )
        attribute_to_docstring = _create_attribute_to_docstring(attributes, )
        property_to_docstring = _create_attribute_to_docstring(properties, )
        attribute_to_docstring = dict(sorted(
            attribute_to_docstring.items(),
            key=lambda item: (-item[0]._documark_priority, item[0]._documark_call_name.lower(), ),
        ))
        docstring += _create_property_list(namespace, property_to_docstring, )
        docstring += _create_categorical_list(namespace, attribute_to_docstring, )
        docstring += _add_attributes(attribute_to_docstring, )
    with open(namespace_docs_path, "wt+") as f:
        f.write(docstring, )


_ICONS = {
    None: ":octicons-file-24:",
    "property": ":octicons-package-24:",
}
_PAGES_REFERENCE = "_documark_reference"
_CATEGORY_TABLE_HEADING = (
    "Function | Description\n"
    "----------|------------\n"
)
_PROPERTY_TABLE_HEADING = (
    "Property | Description\n"
    "----------|------------\n"
)
_DIVIDER_PATTERN = re.compile(r"\n·{20,}\n", )
_DIVIDER_PATTERN_LEGACY = re.compile(r"\n\.{20,}\n", )


def _remove_visual_divider(docstring: str, ) -> str:
    docstring = _DIVIDER_PATTERN.sub("", docstring)
    docstring = _DIVIDER_PATTERN_LEGACY.sub("", docstring)
    return docstring


def _create_categorical_list(namespace: type, attribute_to_docstring: dict, ) -> str:
    docstring = (
        "\n\n\n"
        "Categorical list of functions\n"
        "-------------------------------\n\n"
    )
    for category, category_description in namespace._documark_categories.items():
        if category == "property":
            continue
        docstring += f"### {category_description} ###\n\n"
        docstring += _CATEGORY_TABLE_HEADING
        attribute_to_docstring_of_category = _collect_attribute_to_docstring_of_category(attribute_to_docstring, category, )
        for attribute in attribute_to_docstring_of_category.keys():
            icon = _ICONS.get(attribute._documark_category, _ICONS[None], )
            docstring += f"[`{attribute._documark_call_name}`](#{_get_anchor(attribute._documark_call_name, )}) | {attribute._documark_tagline}\n"
        docstring += "\n\n"
    return docstring


def _create_property_list(namespace: type, property_to_docstring: dict, ) -> str:
    docstring = (
        "\n\n\n"
        "Directly accessible properties\n"
        "------------------------------\n\n"
    )
    category = "property"
    docstring += _PROPERTY_TABLE_HEADING
    property_to_docstring_of_category = _collect_attribute_to_docstring_of_category(property_to_docstring, category, )
    for property in property_to_docstring_of_category.keys():
        icon = _ICONS.get(property._documark_category, _ICONS[None], )
        docstring += f"`{property._documark_call_name}` | {property._documark_tagline}\n"
    docstring += "\n\n"
    return docstring


def _add_attributes(attribute_to_docstring: dict, ) -> None:
        return "\n\n\n".join(
            _finalize_attribute_docstring(a, d, )
            for a, d in attribute_to_docstring.items()
            if a._documark_category != "property"
        )


def _collect_documented_attributes_from_class(namespace: type, ) -> list:
    return tuple(
        getattr(namespace, attribute_name, )
        for attribute_name in dir(namespace)
        if getattr(getattr(namespace, attribute_name, ), _PAGES_REFERENCE, False)
    )


def _collect_documented_properties_from_class(namespace: type, ) -> list:
    return tuple(
        getattr(namespace, attribute_name, ).fget
        for attribute_name in dir(namespace)
        if (
            hasattr(getattr(namespace, attribute_name, ), "fget")
            and getattr(getattr(namespace, attribute_name).fget, _PAGES_REFERENCE, False)
        )
    )


def _create_attribute_to_docstring(references: list, ) -> dict:
    default_extractor = _DOCSTRING_EXTRACTOR[None]
    return {
        attribute: _DOCSTRING_EXTRACTOR.get(type(attribute), default_extractor)(attribute, )
        for attribute in references
    }


def _collect_attribute_to_docstring_of_category(attribute_to_docstring: dict, category: str, ) -> dict:
    return {
        attribute: attribute_docstring
        for attribute, attribute_docstring in attribute_to_docstring.items()
        if attribute._documark_category == category
    }


def _finalize_attribute_docstring(attribute, docstring: str, ) -> str:
    docstring = _remove_visual_divider(docstring, )
    return docstring


def _get_anchor(call_name: str) -> str:
    return call_name.replace(".", "").lower()


_DOCSTRING_EXTRACTOR = {
    None: _op.attrgetter("__doc__", ),
    MethodType: _op.attrgetter("__func__.__doc__", ),
}


