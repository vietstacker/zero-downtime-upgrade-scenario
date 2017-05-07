#!/usr/bin/env python

import subprocess
from subprocess import PIPE
import itertools
import time

RANDOM = 0
SEQUENCE = 1


def start_test(command_list = [], total_commands = 0, append_id = True,
        run_mode = SEQUENCE):
    foutput = open("output.txt", "w")
    ferror = open("error.txt", "w")
    #ferror = foutput
    error_count = 0
    p = subprocess.Popen('openstack', stdin=PIPE, stdout=foutput, stderr=ferror,
                universal_newlines = True)
    stdin = p.stdin

    for i in itertools.izip(xrange(total_commands), itertools.cycle(command_list)):
        time.sleep(0.1)
        if append_id:
            stdin.write(i[1] + str(i[0]) + "\n")
        else:
            stdin.write(i[1] + "\n")

    stdin.close()
    p.wait()
    foutput.close()

def start_group_test(command_list = [], total_commands = 0, append_id = True):
    foutput = open("output.txt", "a")
    ferror = open("error.txt", "a")
    #ferror = foutput
    error_count = 0
    p = subprocess.Popen('openstack', stdin=PIPE, stdout=foutput, stderr=ferror,
                universal_newlines = True)
    stdin = p.stdin

    openstack_processes = []

    for i in xrange(total_commands):
        for command in command_list:
            time.sleep(0.5)
            if append_id:
                command = command + str(i)
            command = command + "\n"
            print command
            stdin.write(command)

    stdin.close()
    p.wait()
    foutput.close()


if __name__ == "__main__":
    #start_test([ "port list", "network list"], 10000)
    start_group_test([ "network create temp", "network delete temp" ], 150)
