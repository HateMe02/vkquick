class SafeDict(dict):
    """ """
    def __missing__(self, key):
        return "{" + key + "}"


class Wrapper:
    """ """
    def __init__(self, fields: dict) -> None:
        self.__fields = fields

    def __format__(self, format_spec: str) -> str:
        format_spec = format_spec.replace(">", "}")
        format_spec = format_spec.replace("<", "{")
        extra_fields = self._extra_fields_to_format()
        format_fields = {**self.fields, **extra_fields}
        inserted_values = SafeDict(format_fields)
        return format_spec.format_map(inserted_values)

    @property
    def fields(self) -> dict:
        """ """
        return self.__fields

    def _extra_fields_to_format(self) -> dict:
        """ """
        return {}

    def __repr__(self) -> str:
        cls_name = self.__class__.__name__
        return f"{cls_name}({self.fields})"
