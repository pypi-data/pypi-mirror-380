import urllib.parse as urlparse
from typing import Generator, Literal, override

from ab_core.auth_flow.oauth2.schema.auth_code_stage import (
    AuthCodeStageInfo,
    AuthCodeStageInfoBeginLogin,
    AuthCodeStageInfoDone,
)
from ab_core.auth_flow.oauth2.schema.flow_type import (
    OAuth2FlowType,
)
from ab_core.impersonation.impersonator import Impersonator

from .base import OAuth2FlowBase


class ImpersonationOAuth2Flow(OAuth2FlowBase):
    """Automate browser login to capture auth code via OIDC with PKCE."""

    type: Literal[OAuth2FlowType.IMPERSONATION] = OAuth2FlowType.IMPERSONATION
    impersonator: Impersonator

    @override
    def get_code(
        self, authorize_url: str
    ) -> Generator[AuthCodeStageInfo, None, AuthCodeStageInfoDone]:
        with self.impersonator.init_context(authorize_url) as context:
            # prepare the user interaction
            interaction = self.impersonator.init_interaction(context)
            if interaction:
                yield AuthCodeStageInfoBeginLogin(
                    ws_url=interaction.ws_url,
                    gui_url=interaction.gui_url,
                )

            # intercept the response during user interaction
            with self.impersonator.intercept_response(
                context,
                cond=lambda r: r.url.startswith(str(self.idp_prefix)) and r.status == 302,
                timeout=self.timeout,
            ) as resp:
                loc = resp.headers.get("location")
                if not loc:
                    raise RuntimeError(
                        "Unable to extract Auth Code: No location found in response headers."
                    )
                auth_code = urlparse.parse_qs(urlparse.urlparse(loc).query).get("code", [None])[0]

            auth_code_done_stage = AuthCodeStageInfoDone(auth_code=auth_code)
            yield auth_code_done_stage
            return auth_code_done_stage
