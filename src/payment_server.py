from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/pay", methods=["POST"])
def pay():
    data = request.get_json(force=True)
    amount = data.get("amount")
    account = data.get("account")

    if not account or amount is None:
        return jsonify({"error": "Missing required fields"}), 400

    if not isinstance(amount, (int, float)) or amount <= 0:
        return jsonify({"error": "Invalid amount"}), 422

    return jsonify({"status": "success", "account": account, "amount": amount}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
