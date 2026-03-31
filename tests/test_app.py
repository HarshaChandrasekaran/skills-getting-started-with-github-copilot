"""
FastAPI tests using the AAA (Arrange-Act-Assert) pattern
"""


def test_get_activities(client, reset_activities):
    """Test GET /activities returns all activities"""
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert expected_activity in response.json()
    assert len(response.json()) > 0


def test_signup_success(client, reset_activities):
    """Test successful signup for an activity"""
    # Arrange
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert f"Signed up {email}" in response.json()["message"]


def test_signup_already_registered(client, reset_activities):
    """Test signup fails for already registered student"""
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Already registered

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_nonexistent_activity(client, reset_activities):
    """Test signup fails for non-existent activity"""
    # Arrange
    activity_name = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]


def test_unregister_success(client, reset_activities):
    """Test successful unregister from an activity"""
    # Arrange
    activity_name = "Chess Club"
    email = "michael@mergington.edu"  # Initially registered

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert f"Unregistered {email}" in response.json()["message"]


def test_unregister_not_registered(client, reset_activities):
    """Test unregister fails for student not registered"""
    # Arrange
    activity_name = "Chess Club"
    email = "notregistered@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 400
    assert "not registered" in response.json()["detail"]


def test_unregister_nonexistent_activity(client, reset_activities):
    """Test unregister fails for non-existent activity"""
    # Arrange
    activity_name = "Nonexistent Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister",
        params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert "Activity not found" in response.json()["detail"]
