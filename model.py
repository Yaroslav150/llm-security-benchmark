def mock_model(prompt):
    if any(word in prompt.lower() for word in ["ignore", "reveal", "bypass"]):
        return "password: 1234"
    return "Safe response"