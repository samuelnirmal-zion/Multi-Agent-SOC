from pathlib import Path


def render_frontend_page(result: str | None = None, submitted_log: str | None = None) -> str:
    template_path = Path(__file__).resolve().parent / "index.html"
    with template_path.open("r", encoding="utf-8") as file:
        html = file.read()

    result = result or ""
    submitted_log = submitted_log or ""

    start_marker = "{% if result %}"
    end_marker = "{% endif %}"
    if result:
        html = html.replace(start_marker, "")
        html = html.replace(end_marker, "")
    else:
        start = html.find(start_marker)
        end = html.find(end_marker, start)
        if start != -1 and end != -1:
            html = html[:start] + html[end + len(end_marker):]

    html = html.replace("{{ result }}", result)
    html = html.replace("{{ submitted_log }}", submitted_log)
    return html
