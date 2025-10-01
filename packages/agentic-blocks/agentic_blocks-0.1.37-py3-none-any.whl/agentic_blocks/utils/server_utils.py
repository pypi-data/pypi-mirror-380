"""
Server utilities for handling web requests and responses.
"""

from agentic_blocks.models import UIMessage


def extract_message_content(ui_msg: UIMessage) -> str:
    """Extract text content from UI message."""
    if ui_msg.parts:
        text_parts = [part.text for part in ui_msg.parts if part.type == "text" and part.text]
        content = " ".join(text_parts)
    elif ui_msg.content:
        content = ui_msg.content
    else:
        content = "[Empty message]"

    # Add file information if present
    if ui_msg.files:
        file_info = ", ".join([f.name for f in ui_msg.files])
        content += f" [Files: {file_info}]"

    return content