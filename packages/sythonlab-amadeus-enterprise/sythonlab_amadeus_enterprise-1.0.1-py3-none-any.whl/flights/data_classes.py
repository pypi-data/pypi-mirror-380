from dataclasses import dataclass

from enum import Enum


class AvailabilityPaxCategory(Enum):
    ADULT = 'ADULT'
    CHILD = 'CHILD'
    INFANT = 'INFANT'


@dataclass
class AvailabilityItinerary:
    ref: int
    departing_from: str
    arriving_to: str
    date: str


@dataclass
class AvailabilityPassenger:
    type: AvailabilityPaxCategory
