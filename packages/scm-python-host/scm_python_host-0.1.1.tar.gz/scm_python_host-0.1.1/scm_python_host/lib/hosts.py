import sys, re, os
import tlog.tlogging as tl
import tio.tfile as tf
import tio.tshell as ts
import tutils.thpe as thpe
import tutils.context_opt as tcontext
import tutils.ttemplate as ttemplate

from tio.tcli import *

log = tl.log
flags = [
    ("n:", "host=", "hostname", ["host", "host/disable", "host/enable", "host/test"]),
    ("i:", "ip=", "ip", "host/enable"),
    ("b:", "branch=", "branch 90_cpe", ["host/test", "host/vscode"]),
    ("r", "force", "force to update", "host/test", "host/vscode"),
]

opp = OptParser(flags)

host_file = "c:\\Windows\\System32\\drivers\\etc\\hosts"


@cli_invoker("host/show|print|cat|more")  # print hosts file in console
def printroute():
    for line in tf.readlines(host_file):
        print(line)


@cli_invoker("host/test")  # print hosts file in console
def testroute(force, host=False, branch=False):
    print(force, host, branch)
    print(f"{force}.{host}.{branch}")
    num = 12.345678
    width = 4
    precision = 4
    print(f"num is {num:{width}.{precision}}")
    print(f"num is {num:4.12}")
    # ts.pipeline('dir . /s')


@cli_invoker("host/|enable")  # add/update a route in hosts
def updaterouter(host: str, ip=""):
    tf.backup(host_file)
    lists = tf.readlines(host_file)
    pattern = re.compile(r"^#*\s*([0-9\.]+)\s+" + host)
    done = False
    writes = []
    log.info("param " + host + ":" + ip)
    for line in lists:
        so = pattern.search(line)
        if so:
            if not done:
                done = True
                ip = ip if ip else so.group(1)
                log.info(f"enable {ip} {host}")
                writes.append(f"{ip} {host}")
            else:
                writes.append(line)
                if not done:
                    if not ip:
                        log.error("ip is compulsory for " + host)
                    else:
                        log.info("add {ip} {host}")
                        writes.append(f"{ip} {host}")
        else:
            writes.append(line)
    if not done:
        log.info(f"add {ip} {host}")
        writes.append(f"{ip} {host}")
        done = True
    with open(host_file, "w") as fw:
        for line in writes:
            fw.write(line + "\n")


@cli_invoker("host/disable")  # disable a route in hosts
def disablerouter(host):
    tf.backup(host_file)
    lists = tf.readlines(host_file)
    writes = []
    pattern = re.compile(r"^\s*([0-9\.]+)\s+" + host)
    for line in lists:
        so = pattern.search(line)
        if so:
            log.info("disable " + so.group(1) + " " + host)
            writes.append("#" + so.group(1) + " " + host)
        else:
            writes.append(line)
    with open(host_file, "w") as fw:
        for line in writes:
            fw.write(line + "\n")


"""
    生成vscode的相关文件,例如project manager配置
    相关配置文件
    sample.yaml:    sh/etc/vscode.template.sample.yaml
    runtime.yaml:   ${hostname}/etc/vscode.template.runtime.yaml
"""


@cli_invoker("host/vscode")  # vscode cfg
def vscode_project_json(force):
    vscode_inst = os.path.abspath(
        os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Code")
    )
    installation = tcontext.load_item(
        thpe.load_template_yaml("vscode"), "vscode/plugins/installation"
    )
    if not installation:
        log.error(f"vscode/plugins/installation is not defined in the vscode yaml")
        return
    context = {}
    context["git_repo"] = tf.escape_path(thpe.git_repo_home())
    log.info(context)
    for file_definition in installation["files"]:
        target_files = file_definition["path"]
        target_files = os.path.abspath(os.path.join(vscode_inst, target_files))
        log.info(target_files)
        if not os.path.exists(target_files):
            tf.writelines(target_files, file_definition["newFile"])
        ttemplate.file_replace_and_persist(
            context, file_definition["templates"], target_files
        )


@cli_invoker("host/npm")  # npm install
def npm_env():
    cmds = ["npm install webpack -g"]
    ts.pipeline(*cmds)


@cli_invoker("host/python")  # python plugins install
def python_env():
    cmds = ["pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple"]
    ts.pipeline(*cmds)


@cli_invoker("host/http-server")  # start a http server for debug
def host_http_server_handler():
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import signal
    import threading
    import time

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            print(f"GET {self.path}", flush=True)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")

        def do_POST(self):
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode()
            print(f"POST {self.path}\nBody: {body}", flush=True)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")

    port = 8080
    server = HTTPServer(("0.0.0.0", port), Handler)
    stop_event = threading.Event()

    def serve():
        print(f"服务器运行中: http://localhost:{port}", flush=True)
        server.serve_forever()
        print("服务器已停止", flush=True)

    thread = threading.Thread(target=serve, daemon=True)
    thread.start()

    def handle_sigint(signum, frame):
        print("\n捕获到 Ctrl+C, 正在关闭服务器...", flush=True)
        server.shutdown()  # 这次可以正常退出
        thread.join()
        sys.exit(0)

    signal.signal(signal.SIGINT, handle_sigint)

    # Windows/Linux 通用等待
    try:
        while not stop_event.is_set():
            time.sleep(0.5)
    except KeyboardInterrupt:
        handle_sigint(None, None)
        thread.join()
