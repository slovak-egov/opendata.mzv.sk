# encoding: utf-8
from flask import render_template
from ckan.common import g
import ckan.lib.helpers as h
from ckan.common import config


class MzvController():

    @staticmethod
    def technical_support():
        return render_template("mzv_pages/technical_support/index.html")

    @staticmethod
    def content_manager():
        return render_template("mzv_pages/content_manager/index.html")

    @staticmethod
    def cookies():
        return render_template("mzv_pages/cookies/index.html")

    @staticmethod
    def accessibility_statement():
        return render_template("mzv_pages/accessibility_statement/index.html")

    @staticmethod
    def contact():
        return render_template("mzv_pages/contact/index.html")

    @staticmethod
    def docs():
        return render_template("mzv_pages/docs/index.html")

    @staticmethod
    def api_docs():
        return render_template("mzv_pages/api_docs/index.html")

    @staticmethod
    def index():
        if g.userobj:
            return h.redirect_to(
                config.get(u'ckan.route_after_login', u'dashboard.index'))
        else:
            return render_template('home/index.html')
