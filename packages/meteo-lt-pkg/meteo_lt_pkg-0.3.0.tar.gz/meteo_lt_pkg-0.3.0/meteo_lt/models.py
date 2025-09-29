"""Models script"""

from dataclasses import dataclass, field, fields
from datetime import datetime, timezone
from typing import List


@dataclass
class Coordinates:
    """Coordinates class"""

    latitude: float
    longitude: float


@dataclass
class Place:
    """Places"""

    code: str
    name: str
    administrative_division: str = field(
        metadata={"json_key": "administrativeDivision"}
    )
    country: str
    coordinates: Coordinates

    @property
    def latitude(self):
        """Latitude from coordinates"""
        return self.coordinates.latitude

    @property
    def longitude(self):
        """Longitude from coordinates"""
        return self.coordinates.longitude


@dataclass
class ForecastTimestamp:
    """ForecastTimestamp"""

    datetime: str = field(metadata={"json_key": "forecastTimeUtc"})
    temperature: float = field(metadata={"json_key": "airTemperature"})
    apparent_temperature: float = field(metadata={"json_key": "feelsLikeTemperature"})
    condition_code: str = field(metadata={"json_key": "conditionCode"})
    wind_speed: float = field(metadata={"json_key": "windSpeed"})
    wind_gust_speed: float = field(metadata={"json_key": "windGust"})
    wind_bearing: float = field(metadata={"json_key": "windDirection"})
    cloud_coverage: float = field(metadata={"json_key": "cloudCover"})
    pressure: float = field(metadata={"json_key": "seaLevelPressure"})
    humidity: float = field(metadata={"json_key": "relativeHumidity"})
    precipitation: float = field(metadata={"json_key": "totalPrecipitation"})


@dataclass
class Forecast:
    """Forecast"""

    place: Place
    forecast_created: str = field(metadata={"json_key": "forecastCreationTimeUtc"})
    current_conditions: ForecastTimestamp
    forecast_timestamps: List[ForecastTimestamp] = field(
        metadata={"json_key": "forecastTimestamps"}
    )

    def __post_init__(self):
        """Post-initialization processing."""

        current_hour = datetime.now(timezone.utc).replace(
            minute=0, second=0, microsecond=0
        )
        # Current conditions are equal to current hour record
        for forecast in self.forecast_timestamps:
            if (
                datetime.fromisoformat(forecast.datetime)
                .astimezone(timezone.utc)
                .replace(minute=0, second=0, microsecond=0)
            ) == current_hour:
                self.current_conditions = forecast
                break

        # Filter out timestamps that are older than current hour
        self.forecast_timestamps = [
            forecast
            for forecast in self.forecast_timestamps
            if (
                datetime.fromisoformat(forecast.datetime)
                .astimezone(timezone.utc)
                .replace(minute=0, second=0, microsecond=0)
            )
            > current_hour
        ]


def from_dict(cls, data: dict):
    """Utility function to convert a dictionary to a dataclass instance."""
    init_args = {}
    for f in fields(cls):
        if not f.init:
            continue  # Skip fields that are not part of the constructor

        json_key = f.metadata.get("json_key", f.name)
        value = data.get(json_key)

        # Recursively convert nested dataclasses
        if isinstance(value, dict) and hasattr(f.type, "from_dict"):
            value = from_dict(f.type, value)
        elif isinstance(value, list) and hasattr(f.type.__args__[0], "from_dict"):
            value = [from_dict(f.type.__args__[0], item) for item in value]
        elif f.name in ("datetime", "forecast_created"):
            # Convert datetime to ISO 8601 format
            dt = datetime.strptime(value, "%Y-%m-%d %H:%M:%S").replace(
                tzinfo=timezone.utc
            )
            value = dt.isoformat()

        init_args[f.name] = value
    return cls(**init_args)


Coordinates.from_dict = classmethod(from_dict)
Place.from_dict = classmethod(from_dict)
ForecastTimestamp.from_dict = classmethod(from_dict)
Forecast.from_dict = classmethod(from_dict)
