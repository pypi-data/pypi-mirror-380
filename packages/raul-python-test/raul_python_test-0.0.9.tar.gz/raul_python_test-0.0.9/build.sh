#!/bin/bash

VERSION=`python -m setuptools_scm`
DOCKERFILE="Dockerfile"

COMMIT_HASH=$(git log -1 --pretty=format:"%H")

echo "Building version $VERSION ..."
BUILD_DATE=$(date -u +'%Y-%m-%dT%H:%M:%SZ')
docker build --rm -f $DOCKERFILE \
    --progress=plain \
    --build-arg BUILD_DATE=$BUILD_DATE \
    --build-arg COMMIT_HASH=$COMMIT_HASH \
    --build-arg VERSION=$VERSION \
    -t vieramercado/test-python:$VERSION .

echo "Tagging $VERSION as 'latest'"
docker tag vieramercado/test-python:$VERSION vieramercado/test-python:latest

echo "Version $VERSION build completed"
