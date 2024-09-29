#!/bin/bash

# Set variebles environment
set -a
source <(grep -v '^#' ./.env.example | sed 's/^/export /')
set +a
