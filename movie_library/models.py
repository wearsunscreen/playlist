from dataclasses import dataclass, field
from datetime import datetime
import uuid
from typing import List

@dataclass
class Movie:
    title: str
    year: int
    director: str
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)
    cast: List[str] = field(default_factory=list)
    series: List[str] = field(default_factory=list)
    last_watched: datetime = None
    rating: int = 0
    tags: List[str] = field(default_factory=list)
    description: str = None
    video_link: str = None