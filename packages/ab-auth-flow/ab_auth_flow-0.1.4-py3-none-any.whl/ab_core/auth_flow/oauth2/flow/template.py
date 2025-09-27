from typing import Generator, Literal, override

from ab_core.auth_flow.oauth2.schema.auth_code_stage import (
    AuthCodeStageInfo,
    AuthCodeStageInfoDone,
)
from ab_core.auth_flow.oauth2.schema.flow_type import (
    OAuth2FlowType,
)

from .base import OAuth2FlowBase


class TemplateOAuth2Flow(OAuth2FlowBase):
    """Automate browser login to capture auth code via OIDC with PKCE."""

    type: Literal[OAuth2FlowType.TEMPLATE] = OAuth2FlowType.TEMPLATE

    @override
    def get_code(
        self,
        authorize_url: str,
    ) -> Generator[AuthCodeStageInfo, None, AuthCodeStageInfoDone]:
        raise NotImplementedError()
