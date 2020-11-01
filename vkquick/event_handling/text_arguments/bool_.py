"""
Bool аргумент
"""
import re
import typing as ty

from vkquick.base import text_argument


class Bool(text_argument.TextArgument):
    """
    Аргумент с двумя возможными значениям -- True и False
    """

    def __init__(
        self,
        *,
        true_extension: ty.Iterable[str] = (),
        false_extension: ty.Iterable[str] = (),
    ):
        """
        * `true_extension`: Дополнительные алиасы на True-значения
        * `false_extension`: Дополнительные алиасы на False-значения
        """
        true_values = [
            "true",
            "1",
            "yes",
            "y",
            "да",
            "д",
            "истина",
            r"\+",
            "правда",
            "t",
            "on",
            "вкл",
            "enable",
        ]
        false_values = [
            "false",
            "0",
            "no",
            "n",
            "нет",
            "н",
            "ложь",
            "-",
            "неправда",
            "f",
            "off",
            "выкл",
            "disable",
        ]
        true_values.extend(true_extension)
        false_values.extend(false_extension)

        self.true_regex = re.compile(
            f"(?:{'|'.join(true_values)})", re.IGNORECASE
        )
        self.false_regex = re.compile(
            f"(?:{'|'.join(false_values)})", re.IGNORECASE
        )

    def cut_part(self, arguments_string: str) -> ty.Tuple[ty.Any, str]:
        value, parsed_string = self.cut_part_lite(
            self.true_regex, arguments_string
        )

        if value is not text_argument.UnmatchedArgument:
            return True, parsed_string

        value, parsed_string = self.cut_part_lite(
            self.false_regex, arguments_string
        )

        if value is not text_argument.UnmatchedArgument:
            return False, parsed_string

        return text_argument.UnmatchedArgument, parsed_string

    def usage_description(self):
        return "Todo"  # TODO
