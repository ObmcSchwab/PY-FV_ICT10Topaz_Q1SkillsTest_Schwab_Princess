from pyscript import document

def create_order(event=None):
    # Define cookie items with IDs and labels
    cookies = [
        ("item1", "Sugar-Free Chocolate Chip Cookies"),
        ("item2", "Matcha Cookies"),
        ("item3", "Red Velvet Cookies"),
        ("item4", "Brownie Cookies")
    ]

    selected_items = []
    subtotal = 0.0

    # Check each cookie
    for item_id, label in cookies:
        checkbox = document.getElementById(item_id)
        if checkbox.checked:
            price = float(checkbox.value)
            subtotal += price
            selected_items.append(f"{label}: ₱{price:.2f}")

    # Calculate VAT and total
    vat = round(subtotal * 0.12, 2)
    total = round(subtotal + vat, 2)

    # Build receipt
    if selected_items:
        receipt_html = "<h2>Your Cookie Receipt 🍪</h2><ul>"
        for entry in selected_items:
            receipt_html += f"<li>{entry}</li>"
        receipt_html += "</ul>"
        receipt_html += f"<p>Subtotal: ₱{subtotal:.2f}</p>"
        receipt_html += f"<p>VAT (12%): ₱{vat:.2f}</p>"
        receipt_html += f"<strong>Total: ₱{total:.2f}</strong>"
    else:
        receipt_html = "<p>No cookies selected.</p>"

    # Display result
    document.getElementById("receipt").innerHTML = receipt_html
