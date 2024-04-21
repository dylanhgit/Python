import pytest
from television import Television

def test_initial_conditions():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0", "Initial state should be off, channel 0, volume 0"

def test_power_functionality():
    tv = Television()
    tv.power()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0", "TV should be on after toggling power"
    tv.power()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0", "TV should be off after toggling power again"

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert str(tv) == "Power = True, Channel = 1, Volume = 0", "Channel should increase by one"
    for _ in range(3):
        tv.channel_up()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0", "Channel should wrap around to 0"

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert str(tv) == f"Power = True, Channel = {Television.MAX_CHANNEL}, Volume = 0", "Channel should wrap to max channel"
    tv.channel_down()
    assert str(tv) == f"Power = True, Channel = {Television.MAX_CHANNEL - 1}, Volume = 0", "Channel should decrease by one"

def test_volume_up():
    tv = Television()
    tv.power()
    for _ in range(100):
        tv.volume_up()
    assert str(tv) == f"Power = True, Channel = 0, Volume = {Television.MAX_VOLUME}", "Volume should cap at max volume"

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    for _ in range(100):
        tv.volume_down()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0", "Volume should not decrease below min volume"

def test_mute_unmute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0", "Volume should be 0 when muted"
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1", "Volume should revert to previous setting when unmuted"
