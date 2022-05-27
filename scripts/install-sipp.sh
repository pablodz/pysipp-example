#!/bin/bash
git clone https://github.com/SIPp/sipp.git && \
    cd sipp && \
    cmake . && \
    make && \
    cd ../
