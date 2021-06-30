# -*- coding:UTF-8 -*-
from mitmproxy.tools._main import mitmweb
mitmweb(args=['-s', './HttpProxy.py', '-p', '9000', '--web-port', '9020'])