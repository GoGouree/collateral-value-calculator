def generate_notification(stock_name, quantity, post_haircut_value):
    """
    Generates a notification string for the given stock details.

    Args:
        stock_name (str): The name of the stock.
        quantity (int): The quantity of stocks.
        post_haircut_value (float): The calculated post-haircut value.

    Returns:
        str: The notification string.
    """
    notification = (
        f"Notification:\n"
        f"Stock Name: {stock_name}\n"
        f"Quantity: {quantity}\n"
        f"Post Haircut Value: {post_haircut_value:.2f}\n"
    )
    return notification