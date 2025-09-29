from typing import Any
from spx_sdk.registry import register_class
from spx_sdk.actions.action import Action
from spx_sdk.validation.decorators import definition_schema


@register_class(name="function")
@definition_schema({
    "type": "object",
    "required": ["function", "call"],
    "properties": {
        "function": {
            "oneOf": [
                {"type": "string", "pattern": r"^(\$in|\$out|\$attr|\$ext)\([^)]+\)$"},
                {"type": "array", "minItems": 1, "items": {"type": "string", "pattern": r"^(\$in|\$out|\$attr|\$ext)\([^)]+\)$"}}
            ],
            "description": "Target attribute(s): single ref or list of refs to attributes using $in/$out/$attr/$ext."
        },
        "call": {
            "type": "string",
            "minLength": 1,
            "description": "Expression string, may reference inputs via $in(...) and other helpers."
        },
    }
}, validation_scope="parent")
class FunctionAction(Action):
    """
    FunctionAction class for executing a function.
    Inherits from Action to manage action components.
    """

    def _populate(self, definition: dict) -> None:
        self.call = None
        super()._populate(definition)

    def run(self, *args, **kwargs) -> Any:
        """
        Evaluate the call expression, resolving attribute references,
        and write the result to all output attributes.
        """
        super().run()
        if self.call is None:
            return False  # No call defined, nothing to run
        return self.write_outputs(self.call)
