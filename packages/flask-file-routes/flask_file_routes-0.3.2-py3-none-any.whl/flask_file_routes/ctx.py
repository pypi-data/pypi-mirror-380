from flask import request, redirect, abort, flash, g
from werkzeug.local import LocalProxy


page = LocalProxy(lambda: g.page)
DEFAULT_HELPERS = {}


class PageContext:
    def __init__(self, ext):
        object.__setattr__(self, "ext", ext)
        object.__setattr__(self, "template_ctx", {})
        object.__setattr__(self, "helpers", {})

    def __getattr__(self, key):
        if key in self.template_ctx:
            return self.template_ctx[key]
        if key in request.view_args:
            return request.view_args[key]
        if key in self.helpers:
            return self.helpers[key]
        if key in self.ext.page_helpers:
            self.helpers[key] = self.ext.page_helpers[key](self)
            return self.helpers[key]
        if key in DEFAULT_HELPERS:
            self.helpers[key] = DEFAULT_HELPERS[key](self)
            return self.helpers[key]
        raise AttributeError()

    def __setattr__(self, key, value):
        self.template_ctx[key] = value

    def get(self, key, default=None):
        return self.template_ctx.get(key, default)
    
    def respond(self, response):
        raise PageResponseException(response)
    
    def redirect(self, url, **kwargs):
        self.respond(redirect(url, **kwargs))

    def abort(self, code):
        abort(code)

    def flash(self, message, category="message"):
        flash(message, category)
    

class PageResponseException(Exception):
    def __init__(self, response):
        super().__init__()
        self.response = response


def decorator_as_page_helper(decorator):
    def page_helper(page):
        def func():
            r = decorator(lambda **kw: None)()  #noqa
            if r:
                page.respond(r)
        return func
    return page_helper