#!/usr/bin/env python
# -*- coding: utf-8 -*-
# **************************************************************************
# Copyright © 2016 jianglin
# File Name: urls.py
# Author: jianglin
# Email: xiyang0807@gmail.com
# Created: 2016-10-03 16:57:33 (CST)
# Last Update:星期一 2016-10-3 18:26:38 (CST)
#          By:
# Description:
# **************************************************************************
from flask import Blueprint
from .views import IndexView, AboutView

site = Blueprint('index', __name__)

index_view = IndexView.as_view('index')
about_view = AboutView.as_view('about')
site.add_url_rule('/', view_func=index_view)
site.add_url_rule('/index', view_func=index_view)
site.add_url_rule('/about', view_func=about_view)
