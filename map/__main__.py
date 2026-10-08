"""Allow ``python -m map`` to run the same report as ``python -m map.engine``."""

from map.engine import main

raise SystemExit(main())
