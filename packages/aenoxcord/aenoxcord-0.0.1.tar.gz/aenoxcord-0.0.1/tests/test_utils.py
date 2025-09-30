import pytest

import aenoxcord
from aenoxcord.internal.dc import FakeDiscord, commands, discord


def test_big_numbers():
    assert aenoxcord.format_number(0) == "0"
    assert aenoxcord.format_number(1) == "1"
    assert aenoxcord.format_number(10) == "10"
    assert aenoxcord.format_number(100) == "0.1K"
    assert aenoxcord.format_number(1_000) == "1K"
    assert aenoxcord.format_number(1_000_000) == "1M"
    assert aenoxcord.format_number(1_100_000) == "1.1M"
    assert aenoxcord.format_number(1_000_000_000) == "1B"

    # negative
    assert aenoxcord.format_number(-1) == "-1"
    assert aenoxcord.format_number(-100) == "-0.1K"
    assert aenoxcord.format_number(-1_000) == "-1K"
    assert aenoxcord.format_number(-1_000_000) == "-1M"
    assert aenoxcord.format_number(-1_100_000) == "-1.1M"
    assert aenoxcord.format_number(-1_000_000_000) == "-1B"

    # decimals and trailing zeros
    assert aenoxcord.format_number(1_550, decimal_places=2) == "1.55K"
    assert aenoxcord.format_number(1_550, decimal_places=3) == "1.55K"
    assert aenoxcord.format_number(1_550, decimal_places=3, trailing_zero=True) == "1.550K"
    assert aenoxcord.format_number(1_000, trailing_zero=True) == "1.0K"
    assert aenoxcord.format_number(1_000, decimal_places=2, trailing_zero=True) == "1.00K"


def test_convert_color():
    if isinstance(discord.lib, FakeDiscord):
        return

    assert str(aenoxcord.convert_color("red")) == "#e74c3c"
    assert str(aenoxcord.convert_color("dark red")) == "#992d22"
    assert str(aenoxcord.convert_color("black")) == "#000000"
    assert str(aenoxcord.convert_color("rgb(255, 255, 255)")) == "#ffffff"

    # test hex params
    assert str(aenoxcord.convert_color("ffffff")) == "#ffffff"
    assert str(aenoxcord.convert_color("#ffffff")) == "#ffffff"

    with pytest.raises(commands.BadColorArgument):
        assert str(aenoxcord.convert_color("#fff", strict_hex=True)) == "#ffffff"

    with pytest.raises(commands.BadColorArgument):
        aenoxcord.convert_color("ffffff", hex_hash=True)
