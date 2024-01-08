import os

import streamlit.testing.v1 as sat




def test_planets():
    app = sat.AppTest.from_file("../../src/pew.py")
    app.run(timeout=60)
    ci = app.chat_input("chat_input").set_value('Name the planets of the solar system').run(timeout=60)
    cms = app.get("chat_message")
    assert  len(cms) == 3
    planets = cms[2].children[0].body
    for planet in 'Mercury,Venus,Earth,Mars,Jupiter,Saturn,Uranus,Neptune'.split(','):
        assert planet in planets
    assert not app.exception

