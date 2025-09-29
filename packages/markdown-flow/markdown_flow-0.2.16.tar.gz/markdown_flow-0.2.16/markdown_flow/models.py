"""
Markdown-Flow Data Model Definitions

Simplified and refactored data models focused on core functionality.
"""

from dataclasses import dataclass, field

from .enums import BlockType, InputType
from .utils import extract_variables_from_text


@dataclass
class UserInput:
    """
    Simplified user input data class.

    Attributes:
        content (dict[str, list[str]]): User input content as variable name to values mapping
        input_type (InputType): Input method, defaults to text input
        is_multi_select (bool): Whether this contains multi-select input, defaults to False
    """

    content: dict[str, list[str]]
    input_type: InputType = InputType.TEXT
    is_multi_select: bool = False


@dataclass
class InteractionValidationConfig:
    """
    Simplified interaction validation configuration.

    Attributes:
        validation_template (Optional[str]): Validation prompt template
        target_variable (Optional[str]): Target variable name
        enable_custom_validation (bool): Enable custom validation, defaults to True
    """

    validation_template: str | None = None
    target_variable: str | None = None
    enable_custom_validation: bool = True


@dataclass
class Block:
    """
    Simplified document block data class.

    Attributes:
        content (str): Block content
        block_type (Union[BlockType, str]): Block type
        index (int): Block index, defaults to 0
        variables (List[str]): List of variable names contained in the block
    """

    content: str
    block_type: BlockType | str
    index: int = 0
    variables: list[str] = field(default_factory=list)

    def __post_init__(self):
        """Post-initialization processing."""
        # Convert to BlockType enum
        if isinstance(self.block_type, str):
            # Efficient type mapping
            type_mapping = {
                "content": BlockType.CONTENT,
                "interaction": BlockType.INTERACTION,
                "preserved_content": BlockType.PRESERVED_CONTENT,
            }

            self.block_type = type_mapping.get(self.block_type, self._parse_block_type_fallback(self.block_type))

        # Auto-extract variables
        if not self.variables:
            self.variables = extract_variables_from_text(self.content)

    def _parse_block_type_fallback(self, block_type_str: str) -> BlockType:
        """Fallback logic for non-standard block_type strings."""
        try:
            return BlockType(block_type_str)
        except ValueError:
            return BlockType.CONTENT

    @property
    def is_interaction(self) -> bool:
        """Check if this is an interaction block."""
        return self.block_type == BlockType.INTERACTION

    @property
    def is_content(self) -> bool:
        """Check if this is a content block."""
        return self.block_type in [BlockType.CONTENT, BlockType.PRESERVED_CONTENT]
