import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    assert encrypt_message("", 5) == ""
    
    assert encrypt_message("wolter", 2) == ("retl_ow")

    assert encrypt_message("wolter", 3) == ("low_ret")

    assert encrypt_message("wolter", -10) == ("retlow")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 7)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("wolter", "tr")


