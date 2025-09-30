from .validator_base import FileValidatorBase
from .ids_validator import IdsValidator
from typing import Optional

def find_file_validator(name: str, options: dict) -> Optional[FileValidatorBase]:
    validators = {
        "ids_validator": IdsValidator,
    }
    if name not in validators:
        return [None, None]

    validator = validators[name]()
    validate_options = validator.configure(options)
    return validator, validate_options


__all__ = ["find_file_validator",]
