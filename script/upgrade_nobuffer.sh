#!/usr/bin/env bash

read -p "Press enter to upgrade"

pushd ~duonghq/demo_boston/master/kolla-ansible/tools

./kolla-ansible -i inventory --configdir etc upgrade --tags=neutron

popd
