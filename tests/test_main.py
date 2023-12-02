import main


def test_app_title():
    assert main.app.title == "dash template"


def test_app_layout():
    assert isinstance(main.app.layout, main.html.Div)


def test_server():
    assert main.server is not None
