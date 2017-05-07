#!/usr/bin/env bash

VIP=192.168.122.250
echo "Create intermission screen"
ssh $VIP 'screen -dmS intermission'

read -p "Press enter to start intermission"

start_command="docker run --rm --net=host  -v /home/stack/nginx_openstack.boston.conf:/nginx.conf --name intermission stack-team3-pc1:40000/intermission:2017"

ssh $VIP "screen -S intermission -X stuff \"$start_command
\""

read -p "Press enter to remove intermission"
echo "Stop and remove intermission"
ssh $VIP "docker stop intermission"
ssh $VIP "screen -X -S intermission quit"
