from typing import Iterator
from enum import Enum
from uuid import uuid4

from .base_annotation import _T, AnnotationObject


class InputTypeEnum(Enum):
    Select = "select"
    Multiselect = "multiple"
    Nest = "nested"
    Number = "number"
    Text = "text"
    MultiText = "multiple-text"


class Input(AnnotationObject):
    def __init__(self,
                 input_type,
                 value: _T = None,
                 required: bool = False,
                 default: _T = None,
                 name: str = None,
                 options=None,
                 **kwargs
                 ) -> None:
        """
        This structure defines that your input can only be a drop-down box or an input textarea box

        Args:
            kind:
                one type of [select, text, multiple selet]
            value:
                _T
            required:
                if necessary
            default:
                default value
            name:
                the name of the current select obj
            options:
                All choices allowed by value

        Returns:
            Input instance

        Examples:
            .. code-block:: python

                input = Input(input_type="select", value="rain")
                input.value

                output:
                >>> rain
        """
        assert input_type in [member.value for member in InputTypeEnum]
        self.input_type = input_type
        self.name = name
        self.required = required
        if options:
            assert isinstance(options, Iterator)
        self.value = value

        # Required but no default provided
        if required and not default:
            assert value
        # Normalize multiselect/nested values to list form
        if input_type in (InputTypeEnum.Multiselect.value,
                          InputTypeEnum.Nest.value) \
                and not isinstance(self.value, Iterator):
            self.value = [self.value, ]
        # Single-select paths fall through
        else:
            pass
            # assert isinstance(value, (str, int, float, bool))

        AnnotationObject.__init__(self, **kwargs)

    @staticmethod
    def gen_input(child, parent_id=None):
        """
        generate the input obj

        Args:
            child:
                subclass
            parent_id:
                superclass

        Returns:
            a Input instance
        """
        input_id = str(uuid4())
        parent_id = parent_id if parent_id else ""
        input_obj = Input(input_type=child['input']['type'].split("-")[0],
                          value=child['input'].get('value', None),
                          parent=parent_id,
                          name=child['label'],
                          team_id = child['input'].get('teamId', None),
                          id=input_id)
        return input_obj
