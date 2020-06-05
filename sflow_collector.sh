#!/bin/bash


# COLLECTOR

git clone https://github.com/sflow/sflowtool.git

sudo apt install autoconf

./boot.sh

./configure

make

sudo make install

cd src

./sflowtool -p 8008
                                    
                                    
