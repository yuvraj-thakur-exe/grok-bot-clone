#!/usr/bin/env sh
set -eu
ORBIT_ROOT="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
if [ -n "${PYTHONPATH:-}" ]; then
  export PYTHONPATH="$ORBIT_ROOT/src:$PYTHONPATH"
else
  export PYTHONPATH="$ORBIT_ROOT/src"
fi
if command -v python3 >/dev/null 2>&1; then
  exec python3 -m orbit_cli "$@"
fi
if command -v python >/dev/null 2>&1; then
  exec python -m orbit_cli "$@"
fi
printf '%s\n' 'ORBIT requires Python 3.11 or newer. Install Python or uv, then rerun.' >&2
exit 127
