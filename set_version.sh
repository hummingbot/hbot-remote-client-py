#!/usr/bin/env bash

VERSION=$1

if [[ -z $VERSION ]]; then
    echo 'Missing version argument'
    exit 1
fi

sed -i "s/__version__ = .*/__version__ = \"${VERSION}\"/g" ./hbotrc/__init__.py
