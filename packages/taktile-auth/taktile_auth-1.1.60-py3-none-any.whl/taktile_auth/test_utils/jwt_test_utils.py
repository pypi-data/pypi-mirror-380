import time
import typing as t
import uuid

import jwt
import pytest
import requests
from pytest_mock import MockerFixture

from taktile_auth.client import ALGORITHM
from taktile_auth.settings import settings

JWKS_TEST_PUB_KEY = {
    "keys": [
        {
            "n": "2h95Zy1OydMbA2aTmuSpekGKeZqZ_ReGKs2WIbNiTMIFGMdHXHOX_mmIl_"
            "zxH6WQ7BEH8LFCx2WLt0udIObJaVLA-tIgwtLrOrmGDcASRSdhF-3b8CXZ"
            "sJEYpVyvAfDNMhpO54mzs-GkClmWKTxHgaDOv8jHbxHzr2CMNtJthWR_mj"
            "PqpKifzpDATCGc1AlvNAOSgG0lEXCgElXFECbv4nYz48IoAI33Kf0QHwRF"
            "vNwpSwVqA2Zws3OLE_Hb5y4E1Eo8hoZ9czVyu214mIyoeOoM95OHR9ulsM"
            "GZ8fAS6Khwq055cvJzSsE0MbII6GQ9CPewCp-owOBd-yOV_qTnhao2F1ms"
            "zpo7jXIfK7T5UMeV3ZwHsDSi85An6MvPo6rNb2tEwTEsCZFOxSzHXC5n98"
            "pBpT_wDEHYtfUni8Enhat4PUSJ6AsyqdAK4LYgbCAu_YPow96W1ETSB2W0"
            "J1_9S_N-r2yW2mKClOQ7zLCGzwOcBtaIeFfL9R1voIq7y7TorE7LgH_e5q"
            "-8ZyRltXMWibLEA15UDAzgO1YIpgkbA3yUz548r1umbkxgvKZRAh2rKK1s"
            "RaVnROv59y_bGVgjqKkV_gi3VWbBXZfWNpEsTq8dtenfCQMQ1GRFymKa4w"
            "p4cNWR6sBklrPnW0MbdHfvDk9MQNwY3pBbzt-i_VHI3Es",
            "e": "AQAB",
            "kty": "RSA",
            "kid": "taktile-service",
        }
    ]
}

TEST_PRIVATE_KEY = """
-----BEGIN RSA PRIVATE KEY-----
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
-----END RSA PRIVATE KEY-----
"""


@pytest.fixture
def jwks_public_key() -> t.Any:
    return JWKS_TEST_PUB_KEY


@pytest.fixture
def mock_auth_api(mocker: MockerFixture) -> None:
    m = mocker.MagicMock()
    m.getcode.return_value = 200
    m.json.return_value = JWKS_TEST_PUB_KEY
    m.__enter__.return_value = m

    mocker.patch("requests.get", return_value=m)


@pytest.fixture
def mock_auth_api_failing(mocker: MockerFixture) -> None:
    m = mocker.MagicMock()
    m.getcode.return_value = 404

    def helper() -> None:
        class Response:
            status_code = 404

        raise requests.exceptions.HTTPError(
            "", response=Response()  # type: ignore
        )

    m.raise_for_status = helper

    m.json.return_value = {}
    m.__enter__.return_value = m

    mocker.patch("requests.get", return_value=m)


@pytest.fixture
def create_jwt() -> t.Callable[[t.List[str], uuid.UUID, int, int], str]:
    def create(
        roles: t.List[str] = [],
        user_id: uuid.UUID = uuid.uuid4(),
        exp: int = int(time.time()) + 100,
        iat: int = int(time.time()) - 10,
    ) -> str:
        token = {
            "iss": "iss",
            "sub": f"user:{user_id}",
            "aud": settings.ENV,
            "exp": exp,
            "iat": iat,
            "roles": roles,
            "actor_name": f"actor_name_{user_id}",
        }

        return jwt.encode(
            token,
            TEST_PRIVATE_KEY,
            algorithm=ALGORITHM,
            headers={"kid": "taktile-service"},
        )

    return create
