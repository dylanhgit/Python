class Television:
    """A class to represent a television set with capabilities to change channels, adjust volume, and mute."""

    MIN_VOLUME = 0  # Minimum volume level
    MAX_VOLUME = 2  # Maximum volume level
    MIN_CHANNEL = 0  # Minimum channel number
    MAX_CHANNEL = 3  # Maximum channel number

    def __init__(self) -> None:
        """Initialize the television with default settings."""
        self.__status = False  # TV is initially off
        self.__muted = False  # TV is initially not muted
        self.__volume = Television.MIN_VOLUME  # Set volume to minimum
        self.__channel = Television.MIN_CHANNEL  # Set channel to minimum
        self.__last_volume = 0  # Remember the last volume before mute

    def power(self) -> None:
        """Toggle the power status of the television."""
        self.__status = not self.__status

    def channel_up(self) -> None:
        """Increase the channel, wrapping around to MIN_CHANNEL after reaching MAX_CHANNEL."""
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decrease the channel, wrapping around to MAX_CHANNEL if below MIN_CHANNEL."""
        if self.__status:
            self.__channel = (self.__channel - 1) if self.__channel > 0 else Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """Increase the volume unless it is at MAX_VOLUME or the TV is muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__last_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume unless it is at MIN_VOLUME or the TV is muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__last_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def mute(self) -> None:
        """Toggle the mute status. Muting sets volume to 0, unmuting restores the previous volume level."""
        if self.__status:
            if not self.__muted:
                self.__last_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume = self.__last_volume
            self.__muted = not self.__muted

    def __str__(self) -> str:
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
