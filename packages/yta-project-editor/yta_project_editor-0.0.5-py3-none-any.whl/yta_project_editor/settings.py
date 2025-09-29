from yta_constants.video import Resolution
from dataclasses import dataclass


@dataclass
class Settings:
    """
    Class to wrap the settings.
    """

    MAX_TIMELINE_TRACK_DURATION: int = 1200
    """
    The maximum duration, in seconds, that a
    timeline track can have according to all
    the subclips on it. This value can change
    to allow longer timeline tracks.
    """
    TRACKS_INDEXES_LIMIT: tuple[int, int] = (0, 9)
    """
    The limit of the tracks indexes we have, starting
    from 0, so only the upper limit + 1 tracks are
    available in the edition system.
    """
    MINIMUM_FPS: int = 5
    """
    The lower frames per second the project can have.
    """
    MAXIMUM_FPS: int = 120
    """
    The greater frames per second the project can have.
    """
    MINIMUM_DIMENSIONS: tuple[int, int] = Resolution.SD_480.value
    """
    The lower dimension the project can have.
    """
    MAXIMUM_DIMENSIONS: tuple[int, int] = Resolution.FULLHD_1080.value
    """
    The greater dimension the project can have.
    """
    DEFAULT_DIMENSIONS: tuple[int, int] = Resolution.FULLHD_1080.value
    """
    The dimension that a project should have by default.
    """




