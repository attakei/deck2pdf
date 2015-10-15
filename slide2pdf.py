#!/usr/bin/env python
import sys
import os
import subprocess
import urllib2
import time


def main():
    run_dir = os.getcwd()
    root_dir = os.path.join(run_dir, '_build', 'slides')
    print(root_dir)

    import SimpleHTTPServer
    import SocketServer
    PORT = 8000
    server = SocketServer.TCPServer(("", PORT), SimpleHTTPServer.SimpleHTTPRequestHandler)

    import multiprocessing
    def httpd_server(root_dir):
        p = multiprocessing.current_process()
        os.chdir(root_dir)
        server.serve_forever()

    httpd = multiprocessing.Process(target=httpd_server, args=[root_dir])
    # httpd.daemon = True
    httpd.start()

    # Warm up
    timeout = 10
    while timeout > 0:
        try:
            urllib2.urlopen('http://localhost:8000/')
            break
        except urllib2.URLError:
            pass
        time.sleep(1)
        timeout -= 1

    # Capture
    for slide_idx in (1, 2):
        resp = urllib2.urlopen('http://localhost:8000/index.html#' + str(slide_idx))
        print(resp.read())

    # server.shutdown()
    httpd.terminate()
    while httpd.is_alive():
        time.sleep(1)

    # Merge

    # end


if __name__ == '__main__':
    main()