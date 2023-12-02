from pages import page_2

def test_layout():
    layout = page_2.layout()
    assert isinstance(layout, page_2.html.Div)