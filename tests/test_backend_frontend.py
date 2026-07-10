from importlib import import_module


def test_backend_module_exposes_create_app():
    backend = import_module("backend")
    app = backend.create_app()
    assert app is not None


def test_frontend_module_exposes_page_renderer():
    frontend = import_module("frontend")
    html = frontend.render_frontend_page()
    assert isinstance(html, str)
    assert "Multi-Agent SOC" in html
