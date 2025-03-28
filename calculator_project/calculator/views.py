import math
from django.shortcuts import render

def calculator_view(request):
    result = None
    history = request.session.get("history", [])  # Retrieve history from session

    if request.method == "POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        operation = request.POST.get("operation")

        try:
            if operation == "sqrt":  # Square root operation
                num1 = float(num1)  # Only one number needed
                if num1 < 0:
                    result = "Error: Cannot calculate square root of a negative number"
                    operation_text = f"√{num1} = Error"
                else:
                    result = math.sqrt(num1)
                    operation_text = f"√{num1} = {result}"
            else:
                num1 = float(num1)
                num2 = float(num2)

                if operation == "add":
                    result = num1 + num2
                    operation_text = f"{num1} + {num2} = {result}"
                elif operation == "subtract":
                    result = num1 - num2
                    operation_text = f"{num1} - {num2} = {result}"
                elif operation == "multiply":
                    result = num1 * num2
                    operation_text = f"{num1} × {num2} = {result}"
                elif operation == "divide":
                    if num2 == 0:
                        result = "Cannot divide by zero"
                        operation_text = f"{num1} ÷ {num2} = Error (Cannot divide by zero)"
                    else:
                        result = num1 / num2
                        operation_text = f"{num1} ÷ {num2} = {result}"

            # Store in history (limit to last 5 calculations)
            history.insert(0, operation_text)  # Insert at the beginning
            history = history[:5]  # Keep only the last 5 calculations
            request.session["history"] = history  # Save to session


        except ValueError:
            result = "Invalid input"

    return render(request, "calculator.html", {"result": result, "history": history})
