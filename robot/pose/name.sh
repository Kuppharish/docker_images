#!/bin/bash

for f in ./*.npy; do 
    mv "${f}" "pose${f#./}"
done
