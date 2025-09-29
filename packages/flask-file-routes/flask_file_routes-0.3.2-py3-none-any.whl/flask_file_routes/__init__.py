from flask import g
import jinjapy
import os
from .ctx import page, PageContext, PageResponseException, DEFAULT_HELPERS, decorator_as_page_helper
from .view import ModuleView


class FileRoutes:
    def __init__(self, app=None, **kwargs):
        self.page_helpers = {}
        if app:
            self.init_app(app, **kwargs)

    def init_app(self, app, pages_folder="pages", url_prefix="/", **kwargs):
        self.app = app

        @app.before_request
        def push_page_context():
            g.page = PageContext(self)

        @app.context_processor
        def template_context():
            return dict(page=g.page, **g.page.template_ctx)
        
        @app.errorhandler(PageResponseException)
        def handle_page_response(e):
            return e.response

        if pages_folder and os.path.exists(os.path.join(app.root_path, pages_folder)):
            self.loader, modules = register_page_package(app, pages_folder, url_prefix=url_prefix, **kwargs)

    def page_helper(self, func=None, name=None):
        def decorator(func):
            self.page_helpers[name or func.__name__] = func
            return func
        if func:
            return decorator(func)
        return decorator


def register_page_package(app_or_blueprint, path="pages", package_name=None, template_prefix=None, url_prefix="", skip_missing_frontmatter=False,
                          jinja_env=None, module_view_class=ModuleView):
    modules = []
    loader = _create_jinjapy_package(app_or_blueprint, path, package_name, template_prefix, jinja_env)
    for module_name, template in loader.list_files(module_with_package=False, with_template_prefix=False):
        if template:
            page_url_segments = template.rsplit(".", 1)[0].split(os.sep)
        else:
            page_url_segments = module_name.split(".")
        endpoint = "_".join([s[1:-1] if s.startswith("(") else s for s in page_url_segments]).replace("-", "_")
        if page_url_segments[-1] == "index":
            del page_url_segments[-1]
        url = url_prefix + "/".join([s for s in page_url_segments if not s.startswith("(")])
        if module_name:
            module_name = f"{loader.package_name}.{module_name}"
        page_module = module_view_class.create_from_module_template(loader, module_name, loader.prefix + template if template else None,
                                                                    url, skip_missing_frontmatter, endpoint)
        if page_module:
            page_module.register(app_or_blueprint)
            modules.append(page_module)
    return loader, modules


def _create_jinjapy_package(app_or_blueprint, path, package_name=None, template_prefix=None, jinja_env=None):
    if not package_name:
        package_name = os.path.basename(path)
    if template_prefix is None:
        template_prefix = package_name.replace(".", "/")
    mod = __import__(app_or_blueprint.import_name)
    if getattr(mod, "__path__", None):
        package_name = f"{app_or_blueprint.import_name}.{package_name}"
    jinja_env = jinja_env or app_or_blueprint.jinja_env
    return jinjapy.register_package(package_name, os.path.join(app_or_blueprint.root_path, path),
                                    template_prefix, env=jinja_env)
