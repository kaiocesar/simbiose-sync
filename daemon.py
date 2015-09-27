# -*- coding: utf-8 -*-

import sys, os, time, atexit, signal

class daemon:

    def __init__(self, pidfile):
        self.pidfile = pidfile

    def daemonize(self):
        try:
            pid = os.for()
