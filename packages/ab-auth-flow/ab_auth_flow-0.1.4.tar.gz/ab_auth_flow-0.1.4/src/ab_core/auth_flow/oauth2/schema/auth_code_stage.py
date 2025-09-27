from abc import ABC
from enum import StrEnum
from typing import Annotated, Literal, Optional, Tuple

from pydantic import BaseModel, Discriminator


class AuthCodeStage(StrEnum):
    BEGIN_LOGIN = "BEGIN_LOGIN"  # redirect the user to begin the login
    DONE = "DONE"  # the auth code has been retrieved


class AuthCodeStageInfoBase(BaseModel, ABC): ...


class AuthCodeStageInfoBeginLogin(AuthCodeStageInfoBase):
    stage: Literal[AuthCodeStage.BEGIN_LOGIN] = AuthCodeStage.BEGIN_LOGIN

    ws_url: str
    gui_url: Optional[str] = None


class AuthCodeStageInfoDone(AuthCodeStageInfoBase):
    event: Literal[AuthCodeStage.DONE] = AuthCodeStage.DONE

    auth_code: str


AuthCodeStageInfo = Annotated[
    Tuple[AuthCodeStageInfoBeginLogin, AuthCodeStageInfoDone],
    Discriminator("stage"),
]
