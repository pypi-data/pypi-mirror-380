from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "smdp_address": "smdpAddress",
        "manual_activation_code": "manualActivationCode",
        "is_top_up_allowed": "isTopUpAllowed",
    }
)
class GetEsimOkResponseEsim(BaseModel):
    """GetEsimOkResponseEsim

    :param iccid: ID of the eSIM, defaults to None
    :type iccid: str, optional
    :param smdp_address: SM-DP+ Address, defaults to None
    :type smdp_address: str, optional
    :param manual_activation_code: The manual activation code, defaults to None
    :type manual_activation_code: str, optional
    :param status: Status of the eSIM, possible values are 'RELEASED', 'DOWNLOADED', 'INSTALLED', 'ENABLED', 'DELETED', or 'ERROR', defaults to None
    :type status: str, optional
    :param is_top_up_allowed: Indicates whether the eSIM is currently eligible for a top-up. This flag should be checked before attempting a top-up request., defaults to None
    :type is_top_up_allowed: bool, optional
    """

    def __init__(
        self,
        iccid: str = SENTINEL,
        smdp_address: str = SENTINEL,
        manual_activation_code: str = SENTINEL,
        status: str = SENTINEL,
        is_top_up_allowed: bool = SENTINEL,
        **kwargs
    ):
        """GetEsimOkResponseEsim

        :param iccid: ID of the eSIM, defaults to None
        :type iccid: str, optional
        :param smdp_address: SM-DP+ Address, defaults to None
        :type smdp_address: str, optional
        :param manual_activation_code: The manual activation code, defaults to None
        :type manual_activation_code: str, optional
        :param status: Status of the eSIM, possible values are 'RELEASED', 'DOWNLOADED', 'INSTALLED', 'ENABLED', 'DELETED', or 'ERROR', defaults to None
        :type status: str, optional
        :param is_top_up_allowed: Indicates whether the eSIM is currently eligible for a top-up. This flag should be checked before attempting a top-up request., defaults to None
        :type is_top_up_allowed: bool, optional
        """
        self.iccid = self._define_str(
            "iccid", iccid, nullable=True, min_length=18, max_length=22
        )
        self.smdp_address = self._define_str(
            "smdp_address", smdp_address, nullable=True
        )
        self.manual_activation_code = self._define_str(
            "manual_activation_code", manual_activation_code, nullable=True
        )
        self.status = self._define_str("status", status, nullable=True)
        self.is_top_up_allowed = is_top_up_allowed
        self._kwargs = kwargs


@JsonMap({})
class GetEsimOkResponse(BaseModel):
    """GetEsimOkResponse

    :param esim: esim, defaults to None
    :type esim: GetEsimOkResponseEsim, optional
    """

    def __init__(self, esim: GetEsimOkResponseEsim = SENTINEL, **kwargs):
        """GetEsimOkResponse

        :param esim: esim, defaults to None
        :type esim: GetEsimOkResponseEsim, optional
        """
        self.esim = self._define_object(esim, GetEsimOkResponseEsim)
        self._kwargs = kwargs
