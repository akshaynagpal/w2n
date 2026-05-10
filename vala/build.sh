#!/bin/zsh
rm -R ./bin
meson setup bin
ninja -C bin

# create dist
cd ./bin
ninja dist
cd ..


# EOF
