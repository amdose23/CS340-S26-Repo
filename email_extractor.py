def extract_domain(email):
    """
    Extracts the domain name from an email address.

    Args:
        email (str): The email address (e.g., user@example.com).

    Returns:
        str: The domain part of the email.
    """
    parts = email.split('@')
    return parts[1]