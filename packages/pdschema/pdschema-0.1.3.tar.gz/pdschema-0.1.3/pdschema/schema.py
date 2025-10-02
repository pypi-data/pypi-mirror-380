from datetime import datetime
from typing import ClassVar, Optional

import pandas as pd

from pdschema.columns import Column


class SchemaMeta(type):
    """Metaclass for Schema to collect declared Column fields."""

    def __new__(cls, name, bases, dct):
        # Collect Column instances declared in the class body
        columns = {key: value for key, value in dct.items() if isinstance(value, Column)}
        # Remove the Column instances from the class dictionary
        for key in columns:
            dct.pop(key)
        # Add the collected columns as a class attribute
        dct["_declared_columns"] = columns
        return super().__new__(cls, name, bases, dct)


class Schema(metaclass=SchemaMeta):
    _declared_columns: ClassVar[dict[str, Column]] = {}

    def __init__(self, columns: Optional[list[Column]] = None):
        if not columns and not self._declared_columns:
            # Default to an empty schema if no columns are provided
            self.columns = {}
        elif columns:
            self.columns = {col.name: col for col in columns}
        else:
            self.columns = {
                col_name: col_obj.with_name(col_name) for col_name, col_obj in self._declared_columns.items()
            }

    def __repr__(self) -> str:
        """Return a string representation of the Schema.

        Returns:
            str: A formatted string showing the schema's columns and their properties
        """
        lines = ["Schema("]
        for col in self.columns.values():
            nullable_str = "nullable=True" if col.nullable else "nullable=False"
            validators_str = f", validators={col.validators}" if col.validators else ""
            dtype_str = col.dtype.__name__ if isinstance(col.dtype, type) else col.dtype
            lines.append(f"    Column(name='{col.name}', dtype={dtype_str}, {nullable_str}{validators_str})")
        lines.append(")")
        return "\n".join(lines)

    def validate(self, df: pd.DataFrame) -> bool:
        errors = []

        for col_name, col in self.columns.items():
            if not col_name:
                raise ValueError("Column name cannot be None")

            # Call the check_missing method of the Column class
            if missing := col.check_missing(df):
                errors.append(missing)
                continue

            series = df[col_name]

            # Call the check_nullability method of the Column class
            if nullability := col.check_nullability(series):
                errors.append(nullability)

            # Call the check_type method of the Column class
            if type_error := col.check_type(series):
                errors.append(type_error)

            errors.extend(col.validate(series))

        if errors:
            raise ValueError("Schema validation failed:\n" + "\n".join(errors))

        return True

    @staticmethod
    def _infer_column_type(series: pd.Series) -> type:
        """Infer the Python type for a pandas Series."""
        if series.empty:
            return object

        type_checks = [
            (pd.api.types.is_integer_dtype, int),
            (pd.api.types.is_float_dtype, float),
            (pd.api.types.is_bool_dtype, bool),
            (pd.api.types.is_string_dtype, str),
            (pd.api.types.is_datetime64_dtype, datetime),
            (lambda dtype: hasattr(dtype, "categories"), str),
            (lambda series: series.apply(lambda x: isinstance(x, dict)).any(), dict),
        ]

        for check, inferred_type in type_checks:
            if callable(check) and check(series):
                return inferred_type

        # For unknown types, try to infer from the first non-null value
        sample = None if series.empty else series.dropna().iloc[0]
        return type(sample) if sample is not None else object

    @staticmethod
    def infer_schema(df: pd.DataFrame) -> "Schema":
        """Infer a Schema from a pandas DataFrame.

        This method analyzes the DataFrame's columns and their data to create
        an appropriate Schema with inferred column definitions.

        Args:
            df: The pandas DataFrame to infer the schema from

        Returns:
            Schema: A new Schema instance with inferred column definitions
        """
        columns = [
            Column(
                name=col_name,
                dtype=Schema._infer_column_type(df[col_name]),
                nullable=bool(df[col_name].isnull().any()),
            )
            for col_name in df.columns
        ]
        return Schema(columns)
