import pytest
from fastapi.testclient import TestClient
from tortoise.contrib.test import finalizer, initializer
from users.models import Certificate, CertificateName_Pydantic


@pytest.fixture(scope="module")
async def initialize_tests():
    initializer(["users.models"])
    yield
    await finalizer()


@pytest.fixture(scope="module")
def client(initialize_tests):
    from main import app

    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="module")
async def test_data():
    certificates = [
        {"name": "AIDA TEST"},
        {"name": "SSI TEST"},
        {"name": "PADI TEST"},
        {"name": "CMAS TEST"},
    ]
    created_certificates = []
    for certificate in certificates:
        created_certificate = await Certificate.create(**certificate)
        created_certificates.append(created_certificate)
    return created_certificates


@pytest.mark.asyncio
async def test_certificate_list(client, test_data) -> None:
    correct_data = await test_data
    response = client.get("/api/user/certificates")
    assert response.status_code == 200
    correct_data_dicts = [
        await CertificateName_Pydantic.from_tortoise_orm(cert) for cert in correct_data
    ]
    assert response.json() == {
        "status_code": 200,
        "message": "Certificates fetched successfully",
        "data": [cert.dict() for cert in correct_data_dicts],
    }
