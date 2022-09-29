from flask import render_template, request
from keep_alive import keep_alive, app


@app.route("/")
def main():
    return render_template("calculator.html")


@app.route("/resultado", methods=["POST"])
def calculate():
    numero_um = request.form["numero_um"]
    numero_dois = request.form["numero_dois"]
    operacao = request.form["operacao"]

    if operacao == "soma":
        result = float(numero_um) + float(numero_dois)
        return render_template("calculator.html", result=result)

    elif operacao == "subtracao":
        result = float(numero_um) - float(numero_dois)
        return render_template("calculator.html", result=result)

    elif operacao == "multiplicacao":
        result = float(numero_um) * float(numero_dois)
        return render_template("calculator.html", result=result)

    elif operacao == "divisao":
        result = float(numero_um) / float(numero_dois)
        return render_template("calculator.html", result=result)

    else:
        return render_template("calculator.html")


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html", error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template("500.html", error=error)


if __name__ == "__main__":
    keep_alive()
