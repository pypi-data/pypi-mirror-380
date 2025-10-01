from datetime import datetime
from typing import Union

import pytest
from pydantic import AnyUrl, TypeAdapter, ValidationError

from marvin.utilities.jsonschema import hash_schema, jsonschema_to_type, merge_defaults


class TestSimpleTypes:
    """Test suite for basic type validation."""

    @pytest.fixture
    def simple_string(self):
        return jsonschema_to_type({"type": "string"})

    @pytest.fixture
    def simple_number(self):
        return jsonschema_to_type({"type": "number"})

    @pytest.fixture
    def simple_integer(self):
        return jsonschema_to_type({"type": "integer"})

    @pytest.fixture
    def simple_boolean(self):
        return jsonschema_to_type({"type": "boolean"})

    @pytest.fixture
    def simple_null(self):
        return jsonschema_to_type({"type": "null"})

    def test_string_accepts_string(self, simple_string):
        validator = TypeAdapter(simple_string)
        assert validator.validate_python("test") == "test"

    def test_string_rejects_number(self, simple_string):
        validator = TypeAdapter(simple_string)
        with pytest.raises(ValidationError):
            validator.validate_python(123)

    def test_number_accepts_float(self, simple_number):
        validator = TypeAdapter(simple_number)
        assert validator.validate_python(123.45) == 123.45

    def test_number_accepts_integer(self, simple_number):
        validator = TypeAdapter(simple_number)
        assert validator.validate_python(123) == 123

    def test_number_accepts_numeric_string(self, simple_number):
        validator = TypeAdapter(simple_number)
        assert validator.validate_python("123.45") == 123.45
        assert validator.validate_python("123") == 123

    def test_number_rejects_invalid_string(self, simple_number):
        validator = TypeAdapter(simple_number)
        with pytest.raises(ValidationError):
            validator.validate_python("not a number")

    def test_integer_accepts_integer(self, simple_integer):
        validator = TypeAdapter(simple_integer)
        assert validator.validate_python(123) == 123

    def test_integer_accepts_integer_string(self, simple_integer):
        validator = TypeAdapter(simple_integer)
        assert validator.validate_python("123") == 123

    def test_integer_rejects_float(self, simple_integer):
        validator = TypeAdapter(simple_integer)
        with pytest.raises(ValidationError):
            validator.validate_python(123.45)

    def test_integer_rejects_float_string(self, simple_integer):
        validator = TypeAdapter(simple_integer)
        with pytest.raises(ValidationError):
            validator.validate_python("123.45")

    def test_boolean_accepts_boolean(self, simple_boolean):
        validator = TypeAdapter(simple_boolean)
        assert validator.validate_python(True) is True
        assert validator.validate_python(False) is False

    def test_boolean_accepts_boolean_strings(self, simple_boolean):
        validator = TypeAdapter(simple_boolean)
        assert validator.validate_python("true") is True
        assert validator.validate_python("True") is True
        assert validator.validate_python("false") is False
        assert validator.validate_python("False") is False

    def test_boolean_rejects_invalid_string(self, simple_boolean):
        validator = TypeAdapter(simple_boolean)
        with pytest.raises(ValidationError):
            validator.validate_python("not a boolean")

    def test_null_accepts_none(self, simple_null):
        validator = TypeAdapter(simple_null)
        assert validator.validate_python(None) is None

    def test_null_rejects_false(self, simple_null):
        validator = TypeAdapter(simple_null)
        with pytest.raises(ValidationError):
            validator.validate_python(False)


class TestStringConstraints:
    """Test suite for string constraint validation."""

    @pytest.fixture
    def min_length_string(self):
        return jsonschema_to_type({"type": "string", "minLength": 3})

    @pytest.fixture
    def max_length_string(self):
        return jsonschema_to_type({"type": "string", "maxLength": 5})

    @pytest.fixture
    def pattern_string(self):
        return jsonschema_to_type({"type": "string", "pattern": "^[A-Z][a-z]+$"})

    @pytest.fixture
    def email_string(self):
        return jsonschema_to_type({"type": "string", "format": "email"})

    def test_min_length_accepts_valid(self, min_length_string):
        validator = TypeAdapter(min_length_string)
        assert validator.validate_python("test") == "test"

    def test_min_length_rejects_short(self, min_length_string):
        validator = TypeAdapter(min_length_string)
        with pytest.raises(ValidationError):
            validator.validate_python("ab")

    def test_max_length_accepts_valid(self, max_length_string):
        validator = TypeAdapter(max_length_string)
        assert validator.validate_python("test") == "test"

    def test_max_length_rejects_long(self, max_length_string):
        validator = TypeAdapter(max_length_string)
        with pytest.raises(ValidationError):
            validator.validate_python("toolong")

    def test_pattern_accepts_valid(self, pattern_string):
        validator = TypeAdapter(pattern_string)
        assert validator.validate_python("Hello") == "Hello"

    def test_pattern_rejects_invalid(self, pattern_string):
        validator = TypeAdapter(pattern_string)
        with pytest.raises(ValidationError):
            validator.validate_python("hello")

    def test_email_accepts_valid(self, email_string):
        validator = TypeAdapter(email_string)
        result = validator.validate_python("test@example.com")
        assert result == "test@example.com"

    def test_email_rejects_invalid(self, email_string):
        validator = TypeAdapter(email_string)
        with pytest.raises(ValidationError):
            validator.validate_python("not-an-email")


class TestNumberConstraints:
    """Test suite for numeric constraint validation."""

    @pytest.fixture
    def multiple_of_number(self):
        return jsonschema_to_type({"type": "number", "multipleOf": 0.5})

    @pytest.fixture
    def min_number(self):
        return jsonschema_to_type({"type": "number", "minimum": 0})

    @pytest.fixture
    def exclusive_min_number(self):
        return jsonschema_to_type({"type": "number", "exclusiveMinimum": 0})

    @pytest.fixture
    def max_number(self):
        return jsonschema_to_type({"type": "number", "maximum": 100})

    @pytest.fixture
    def exclusive_max_number(self):
        return jsonschema_to_type({"type": "number", "exclusiveMaximum": 100})

    def test_multiple_of_accepts_valid(self, multiple_of_number):
        validator = TypeAdapter(multiple_of_number)
        assert validator.validate_python(2.5) == 2.5

    def test_multiple_of_rejects_invalid(self, multiple_of_number):
        validator = TypeAdapter(multiple_of_number)
        with pytest.raises(ValidationError):
            validator.validate_python(2.7)

    def test_minimum_accepts_equal(self, min_number):
        validator = TypeAdapter(min_number)
        assert validator.validate_python(0) == 0

    def test_minimum_rejects_less(self, min_number):
        validator = TypeAdapter(min_number)
        with pytest.raises(ValidationError):
            validator.validate_python(-1)

    def test_exclusive_minimum_rejects_equal(self, exclusive_min_number):
        validator = TypeAdapter(exclusive_min_number)
        with pytest.raises(ValidationError):
            validator.validate_python(0)

    def test_maximum_accepts_equal(self, max_number):
        validator = TypeAdapter(max_number)
        assert validator.validate_python(100) == 100

    def test_maximum_rejects_greater(self, max_number):
        validator = TypeAdapter(max_number)
        with pytest.raises(ValidationError):
            validator.validate_python(101)

    def test_exclusive_maximum_rejects_equal(self, exclusive_max_number):
        validator = TypeAdapter(exclusive_max_number)
        with pytest.raises(ValidationError):
            validator.validate_python(100)


class TestArrayTypes:
    """Test suite for array validation."""

    @pytest.fixture
    def string_array(self):
        return jsonschema_to_type({"type": "array", "items": {"type": "string"}})

    @pytest.fixture
    def min_items_array(self):
        return jsonschema_to_type(
            {"type": "array", "items": {"type": "string"}, "minItems": 2}
        )

    @pytest.fixture
    def max_items_array(self):
        return jsonschema_to_type(
            {"type": "array", "items": {"type": "string"}, "maxItems": 3}
        )

    @pytest.fixture
    def unique_items_array(self):
        return jsonschema_to_type(
            {"type": "array", "items": {"type": "string"}, "uniqueItems": True}
        )

    def test_array_accepts_valid_items(self, string_array):
        validator = TypeAdapter(string_array)
        assert validator.validate_python(["a", "b"]) == ["a", "b"]

    def test_array_rejects_invalid_items(self, string_array):
        validator = TypeAdapter(string_array)
        with pytest.raises(ValidationError):
            validator.validate_python([1, "b"])

    def test_min_items_accepts_valid(self, min_items_array):
        validator = TypeAdapter(min_items_array)
        assert validator.validate_python(["a", "b"]) == ["a", "b"]

    def test_min_items_rejects_too_few(self, min_items_array):
        validator = TypeAdapter(min_items_array)
        with pytest.raises(ValidationError):
            validator.validate_python(["a"])

    def test_max_items_accepts_valid(self, max_items_array):
        validator = TypeAdapter(max_items_array)
        assert validator.validate_python(["a", "b", "c"]) == ["a", "b", "c"]

    def test_max_items_rejects_too_many(self, max_items_array):
        validator = TypeAdapter(max_items_array)
        with pytest.raises(ValidationError):
            validator.validate_python(["a", "b", "c", "d"])

    def test_unique_items_accepts_unique(self, unique_items_array):
        validator = TypeAdapter(unique_items_array)
        assert isinstance(validator.validate_python(["a", "b"]), set)

    def test_unique_items_converts_duplicates(self, unique_items_array):
        validator = TypeAdapter(unique_items_array)
        result = validator.validate_python(["a", "a", "b"])
        assert result == {"a", "b"}


class TestObjectTypes:
    """Test suite for object validation."""

    @pytest.fixture
    def simple_object(self):
        return jsonschema_to_type(
            {
                "type": "object",
                "properties": {"name": {"type": "string"}, "age": {"type": "integer"}},
            }
        )

    @pytest.fixture
    def required_object(self):
        return jsonschema_to_type(
            {
                "type": "object",
                "properties": {"name": {"type": "string"}, "age": {"type": "integer"}},
                "required": ["name"],
            }
        )

    @pytest.fixture
    def nested_object(self):
        return jsonschema_to_type(
            {
                "type": "object",
                "properties": {
                    "user": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "age": {"type": "integer"},
                        },
                        "required": ["name"],
                    }
                },
            }
        )

    def test_object_accepts_valid(self, simple_object):
        validator = TypeAdapter(simple_object)
        result = validator.validate_python({"name": "test", "age": 30})
        assert result.name == "test"
        assert result.age == 30

    def test_object_accepts_extra_properties(self, simple_object):
        validator = TypeAdapter(simple_object)
        result = validator.validate_python(
            {"name": "test", "age": 30, "extra": "field"}
        )
        assert result.name == "test"
        assert result.age == 30
        assert not hasattr(result, "extra")

    def test_required_accepts_valid(self, required_object):
        validator = TypeAdapter(required_object)
        result = validator.validate_python({"name": "test"})
        assert result.name == "test"
        assert result.age is None

    def test_required_rejects_missing(self, required_object):
        validator = TypeAdapter(required_object)
        with pytest.raises(ValidationError):
            validator.validate_python({})

    def test_nested_accepts_valid(self, nested_object):
        validator = TypeAdapter(nested_object)
        result = validator.validate_python({"user": {"name": "test", "age": 30}})
        assert result.user.name == "test"
        assert result.user.age == 30

    def test_nested_rejects_invalid(self, nested_object):
        validator = TypeAdapter(nested_object)
        with pytest.raises(ValidationError):
            validator.validate_python({"user": {"age": 30}})


class TestDefaultValues:
    """Test suite for default value handling."""

    @pytest.fixture
    def simple_defaults(self):
        return jsonschema_to_type(
            {
                "type": "object",
                "properties": {
                    "name": {"type": "string", "default": "anonymous"},
                    "age": {"type": "integer", "default": 0},
                },
            }
        )

    @pytest.fixture
    def nested_defaults(self):
        return jsonschema_to_type(
            {
                "type": "object",
                "properties": {
                    "user": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "default": "anonymous"},
                            "settings": {
                                "type": "object",
                                "properties": {
                                    "theme": {"type": "string", "default": "light"}
                                },
                                "default": {"theme": "dark"},
                            },
                        },
                        "default": {"name": "guest", "settings": {"theme": "system"}},
                    }
                },
            }
        )

    def test_simple_defaults_empty_object(self, simple_defaults):
        validator = TypeAdapter(simple_defaults)
        result = validator.validate_python({})
        assert result.name == "anonymous"
        assert result.age == 0

    def test_simple_defaults_partial_override(self, simple_defaults):
        validator = TypeAdapter(simple_defaults)
        result = validator.validate_python({"name": "test"})
        assert result.name == "test"
        assert result.age == 0

    def test_nested_defaults_empty_object(self, nested_defaults):
        validator = TypeAdapter(nested_defaults)
        result = validator.validate_python({})
        assert result.user.name == "guest"
        assert result.user.settings.theme == "system"

    def test_nested_defaults_partial_override(self, nested_defaults):
        validator = TypeAdapter(nested_defaults)
        result = validator.validate_python({"user": {"name": "test"}})
        assert result.user.name == "test"
        assert result.user.settings.theme == "system"


class TestUnionTypes:
    """Test suite for testing union type behaviors."""

    @pytest.fixture
    def heterogeneous_union(self):
        return jsonschema_to_type({"type": ["string", "number", "boolean", "null"]})

    @pytest.fixture
    def union_with_constraints(self):
        return jsonschema_to_type(
            {"type": ["string", "number"], "minLength": 3, "minimum": 0}
        )

    @pytest.fixture
    def union_with_formats(self):
        return jsonschema_to_type({"type": ["string", "null"], "format": "email"})

    @pytest.fixture
    def nested_union_array(self):
        return jsonschema_to_type(
            {"type": "array", "items": {"type": ["string", "number"]}}
        )

    @pytest.fixture
    def nested_union_object(self):
        return jsonschema_to_type(
            {
                "type": "object",
                "properties": {
                    "id": {"type": ["string", "integer"]},
                    "data": {
                        "type": ["object", "null"],
                        "properties": {"value": {"type": "string"}},
                    },
                },
            }
        )

    def test_heterogeneous_accepts_string(self, heterogeneous_union):
        validator = TypeAdapter(heterogeneous_union)
        assert validator.validate_python("test") == "test"

    def test_heterogeneous_accepts_number(self, heterogeneous_union):
        validator = TypeAdapter(heterogeneous_union)
        assert validator.validate_python(123.45) == 123.45

    def test_heterogeneous_accepts_boolean(self, heterogeneous_union):
        validator = TypeAdapter(heterogeneous_union)
        assert validator.validate_python(True) is True

    def test_heterogeneous_accepts_null(self, heterogeneous_union):
        validator = TypeAdapter(heterogeneous_union)
        assert validator.validate_python(None) is None

    def test_heterogeneous_rejects_array(self, heterogeneous_union):
        validator = TypeAdapter(heterogeneous_union)
        with pytest.raises(ValidationError):
            validator.validate_python([])

    def test_constrained_string_valid(self, union_with_constraints):
        validator = TypeAdapter(union_with_constraints)
        assert validator.validate_python("test") == "test"

    def test_constrained_string_invalid(self, union_with_constraints):
        validator = TypeAdapter(union_with_constraints)
        with pytest.raises(ValidationError):
            validator.validate_python("ab")

    def test_constrained_number_valid(self, union_with_constraints):
        validator = TypeAdapter(union_with_constraints)
        assert validator.validate_python(10) == 10

    def test_constrained_number_invalid(self, union_with_constraints):
        validator = TypeAdapter(union_with_constraints)
        with pytest.raises(ValidationError):
            validator.validate_python(-1)

    def test_format_valid_email(self, union_with_formats):
        validator = TypeAdapter(union_with_formats)
        result = validator.validate_python("test@example.com")
        assert isinstance(result, str)

    def test_format_valid_null(self, union_with_formats):
        validator = TypeAdapter(union_with_formats)
        assert validator.validate_python(None) is None

    def test_format_invalid_email(self, union_with_formats):
        validator = TypeAdapter(union_with_formats)
        with pytest.raises(ValidationError):
            validator.validate_python("not-an-email")

    def test_nested_array_mixed_types(self, nested_union_array):
        validator = TypeAdapter(nested_union_array)
        result = validator.validate_python(["test", 123, "abc"])
        assert result == ["test", 123, "abc"]

    def test_nested_array_rejects_invalid(self, nested_union_array):
        validator = TypeAdapter(nested_union_array)
        with pytest.raises(ValidationError):
            validator.validate_python(["test", ["not", "allowed"], "abc"])

    def test_nested_object_string_id(self, nested_union_object):
        validator = TypeAdapter(nested_union_object)
        result = validator.validate_python({"id": "abc123", "data": {"value": "test"}})
        assert result.id == "abc123"
        assert result.data.value == "test"

    def test_nested_object_integer_id(self, nested_union_object):
        validator = TypeAdapter(nested_union_object)
        result = validator.validate_python({"id": 123, "data": None})
        assert result.id == 123
        assert result.data is None


class TestFormatTypes:
    """Test suite for format type validation."""

    @pytest.fixture
    def datetime_format(self):
        return jsonschema_to_type({"type": "string", "format": "date-time"})

    @pytest.fixture
    def email_format(self):
        return jsonschema_to_type({"type": "string", "format": "email"})

    @pytest.fixture
    def uri_format(self):
        return jsonschema_to_type({"type": "string", "format": "uri"})

    @pytest.fixture
    def uri_reference_format(self):
        return jsonschema_to_type({"type": "string", "format": "uri-reference"})

    @pytest.fixture
    def json_format(self):
        return jsonschema_to_type({"type": "string", "format": "json"})

    @pytest.fixture
    def mixed_formats_object(self):
        return jsonschema_to_type(
            {
                "type": "object",
                "properties": {
                    "full_uri": {"type": "string", "format": "uri"},
                    "ref_uri": {"type": "string", "format": "uri-reference"},
                },
            }
        )

    def test_datetime_valid(self, datetime_format):
        validator = TypeAdapter(datetime_format)
        result = validator.validate_python("2024-01-17T12:34:56Z")
        assert isinstance(result, datetime)

    def test_datetime_invalid(self, datetime_format):
        validator = TypeAdapter(datetime_format)
        with pytest.raises(ValidationError):
            validator.validate_python("not-a-date")

    def test_email_valid(self, email_format):
        validator = TypeAdapter(email_format)
        result = validator.validate_python("test@example.com")
        assert isinstance(result, str)

    def test_email_invalid(self, email_format):
        validator = TypeAdapter(email_format)
        with pytest.raises(ValidationError):
            validator.validate_python("not-an-email")

    def test_uri_valid(self, uri_format):
        validator = TypeAdapter(uri_format)
        result = validator.validate_python("https://example.com")
        assert isinstance(result, AnyUrl)

    def test_uri_invalid(self, uri_format):
        validator = TypeAdapter(uri_format)
        with pytest.raises(ValidationError):
            validator.validate_python("not-a-uri")

    def test_uri_reference_valid(self, uri_reference_format):
        validator = TypeAdapter(uri_reference_format)
        result = validator.validate_python("https://example.com")
        assert isinstance(result, str)

    def test_uri_reference_relative_valid(self, uri_reference_format):
        validator = TypeAdapter(uri_reference_format)
        result = validator.validate_python("/path/to/resource")
        assert isinstance(result, str)

    def test_uri_reference_invalid(self, uri_reference_format):
        validator = TypeAdapter(uri_reference_format)
        result = validator.validate_python("not a uri")
        assert isinstance(result, str)

    def test_json_valid(self, json_format):
        validator = TypeAdapter(json_format)
        result = validator.validate_python('{"key": "value"}')
        assert isinstance(result, dict)

    def test_json_invalid(self, json_format):
        validator = TypeAdapter(json_format)
        with pytest.raises(ValidationError):
            validator.validate_python("{invalid json}")

    def test_mixed_formats_object(self, mixed_formats_object):
        validator = TypeAdapter(mixed_formats_object)
        result = validator.validate_python(
            {"full_uri": "https://example.com", "ref_uri": "/path/to/resource"}
        )
        assert isinstance(result.full_uri, AnyUrl)
        assert isinstance(result.ref_uri, str)


class TestCircularReferences:
    """Test suite for circular reference handling."""

    @pytest.fixture
    def self_referential(self):
        return jsonschema_to_type(
            {
                "type": "object",
                "properties": {"name": {"type": "string"}, "child": {"$ref": "#"}},
            }
        )

    @pytest.fixture
    def mutually_recursive(self):
        return jsonschema_to_type(
            {
                "type": "object",
                "definitions": {
                    "Person": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "friend": {"$ref": "#/definitions/Pet"},
                        },
                    },
                    "Pet": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "owner": {"$ref": "#/definitions/Person"},
                        },
                    },
                },
                "properties": {"person": {"$ref": "#/definitions/Person"}},
            }
        )

    def test_self_ref_single_level(self, self_referential):
        validator = TypeAdapter(self_referential)
        result = validator.validate_python(
            {"name": "parent", "child": {"name": "child"}}
        )
        assert result.name == "parent"
        assert result.child.name == "child"
        assert result.child.child is None

    def test_self_ref_multiple_levels(self, self_referential):
        validator = TypeAdapter(self_referential)
        result = validator.validate_python(
            {
                "name": "grandparent",
                "child": {"name": "parent", "child": {"name": "child"}},
            }
        )
        assert result.name == "grandparent"
        assert result.child.name == "parent"
        assert result.child.child.name == "child"

    def test_mutual_recursion_single_level(self, mutually_recursive):
        validator = TypeAdapter(mutually_recursive)
        result = validator.validate_python(
            {"person": {"name": "Alice", "friend": {"name": "Spot"}}}
        )
        assert result.person.name == "Alice"
        assert result.person.friend.name == "Spot"
        assert result.person.friend.owner is None

    def test_mutual_recursion_multiple_levels(self, mutually_recursive):
        validator = TypeAdapter(mutually_recursive)
        result = validator.validate_python(
            {
                "person": {
                    "name": "Alice",
                    "friend": {"name": "Spot", "owner": {"name": "Bob"}},
                }
            }
        )
        assert result.person.name == "Alice"
        assert result.person.friend.name == "Spot"
        assert result.person.friend.owner.name == "Bob"


class TestIdentifierNormalization:
    """Test suite for handling non-standard property names."""

    @pytest.fixture
    def special_chars(self):
        return jsonschema_to_type(
            {
                "type": "object",
                "properties": {
                    "@type": {"type": "string"},
                    "first-name": {"type": "string"},
                    "last.name": {"type": "string"},
                    "2nd_address": {"type": "string"},
                    "$ref": {"type": "string"},
                },
            }
        )

    def test_normalizes_special_chars(self, special_chars):
        validator = TypeAdapter(special_chars)
        result = validator.validate_python(
            {
                "@type": "person",
                "first-name": "Alice",
                "last.name": "Smith",
                "2nd_address": "456 Oak St",
                "$ref": "12345",
            }
        )
        assert result.field_type == "person"  # @type -> field_type
        assert result.first_name == "Alice"  # first-name -> first_name
        assert result.last_name == "Smith"  # last.name -> last_name
        assert (
            result.field_2nd_address == "456 Oak St"
        )  # 2nd_address -> field_2nd_address
        assert result.field_ref == "12345"  # $ref -> field_ref


class TestConstantValues:
    """Test suite for constant value validation."""

    @pytest.fixture
    def string_const(self):
        return jsonschema_to_type({"type": "string", "const": "production"})

    @pytest.fixture
    def number_const(self):
        return jsonschema_to_type({"type": "number", "const": 42.5})

    @pytest.fixture
    def boolean_const(self):
        return jsonschema_to_type({"type": "boolean", "const": True})

    @pytest.fixture
    def null_const(self):
        return jsonschema_to_type({"type": "null", "const": None})

    @pytest.fixture
    def object_with_consts(self):
        return jsonschema_to_type(
            {
                "type": "object",
                "properties": {
                    "env": {"const": "production"},
                    "version": {"const": 1},
                    "enabled": {"const": True},
                },
            }
        )

    def test_string_const_valid(self, string_const):
        validator = TypeAdapter(string_const)
        assert validator.validate_python("production") == "production"

    def test_string_const_invalid(self, string_const):
        validator = TypeAdapter(string_const)
        with pytest.raises(ValidationError):
            validator.validate_python("development")

    def test_number_const_valid(self, number_const):
        validator = TypeAdapter(number_const)
        assert validator.validate_python(42.5) == 42.5

    def test_number_const_invalid(self, number_const):
        validator = TypeAdapter(number_const)
        with pytest.raises(ValidationError):
            validator.validate_python(42)

    def test_boolean_const_valid(self, boolean_const):
        validator = TypeAdapter(boolean_const)
        assert validator.validate_python(True) is True

    def test_boolean_const_invalid(self, boolean_const):
        validator = TypeAdapter(boolean_const)
        with pytest.raises(ValidationError):
            validator.validate_python(False)

    def test_null_const_valid(self, null_const):
        validator = TypeAdapter(null_const)
        assert validator.validate_python(None) is None

    def test_null_const_invalid(self, null_const):
        validator = TypeAdapter(null_const)
        with pytest.raises(ValidationError):
            validator.validate_python(False)

    def test_object_consts_valid(self, object_with_consts):
        validator = TypeAdapter(object_with_consts)
        result = validator.validate_python(
            {"env": "production", "version": 1, "enabled": True}
        )
        assert result.env == "production"
        assert result.version == 1
        assert result.enabled is True

    def test_object_consts_invalid(self, object_with_consts):
        validator = TypeAdapter(object_with_consts)
        with pytest.raises(ValidationError):
            validator.validate_python(
                {
                    "env": "production",
                    "version": 2,  # Wrong constant
                    "enabled": True,
                }
            )


class TestSchemaCaching:
    """Test suite for schema caching behavior."""

    def test_identical_schemas_reuse_class(self):
        schema = {"type": "object", "properties": {"name": {"type": "string"}}}

        class1 = jsonschema_to_type(schema)
        class2 = jsonschema_to_type(schema)
        assert class1 is class2

    def test_different_names_different_classes(self):
        schema = {"type": "object", "properties": {"name": {"type": "string"}}}

        class1 = jsonschema_to_type(schema, name="Class1")
        class2 = jsonschema_to_type(schema, name="Class2")
        assert class1 is not class2
        assert class1.__name__ == "Class1"
        assert class2.__name__ == "Class2"

    def test_nested_schema_caching(self):
        schema = {
            "type": "object",
            "properties": {
                "nested": {"type": "object", "properties": {"name": {"type": "string"}}}
            },
        }

        class1 = jsonschema_to_type(schema)
        class2 = jsonschema_to_type(schema)

        # Both main classes and their nested classes should be identical
        assert class1 is class2
        assert (
            class1.__dataclass_fields__["nested"].type
            is class2.__dataclass_fields__["nested"].type
        )


class TestSchemaHashing:
    """Test suite for schema hashing utility."""

    def test_deterministic_hash(self):
        schema = {"type": "object", "properties": {"name": {"type": "string"}}}
        hash1 = hash_schema(schema)
        hash2 = hash_schema(schema)
        assert hash1 == hash2
        assert isinstance(hash1, str)
        assert len(hash1) == 64  # SHA-256 hash length

    def test_different_schemas_different_hashes(self):
        schema1 = {"type": "object", "properties": {"name": {"type": "string"}}}
        schema2 = {"type": "object", "properties": {"age": {"type": "integer"}}}
        assert hash_schema(schema1) != hash_schema(schema2)

    def test_order_independent_hash(self):
        schema1 = {"properties": {"name": {"type": "string"}}, "type": "object"}
        schema2 = {"type": "object", "properties": {"name": {"type": "string"}}}
        assert hash_schema(schema1) == hash_schema(schema2)

    def test_nested_schema_hash(self):
        schema = {
            "type": "object",
            "properties": {
                "nested": {"type": "object", "properties": {"name": {"type": "string"}}}
            },
        }
        hash1 = hash_schema(schema)
        assert isinstance(hash1, str)
        assert len(hash1) == 64


class TestDefaultMerging:
    """Test suite for default value merging behavior."""

    def test_simple_merge(self):
        defaults = {"name": "anonymous", "age": 0}
        data = {"name": "test"}
        result = merge_defaults(data, {"properties": {}}, defaults)
        assert result["name"] == "test"
        assert result["age"] == 0

    def test_nested_merge(self):
        defaults = {"user": {"name": "anonymous", "settings": {"theme": "light"}}}
        data = {"user": {"name": "test"}}
        result = merge_defaults(data, {"properties": {}}, defaults)
        assert result["user"]["name"] == "test"
        assert result["user"]["settings"]["theme"] == "light"

    def test_array_merge(self):
        defaults = {
            "items": [
                {"name": "item1", "done": False},
                {"name": "item2", "done": False},
            ]
        }
        data = {"items": [{"name": "custom", "done": True}]}
        result = merge_defaults(data, {"properties": {}}, defaults)
        assert len(result["items"]) == 1
        assert result["items"][0]["name"] == "custom"
        assert result["items"][0]["done"] is True

    def test_empty_data_uses_defaults(self):
        schema = {
            "properties": {
                "user": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "default": "anonymous"},
                        "settings": {"type": "object", "default": {"theme": "light"}},
                    },
                    "default": {"name": "guest", "settings": {"theme": "dark"}},
                }
            }
        }
        result = merge_defaults({}, schema)
        assert result["user"]["name"] == "guest"
        assert result["user"]["settings"]["theme"] == "dark"

    def test_property_level_defaults(self):
        schema = {
            "properties": {
                "name": {"type": "string", "default": "anonymous"},
                "age": {"type": "integer", "default": 0},
            }
        }
        result = merge_defaults({}, schema)
        assert result["name"] == "anonymous"
        assert result["age"] == 0

    def test_nested_property_defaults(self):
        schema = {
            "properties": {
                "user": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "default": "anonymous"},
                        "settings": {
                            "type": "object",
                            "properties": {
                                "theme": {"type": "string", "default": "light"}
                            },
                        },
                    },
                }
            }
        }
        result = merge_defaults({"user": {"settings": {}}}, schema)
        assert result["user"]["name"] == "anonymous"
        assert result["user"]["settings"]["theme"] == "light"

    def test_default_priority(self):
        schema = {
            "properties": {
                "settings": {
                    "type": "object",
                    "properties": {"theme": {"type": "string", "default": "light"}},
                    "default": {"theme": "dark"},
                }
            },
            "default": {"settings": {"theme": "system"}},
        }

        # Test priority: data > parent default > object default > property default
        result1 = merge_defaults({}, schema)  # Uses schema default
        assert result1["settings"]["theme"] == "system"

        result2 = merge_defaults({"settings": {}}, schema)  # Uses object default
        assert result2["settings"]["theme"] == "dark"

        result3 = merge_defaults(
            {"settings": {"theme": "custom"}}, schema
        )  # Uses provided data
        assert result3["settings"]["theme"] == "custom"


class TestEdgeCases:
    """Test suite for edge cases and corner scenarios."""

    def test_empty_schema(self):
        schema = {}
        result = jsonschema_to_type(schema)
        assert result is object

    def test_schema_without_type(self):
        schema = {"properties": {"name": {"type": "string"}}}
        Type = jsonschema_to_type(schema)
        validator = TypeAdapter(Type)
        result = validator.validate_python({"name": "test"})
        assert result.name == "test"

    def test_recursive_defaults(self):
        schema = {
            "type": "object",
            "properties": {
                "node": {
                    "type": "object",
                    "properties": {"value": {"type": "string"}, "next": {"$ref": "#"}},
                    "default": {"value": "default", "next": None},
                }
            },
        }
        Type = jsonschema_to_type(schema)
        validator = TypeAdapter(Type)
        result = validator.validate_python({})
        assert result.node.value == "default"
        assert result.node.next is None

    def test_mixed_type_array(self):
        schema = {
            "type": "array",
            "items": [{"type": "string"}, {"type": "number"}, {"type": "boolean"}],
        }
        Type = jsonschema_to_type(schema)
        validator = TypeAdapter(Type)
        result = validator.validate_python(["test", 123, True])
        assert result == ["test", 123, True]


class TestNameHandling:
    """Test suite for schema name handling."""

    def test_name_from_title(self):
        schema = {
            "type": "object",
            "title": "Person",
            "properties": {"name": {"type": "string"}},
        }
        Type = jsonschema_to_type(schema)
        assert Type.__name__ == "Person"

    def test_explicit_name_overrides_title(self):
        schema = {
            "type": "object",
            "title": "Person",
            "properties": {"name": {"type": "string"}},
        }
        Type = jsonschema_to_type(schema, name="CustomPerson")
        assert Type.__name__ == "CustomPerson"

    def test_default_name_without_title(self):
        schema = {"type": "object", "properties": {"name": {"type": "string"}}}
        Type = jsonschema_to_type(schema)
        assert Type.__name__ == "Root"

    def test_name_only_allowed_for_objects(self):
        schema = {"type": "string"}
        with pytest.raises(ValueError, match="Can not apply name to non-object schema"):
            jsonschema_to_type(schema, name="StringType")

    def test_nested_object_names(self):
        schema = {
            "type": "object",
            "title": "Parent",
            "properties": {
                "child": {
                    "type": "object",
                    "title": "Child",
                    "properties": {"name": {"type": "string"}},
                }
            },
        }
        Type = jsonschema_to_type(schema)
        assert Type.__name__ == "Parent"
        assert Type.__dataclass_fields__["child"].type.__origin__ is Union
        assert Type.__dataclass_fields__["child"].type.__args__[0].__name__ == "Child"
        assert Type.__dataclass_fields__["child"].type.__args__[1] is type(None)

    def test_recursive_schema_naming(self):
        schema = {
            "type": "object",
            "title": "Node",
            "properties": {"next": {"$ref": "#"}},
        }
        Type = jsonschema_to_type(schema)
        assert Type.__name__ == "Node"
        assert Type.__dataclass_fields__["next"].type.__origin__ is Union
        assert (
            Type.__dataclass_fields__["next"].type.__args__[0].__forward_arg__ == "Node"
        )
        assert Type.__dataclass_fields__["next"].type.__args__[1] is type(None)

    def test_name_caching_with_different_titles(self):
        """Ensure schemas with different titles create different cached classes"""
        schema1 = {
            "type": "object",
            "title": "Type1",
            "properties": {"name": {"type": "string"}},
        }
        schema2 = {
            "type": "object",
            "title": "Type2",
            "properties": {"name": {"type": "string"}},
        }
        Type1 = jsonschema_to_type(schema1)
        Type2 = jsonschema_to_type(schema2)
        assert Type1 is not Type2
        assert Type1.__name__ == "Type1"
        assert Type2.__name__ == "Type2"

    def test_recursive_schema_with_invalid_python_name(self):
        """Test that recursive schemas work with titles that aren't valid Python identifiers"""
        schema = {
            "type": "object",
            "title": "My Complex Type!",
            "properties": {"name": {"type": "string"}, "child": {"$ref": "#"}},
        }
        Type = jsonschema_to_type(schema)
        # The class should get a sanitized name
        assert Type.__name__ == "My_Complex_Type"
        # Create an instance to verify the recursive reference works
        validator = TypeAdapter(Type)
        result = validator.validate_python(
            {"name": "parent", "child": {"name": "child", "child": None}}
        )
        assert result.name == "parent"
        assert result.child.name == "child"
        assert result.child.child is None
