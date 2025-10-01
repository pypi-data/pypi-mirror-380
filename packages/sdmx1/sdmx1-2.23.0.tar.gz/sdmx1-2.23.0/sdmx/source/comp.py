from sdmx.source import Source as BaseSource

from .estat import handle_references_param


class Source(BaseSource):
    """Handle `COMP` quirks.

    .. versionadded:: 2.13.2
    """

    _id = "COMP"

    def modify_request_args(self, kwargs):
        """Modify arguments used to build query URL.

        See also
        --------
        :func:`.handle_references_param`, :issue:`162`
        """
        super().modify_request_args(kwargs)

        handle_references_param(kwargs)
