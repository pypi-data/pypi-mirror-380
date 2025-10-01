# https://{portalUrl}/api/public/v1/approve/{organization}/{group}/pkg:rl/{project}/{package}@{version}
# qp:: reason: str


from typing import (
    Any,
    List,
    Dict,
)

import logging

from spectra_assure_api_client.communication.exceptions import (
    SpectraAssureInvalidAction,
)

from .base import SpectraAssureApiOperationsBase


logger = logging.getLogger(__name__)


class SpectraAssureApiOperationsApprove(  # pylint: disable=too-many-ancestors
    SpectraAssureApiOperationsBase,
):  # pylint: disable=too-many-instance-attributes

    @staticmethod
    def qp_approve(
        *,
        what: str,
        **qp: Any,
    ) -> Dict[str, Any]:
        r: Dict[str, Any] = {}

        version_qp: List[str] = [
            "reason",
        ]

        if what in ["version"]:
            for k in version_qp:
                if k in qp:
                    r[k] = qp[k]

        return r

    def approve(
        self,
        *,
        project: str,
        package: str,
        version: str,
        auto_adapt_to_throttle: bool = False,
        **qp: Any,
    ) -> Any:
        """
        Action:
            Execute a approve() API call.

        Args:
         - project: str, mandatory.
         - package: str, mandatory.
         - version: str, mandatory.
         - auto_adapt_to_throttle: bool, default False, optional.
         - qp: Dict[str,Any] , optional.

        Return:
            The 'requests.result' of the approve API call.

        Raises:
            May raise exceptions on issues with the HTTP connection or wrong parameters.
            - SpectraAssureInvalidAction: our exception.
            - <any other exception> from requests.get().

        QueryParameters:
            scan supports the following query parameters:
             - reason: str

        """

        action = "approve"
        what = self._what(
            project=project,
            package=package,
            version=version,
        )

        supported = [
            "version",
        ]
        if what not in supported:
            msg = f"'approve' is only supported for {'and '.join(supported)}"
            raise SpectraAssureInvalidAction(message=msg)

        url = self._make_current_url(
            action=action,
            project=project,
            package=package,
            version=version,
        )

        valid_qp: Dict[str, Any] = self.qp_approve(
            what=what,
            **qp,
        )
        return self.do_it_put(
            url=url,
            auto_adapt_to_throttle=auto_adapt_to_throttle,
            **valid_qp,
        )
