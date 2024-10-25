from typing import ClassVar, Dict, Literal, Optional

from pydantic import BaseModel


class WikipediaTool(BaseModel):
    config_id: ClassVar[str] = "wikipedia.WikipediaToolSpec"
    name: Literal["wikipedia"] = "wikipedia"
    tool_type: Literal["llamahub"] = "llamahub"
    label: Literal["Wikipedia"] = "Wikipedia"
    description: str = (
        "Use Wikipedia to gather more information about a topic from the query."
    )
    custom_prompt: Optional[str] = None
    config: Dict = {}
    enabled: bool = False
