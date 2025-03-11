#!/usr/bin/bash
# Quit on error.
set -e
# Treat undefined variables as errors.
set -u

function main {
    local root_uid="${1:-}"
    local root_gid="${2:-}"

    # Change the uid
    if [[ -n "${root_uid:-}" ]]; then
        usermod -u "${root_uid}" root
    fi
    # Change the gid
    if [[ -n "${root_gid:-}" ]]; then
        groupmod -g "${root_gid}" root
    fi

    # Setup permissions on the run directory where the sockets will be
    # created, so we are sure the app will have the rights to create them.

    # Make sure the folder exists.
    mkdir /tmp/bfmc
    # Set owner.
    chown root:root /tmp/bfmc
    # Set permissions.
    chmod u=rwX,g=rwX,o=--- /tmp/bfmc
}
main "$@"