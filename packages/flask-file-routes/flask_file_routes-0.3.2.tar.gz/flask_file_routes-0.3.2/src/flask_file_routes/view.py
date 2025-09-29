from flask import render_template, request, current_app, url_for, redirect, abort, g, render_template_string
from flask.views import http_method_funcs
from blinker import Namespace
import runpy
import os
import re
import markdown
import yaml
import inspect
from .ctx import page


_signals = Namespace()
before_page_module_execute = _signals.signal("before-page-module-execute")
before_page_module_render = _signals.signal("before-page-module-render")
after_page_module_render = _signals.signal("after-page-module-render")


class ModuleView:
    module_globals = dict(page=page, g=g, request=request, render_template=render_template,
                    url_for=url_for, redirect=redirect, abort=abort, app=current_app, current_app=current_app)
    
    @classmethod
    def create_from_module_template(cls, loader, module_name, template, url=None, skip_missing_frontmatter=False, endpoint=None):
        if template:
            template_code, python_code = loader.split_source(template)
            if template_code is None:
                template = None
        else:
            python_code = loader.split_source(loader.get_file_from_module(module_name))[1]

        if skip_missing_frontmatter and python_code is None:
            return None
        
        if python_code:
            m = re.match(r"#\s+methods\s*=\s*([a-z,\s]+)$", python_code, re.I)
            if m:
                methods = [me.strip().upper() for me in m.group(1).split(",")]
            else:
                methods = [m.upper() for m in http_method_funcs if re.search(rf"^(def\s+{m}\()|{m}\s*=", python_code, re.MULTILINE)]
            if not methods:
                methods = ["GET"]
        else:
            methods = ["GET"]
            module_name = None

        return cls(module_name, template, url=url, methods=methods, frontmatter=python_code, endpoint=endpoint)

    def __init__(self, module_name, template, url=None, methods=None, decorators=None, frontmatter=None, endpoint=None):
        if not methods:
            methods = ["GET"]
        self.module_name = module_name
        self.template = template
        self.url = url
        self.methods = methods
        self.decorators = decorators or []
        self.frontmatter = frontmatter
        self.endpoint = endpoint

    @property
    def is_markdown(self):
        return self.template and self.template.endswith(".md")

    def execute(self, view_args=None, method=None):
        if view_args is None:
            view_args = request.view_args
        if method is None:
            method = request.method.lower()
        page.template = self.template
        page.is_markdown = self.is_markdown

        before_page_module_execute.send(self)
        out = None
        if self.module_name:
            m = runpy.run_module(self.module_name, self.module_globals)
            if method in m and callable(m[method]):
                resp = m[method](**view_args)
                if resp:
                    out = resp
        elif self.frontmatter:
            page.template_ctx.update(yaml.safe_load(self.frontmatter))

        before_page_module_render.send(self)
        if out is None:
            if page.template:
                out = self._render()
            else:
                out = ""
        after_page_module_render.send(self)
        return out
    
    def _render(self):
        if page.get('is_markdown'):
            markdown_options = dict(current_app.config.get("PAGES_MARKDOWN_OPTIONS", {}), **page.get("markdown_options", {}))
            out = markdown.markdown(render_template(page.template), **markdown_options)
        else:
            out = self._render_template()
        if page.get("layout"):
            if inspect.isgenerator(out):
                out = "".join(map(str, list(out)))
            layout = page.layout
            block = "content"
            if ":" in layout:
                layout, block = layout.rsplit(":", 1)
            out = render_template_string(
                '{%% extends "%s" %%}{%% block %s %%}%s{%% endblock %%}' % (layout, block, out))
        return out
    
    def _render_template(self):
        return render_template(page.template)

    def as_view(self):
        def view_func(**args):
            return self.execute(args)
        for decorator in self.decorators:
            view_func = decorator(view_func)
        return view_func
    
    def register(self, app_or_blueprint, url=None, **add_url_rule_kwargs):
        add_url_rule_kwargs.setdefault("methods", self.methods)
        if self.endpoint:
            add_url_rule_kwargs.setdefault("endpoint", self.endpoint)
        elif self.module_name:
            add_url_rule_kwargs.setdefault("endpoint", self.module_name.replace(".", "_"))
        else:
            add_url_rule_kwargs.setdefault("endpoint", self.template.split(".")[0].replace(os.sep, "_"))
        app_or_blueprint.add_url_rule(self.url if url is None else url, view_func=self.as_view(), **add_url_rule_kwargs)