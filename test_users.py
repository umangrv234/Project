import pytest
from CreateMultipleUsers import MultipleUsers

createMultipleUsers = MultipleUsers()


@pytest.mark.parametrize('total_users', [2, 3, 4])
def test_create_multiple_users(total_users):
    status_code, _ = createMultipleUsers.createMultipleUsers(noOfUsers=total_users)
    assert status_code == 200


def test_update_user_username():
    status_code, _ = createMultipleUsers.updateUserName("string", "umang1234")
    assert status_code == 200


def test_get_user_by_updated_username():
    status_code, _ = createMultipleUsers.getUsername(updatedUserName="umang1234")
    assert status_code == 200
