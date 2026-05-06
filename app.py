from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify(message="Calculator API is running")


@app.route("/health")
def health():
    return jsonify(status="healthy")


@app.route("/calc")
def calculate():
    op = request.args.get("op")
    a = request.args.get("a")
    b = request.args.get("b")

    if op is None or a is None or b is None:
        return jsonify(error="Missing required parameters: op, a, b"), 400

    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return jsonify(error="a and b must be numbers"), 400

    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    elif op == "div":
        if b == 0:
            return jsonify(error="Cannot divide by zero"), 400
        result = a / b
    else:
        return jsonify(error="Invalid operation"), 400

    return jsonify(result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
