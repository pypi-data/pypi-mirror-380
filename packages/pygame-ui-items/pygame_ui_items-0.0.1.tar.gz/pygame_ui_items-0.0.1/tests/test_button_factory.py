import pytest
import pygame as pg
from pygame_ui_items import button_factory
from pygame_ui_items.button import Button, RedButton, BlueButton, GreenButton, YellowButton

@pytest.fixture(autouse=True)
def pygame_setup():
    pg.init()
    pg.font.init()
    screen = pg.display.set_mode((200, 200))
    yield screen
    pg.quit()

def test_button_red_factory_creates_redbutton():
    btn = button_factory.button_red("Play")
    assert isinstance(btn, RedButton)
    assert btn._text == "Play"

def test_button_blue_factory_creates_bluebutton():
    btn = button_factory.button_blue("Play")
    assert isinstance(btn, BlueButton)
    assert btn._text == "Play"

def test_button_green_factory_creates_greenbutton():
    btn = button_factory.button_green("Play")
    assert isinstance(btn, GreenButton)
    assert btn._text == "Play"

def test_button_yellow_factory_creates_yellowbutton():
    btn = button_factory.button_yellow("Play")
    assert isinstance(btn, YellowButton)
    assert btn._text == "Play"

def test_create_button_factory_creates_base_button():
    btn = button_factory.create_button("Play")
    assert isinstance(btn, Button)
    assert btn._text == "Play"
