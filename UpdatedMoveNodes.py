from ast import literal_eval as make_tuple
import subprocess
import argparse
import time

wlan_range = 300

file_object = open("config.txt", "r")
start_time = time.time()
line = file_object.readline()
while (line != "end\n"):
    config_tuple = make_tuple(line)
    #(executing time, (node1, node2...), group number)
    sleep_time = config_tuple[0] - (time.time() - start_time)
    if sleep_time > 0.0:
        time.sleep(sleep_time)
    group = config_tuple[2]
    x_position = wlan_range*group
    for node in config_tuple[1]:
        print("moving node %s to group %s at time %s" %(node, group, config_tuple[0]))

        subprocess.run(["python3", "/home/jacob/core/daemon/scripts/coresendmsg",
                        "NODE", "NUMBER=%s" % node, "X_POSITION=%s" % x_position, "Y_POSITION=100"])
    line = file_object.readline()
