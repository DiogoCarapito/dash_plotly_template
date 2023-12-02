from pages import page_1

def test_layout():
    layout = page_1.layout()
    assert isinstance(layout, page_1.html.Div)