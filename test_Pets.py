import pytest
from CreateMultiplePets import CreateMultiplePets

createMultiplePets = CreateMultiplePets()
status = ['available', 'pending', 'sold']


def test_create_multiple_pets():
    status_code, _ = createMultiplePets.createMultiplePet()
    assert status_code == 200


@pytest.mark.parametrize('status', ['available', 'pending', 'sold'])
def test_update_multiple_pets(status):
    status_code, _ = createMultiplePets.updatePetStatus(status)
    assert status_code == 200


@pytest.mark.parametrize('status', status)
def test_get_pet_by_status(status):
    status_code, _, verifyUpdateStatus = createMultiplePets.getPetByStatus(status)
    assert status_code == 200
    assert verifyUpdateStatus == status
