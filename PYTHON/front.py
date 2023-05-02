from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
import plotly.graph_objects as go
import json
import plotly
import plotly.express as px

app = Flask(_name_)
app.secret_key = 'clave_secreta'

# Ruta para la página de inicio de sesión
@app.route("/")
def login():
    return render_template("login.html")

# Ruta para procesar el inicio de sesión
@app.route("/", methods=["POST"])
def process_login():
    # Obtener los datos enviados por el formulario
    username = request.form["username"]
    password = request.form["password"]

    # Validar los datos de inicio de sesión
    if username == "usuario" and password == "contraseña":
        # Si son correctos, redirigir a la página de inicio
        # de sesión con una variable de sesión que indica que
        # el usuario ha iniciado sesión correctamente
        session["logged_in"] = True
        session["username"] = username
        return redirect(url_for("grafica"))
    else:
        # Si son incorrectos, mostrar un mensaje de error
        # en la página de inicio de sesión
        error = "Nombre de usuario o contraseña incorrectos"
        return render_template("login.html", error=error)

# Ruta para la página de inicio después de iniciar sesión con éxito
@app.route("/grafica")
def grafica():
    # Verificar si el usuario ha iniciado sesión
    if not session.get("logged_in"):
        # Si no ha iniciado sesión, redirigir a la página de inicio de sesión
        return redirect(url_for("login"))

    url = "http://0.0.0.0:5000/mostrar_estacionesnivel"
    data = pd.read_json(url,convert_dates='True')

    latr = []
    lonr = []
    zr = []
    for i in range(0,100):
        zr.append(data['datos'][i]['porcentajeNivel'])
        latr.append(data['datos'][i]['coordenadas'][0]['latitud'])
        lonr.append(data['datos'][i]['coordenadas'][0]['longitud'])

    fig = go.Figure(go.Densitymapbox(lat=latr,lon=lonr,z=zr,radius=20, opacity=0.9, zmin=0,zmax=1))
    fig.update_layout(mapbox_style="stamen-terrain",mapbox_center_lon=-75.589,mapbox_center_lat=6.240)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('grafica.html', graphJSON=graphJSON)

# Ruta para cerrar sesión
@app.route("/logout")
def logout():
    # Eliminar la variable de sesión que indica que el usuario ha iniciado sesión
    session["logged_in"] = False
    session.pop("username", None)
    return redirect(url_for("login"))

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8080)
