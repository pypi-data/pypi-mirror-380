from typing import List
from typing import NotRequired
from typing import Optional
from typing import TypedDict


class Claim(TypedDict):
    key: str
    value: str


class LvUserData(TypedDict):
    id: str
    name: str
    email: str
    cnpj: str
    cpf: str
    gender: int
    cep: NotRequired[Optional[str]]
    street: NotRequired[Optional[str]]
    complement: NotRequired[Optional[str]]
    phoneNumber: NotRequired[Optional[str]]
    neighbourhood: NotRequired[Optional[str]]
    state: int
    city: NotRequired[Optional[str]]
    mobile: NotRequired[Optional[str]]
    number: NotRequired[Optional[str]]
    twoFactorEnabled: bool
    uf: str
    metadata: NotRequired[Optional[str]]
    claims: List[Claim]
    roles: List[str]
    sellers: List[str]
    permissions: List[str]
    cnpjs: List[str]
    cpfs: List[str]
    fidRoles: NotRequired[Optional[List[str]]]
    isJSMAdmin: bool


class LvUserDataResponse(TypedDict):
    data: LvUserData
    success: bool
