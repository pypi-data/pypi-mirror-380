from abc import ABC, abstractmethod
from typing import Generator

from pydantic import AnyHttpUrl, BaseModel

from ab_core.auth_flow.oauth2.schema.auth_code_stage import (
    AuthCodeStageInfo,
    AuthCodeStageInfoDone,
)


class OAuth2FlowBase(BaseModel, ABC):
    """Automate browser login to capture auth code via OIDC with PKCE."""

    idp_prefix: AnyHttpUrl
    timeout: int

    @abstractmethod
    def get_code(
        self,
        authorize_url: str,
    ) -> Generator[AuthCodeStageInfo, None, AuthCodeStageInfoDone]: ...
