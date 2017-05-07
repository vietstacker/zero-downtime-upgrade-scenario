#!/usr/bin/env bash

read -p "Press enter to enable buffer"

echo "Enable buffer"
curl http://192.168.122.250:5000/_intermission/enable

read -p "Press enter to upgrade"

workon master
pushd ~stack/master/kolla-ansible/tools

./kolla-ansible -i inventory --configdir etc upgrade --tags=neutron

popd
deactivate

echo "Disable buffer"
curl http://192.168.122.250:5000/_intermission/disable
