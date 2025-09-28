import pytest
import pygame as pg
from pygame_ui_items.button import Button, RedButton, BlueButton, GreenButton, YellowButton

@pytest.fixture(autouse=True)
def pygame_setup():
    pg.init()
    pg.font.init()
    screen = pg.display.set_mode((200, 200))
    yield screen
    pg.quit()

def test_button_initialization():
    btn = Button(10, 20, 100, 40, text="Click Me")
    assert btn._text == "Click Me"
    assert btn._state == "normal"
    assert btn._hovered is False
    assert btn._pressed is False

def test_button_click_triggers_callback():
    clicked = {"value": False}
    def on_click():
        clicked["value"] = True
    
    btn = Button(10, 20, 100, 40, text="Click", onclick=on_click)
    btn._hovered = True
    
    down_event = pg.event.Event(pg.MOUSEBUTTONDOWN, {"button": 1, "pos": (15, 25)})
    up_event = pg.event.Event(pg.MOUSEBUTTONUP, {"button": 1, "pos": (15, 25)})

    btn.handle_event(down_event)
    btn.handle_event(up_event)

    assert clicked["value"] is True

@pytest.mark.parametrize("cls", [RedButton, BlueButton, GreenButton, YellowButton])
def test_colored_buttons_have_expected_styles(cls):
    btn = cls(0, 0, 100, 40, text="Test")
    styles = btn._get_default_styles()
    assert "bg_color" in styles
    assert "hover_bg_color" in styles
    assert "pressed_bg_color" in styles
