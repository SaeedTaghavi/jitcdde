from ._jitcdde import (
		jitcdde, jitcdde_lyap, jitcdde_restricted_lyap, jitcdde_transversal_lyap,
		t, y, current_y, past_y, anchors,
		UnsuccessfulIntegration,
		_find_max_delay, _get_delays,
		quadrature,
		test,
		)

try:
	from .version import version as __version__
except ImportError:
	from warnings import warn
	warn('Failed to find (autogenerated) version.py. Do not worry about this unless you really need to know the version.')
