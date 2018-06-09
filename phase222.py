from jinja2 import Template
index_html = open("index.html").read()

template_html = open("base.html")
template = Template(template_html)
template.render(
    title="Bio"
    content=index_html,
)
