from django.shortcuts import render
import math


def validate_input(num1, num2, operation):
    """Validates input values based on the operation type."""
    if not num1:
        return "First number is required", None, None
    try:
        num1 = float(num1)
    except ValueError:
        return "Invalid input for first number", None, None

    if operation == "sqrt":
        return None, num1, None  # num2 not needed

    if not num2:
        return "Second number is required for this operation", None, None
    try:
        num2 = float(num2)
    except ValueError:
        return "Invalid input for second number", None, None

    return None, num1, num2


def perform_calculation(num1, num2, operation):
    """Performs the requested mathematical operation."""
    operations = {
        "add": (num1 + num2, f"{num1} + {num2} = {num1 + num2}"),
        "subtract": (num1 - num2, f"{num1} - {num2} = {num1 - num2}"),
        "multiply": (num1 * num2, f"{num1} × {num2} = {num1 * num2}"),
        "percentage": (num1 * (num2 / 100), f"{num2}% of {num1} = {num1 * (num2 / 100)}"),
        "divide": (None if num2 == 0 else num1 / num2,
                   f"{num1} ÷ {num2} = {num1 / num2}" if num2 != 0 else "Cannot divide by zero"),
        "exponent": (num1 ** num2, f"{num1} ^ {num2} = {num1 ** num2}")
    }

    if operation == "sqrt":
        if num1 < 0:
            return "Error: Cannot calculate square root of a negative number", f"√{num1} = Error"
        return math.sqrt(num1), f"√{num1} = {math.sqrt(num1)}"

    return operations.get(operation, ("Invalid operation", "Invalid operation"))


def calculator_view(request):
    """Handles calculator operations and session history."""
    result, operation_text = None, None
    history = request.session.get("history", [])

    if request.method == "POST":
        action = request.POST.get("action")

        # ✅ Handle Reset
        if action == "reset":
            request.session.pop("history", None)
            return render(request, "calculator.html", {"result": None, "history": []})

        num1, num2, operation = request.POST.get("num1"), request.POST.get("num2"), request.POST.get("operation")

        # ✅ Validate Input
        error, num1, num2 = validate_input(num1, num2, operation)
        if error:
            result = error
        else:
            result, operation_text = perform_calculation(num1, num2, operation)

        # ✅ Store in History
        if operation_text and result is not None:
            history.insert(0, operation_text)
            history = history[:5]
            request.session["history"] = history

    return render(request, "calculator.html", {"result": result, "history": history})
