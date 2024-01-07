import streamlit.testing.v1 as sat




def test_planets():
    app = sat.AppTest.from_file("/home/romilly/git/active/kew-pd/src/pew.py")
    app.run(timeout=60)
    ci = app.chat_input("chat_input").set_value('Name the planets of the solar system').run(timeout=60)
    cms = app.get("chat_message")
    assert  len(cms) == 3
    for cm in cms:
        print(cm.children[0].body)
    assert not app.exception

