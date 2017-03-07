#!/bin/bash

# shellcheck disable=SC2034
DESCRIPTION="beaglebone black"

function install_device {
    run_pip install Adafruit_BBIO
}

function install_device_config {
    config_set 'input_device' 'default:CARD=Device'
    config_set 'output_device' 'default:CARD=Device'

    config_set 'device' 'bbb'
}
