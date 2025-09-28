from enum import Enum
from typing import Optional, Literal, Union, Annotated, List

from pydantic import BaseModel, Field, TypeAdapter


class Input(BaseModel):
    name: str= Field(..., description="Name of the input field")

class TextInput(Input):
    type: Literal["text"] = "text"
    placeholder: Optional[str] = Field(None, description="Placeholder text for the input field")

class FileInput(Input):
    type: Literal["file"] = "file"


class StatusIcon:
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"


class StatusUpdate(BaseModel):
    type: Literal["status_update"] = "status_update"
    id: Optional[str] = None
    icon: Literal["info", "warning", "error"]
    text: str


class Feedback(BaseModel):
    name: str = Field(..., description="Name of the feedback option")
    allow_multiple: bool = Field(
        default = False, description="Whether multiple options can be selected for multi-select feedback"
    )

class OptionFeedback(Feedback):
    type: Literal["select"] = "select"
    options: list[str] = Field(..., description="List of options for select or multi-select feedback")
    
class ThumbsFeedback(Feedback):
    type: Literal["thumbs"] = "thumbs"
    options: List[Literal["thumbs_up", "thumbs_down"]] = Field(
        default=["thumbs_up", "thumbs_down"],
        description="Options for thumbs feedback, typically 'thumbs_up' and 'thumbs_down'"
    )

class TextFeedback(Feedback):
    type: Literal["text"] = "text"


class BaseMessage(BaseModel):
    id: Optional[str] = None
    feedback: Optional[Union[OptionFeedback, TextFeedback]] = None


class MarkdownMessage(BaseMessage):
    type: Literal["markdown"] = "markdown"
    content: str
    feedback: Optional[List[Union[OptionFeedback, TextFeedback, ThumbsFeedback]]] = None

UserHandlerResponse = TypeAdapter(Annotated[MarkdownMessage | StatusUpdate, Field(discriminator="type")])


# print(OptionFeedback(
#     name="Your thoughts",
#     options=['a', 'b'],
#     allow_multiple=True
# ).model_dump())
# yield StatusUpdate(icon=StatusIcon.INFO, text="Processing your request...")
# yield MarkdownMessage(content="Hello, world!", id=1, feedback=[Feedback(spec=MyFeedbackSpec)])
