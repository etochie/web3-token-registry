#!/bin/bash

ENV=""

if [ -z "${1}" ]; then
    echo "arg must be test or prod"
    exit 1
else
    case ${1} in
      "dev")
          ENV="dev"
          ;;
      "qa")
          ENV="qa"
          ;;
      "prod")
          ENV="prod"
          ;;
      *)
          echo "unsupported env"
          exit 1
          ;;
    esac
fi

echo "env: ${1}"

git pull
git tag -d ${ENV}
git push --delete origin ${ENV}
git tag -a ${ENV} -m "${ENV}"
git push origin ${ENV}
