#!/home/vagrant/.pyenv/shims/python
# -*- coding: utf-8 -*-

"""
漏洞扫描脚本
"""

import os
import subprocess
import threading
import sys

from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
from urllib.parse import unquote

DEBUG = False
if len(sys.argv) > 1 and sys.argv[1].upper() == 'DEBUG':
    DEBUG = True

host = ('0.0.0.0', 8888)

VULNSCAN_HOME = os.getcwd()
OUT_PATH = os.path.join(VULNSCAN_HOME, "output")
if not os.path.exists(OUT_PATH):
    os.makedirs(OUT_PATH)


class Request(BaseHTTPRequestHandler):
    """请求处理方法
    """
    timeout = 5
    # 服务器版本
    server_version = "Vulnscan"

    uid = None
    task_id = None
    scan_url = None
    api = None

    def do_GET(self):
        """get 请求处理方法
        """
        if self.validate_path is None:
            return

        output_file = f'{self.task_id}.html'
        web_scaner = WebScanner(
            uid=self.uid,
            task_id=self.task_id,
            url=self.scan_url,
            output_file=output_file,
            api=self.api
            )
        if DEBUG:
            web_scaner.run()
        else:
            web_scaner.start()

        self.send_response(200)
        # 设置响应体类型
        self.send_header("Content-type", "text/html")
        self.end_headers()
        buf = 'ok'
        self.wfile.write(buf.encode())

    def do_POST(self):
        self.do_GET()

    @property
    def validate_path(self):
        """校验路径与参数
        """
        if '?' not in self.path or '&' not in self.path:
            self.send_error(400)
            self.wfile.write(b'{"error":400,"msg":"Bad Request"}')
            return

        url_path, url_query = self.path.split('?')
        if url_path != '/start':
            self.send_error(404)
            self.wfile.write(b'{"error":404,"msg":"Not Found"}')
            return

        params = dict(p.split('=') for p in url_query.split('&'))
        if ('uid' not in params.keys()
                or 'task_id' not in params.keys()
                or 'url' not in params.keys()
                or 'api' not in params.keys()
                or params['uid'] == ''
                or params['task_id'] == ''
                or params['url'] == ''
                or params['api'] == ''):
            self.send_error(400)
            self.wfile.write(b'{"error":400,"msg":"Bad Request"}')
            return
        # print(self.path)

        self.uid = params['uid']
        self.task_id = params['task_id']
        self.scan_url = unquote(params['url'])
        self.api = unquote(params['api'])
        # print(self.scan_url)

        return True


class WebScanner:
    """漏洞扫描器
    """

    XRAY_HOME = os.environ.get("XRAY_HOME")
    XRAY_CMD = os.environ.get("XRAY_CMD") or 'xray_linux_amd64'

    def __init__(self, uid, task_id, url, output_file, api):
        self.uid = uid
        self.task_id = task_id
        self.url = url
        self.output_file = output_file
        self.api = api
        # print(self.output_file)

    def start(self):
        """开启线程
        """
        thread = threading.Thread(target=self.run)
        thread.start()

    def run(self):
        """开始扫描
        """
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        os.chdir(self.XRAY_HOME)
        xray_cmd = f"./{self.XRAY_CMD} webscan --basic-crawler {self.url}\
                --html-output {os.path.join(OUT_PATH, self.output_file)}"

        cmd = ["bash", "-c", xray_cmd]
        if DEBUG:
            ret = subprocess.run(
                cmd,
                check=False,
                shell=False
            )
        else:
            ret = subprocess.run(
                cmd,
                check=False,
                shell=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
        task_statu_id = 2
        if ret.returncode != 0:
            task_statu_id = 3
        post_report(
            uid=self.uid,
            task_id=self.task_id,
            task_status_id=task_statu_id,
            api=self.api,
            report_file=self.output_file
        )
        return ret


def post_report(uid, task_id, task_status_id, api, report_file):
    payload = (('uid', uid), ('task_id', task_id), ('task_status_id', task_status_id))
    print(payload)
    files = None
    if report_file is not None:
        files = {
            'report_file': (report_file, open(os.path.join(OUT_PATH, report_file), 'rb'), 'text/html', {'Expires': '0'})
        }
    r = requests.post(api, data=payload, files=files)
    print(r.status_code, r.text)


if __name__ == '__main__':
    server = HTTPServer(host, Request)
    print("Starting server, listen at: %s:%s" % host)
    mode = {True: 'on', False: 'off'}
    print(f"Debug mode is {mode[DEBUG]}")
    server.serve_forever()
