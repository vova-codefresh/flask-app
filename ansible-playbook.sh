#!/bin/bash
# ansible-playbook.sh $PARAM_ENVIRONMENT $ANSIBLE_PLAYBOOK "$ANSIBLE_HOSTS"
#
# exmple:
#
# ./ansible-playbook.sh aws-load docker-node cf-load-aue1-docker-node-0005


echo "PARAM_ENVIRONMENT = $1 "
echo "ANSIBLE_PLAYBOOK = $2 "
echo "ANSIBLE_HOSTS = $3 "

