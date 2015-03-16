#!/usr/bin/env bash

python ./generate_projects.py

CONFIGURATION="Release"
TARGET="SinchService"

# build for device
xcodebuild -target $TARGET \
    -sdk iphoneos \
    -configuration $CONFIGURATION \
    -arch armv7 -arch armv7s -arch arm64\
    clean build

# build for simulator
xcodebuild -target $TARGET \
    -sdk iphonesimulator \
    -configuration $CONFIGURATION \
    -arch i386 -arch x86_64 \
    clean build
