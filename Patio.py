@app.patch("/orders/<int:order_id>")
def update_payment(order_id):
    order = find_order(order_id)
    if order is None:
        return jsonify({"error": "Order not found"}), 404
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or not isinstance(data.get("paid"), bool):
        return jsonify({"error": "paid must be true or false"}), 400
    order["paid"] = data["paid"]
    return jsonify(order), 200