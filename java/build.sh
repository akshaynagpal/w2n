#!/bin/zsh
#
# SPDX-FileCopyrightText: 2021 - Sebastian Ritter <bastie@users.noreply.github.com>
# SPDX-License-Identifier: MIT
#

# Informations
W2N_VERSION='1.0.0'

# save start location
LOCATION_START=`pwd`
LOCATION_SCRIPT="${0:A:h}"

# start working
cd ${LOCATION_SCRIPT}

LOCATION_TARGET="./bin"
LOCATION_SOURCE="./src"

## clean
  rm -Rf ${LOCATION_TARGET}
  mkdir -p ${LOCATION_TARGET}

  ### compile
  mv -f src/module-info.java src/module-info.bak
  mv -f src/module-info.release src/module-info.java
  
  javac -d ${LOCATION_TARGET} -sourcepath ${LOCATION_SOURCE} -target 11 -source 11 -g:none -Xlint -encoding utf8 src/word2number/W2N.java src/module-info.java
  
  mv -f ${LOCATION_SOURCE}/module-info.java ${LOCATION_SOURCE}/module-info.release
  mv -f ${LOCATION_SOURCE}/module-info.bak  ${LOCATION_SOURCE}/module-info.java
  
  ### add ressources
  LOCATION_RESSOURCES="/word2number/data"
  mkdir -p ${LOCATION_TARGET}${LOCATION_RESSOURCES}
  cp ${LOCATION_SOURCE}${LOCATION_RESSOURCES}/*.properties ${LOCATION_TARGET}${LOCATION_RESSOURCES}
  
  ### create Java archive
  cd ${LOCATION_TARGET}
  jar --create --file ./w2ni18n-${W2N_VERSION}.jar .

# worked

# go back to start location
cd ${LOCATION_START}

# EOF
