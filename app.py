#!/usr/bin/env python3
"""
app
"""
from flask import Flask, render_template, request, abort, jsonify
from configs.xtoxica_configs import *

host_url = f"{host_ip}:{main_port_no}"

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def homepage():
    """
    home page
    """
    # here I want to pass host_ip to the html file index.html

    return render_template("index.html", host_url=host_url)

@app.route("/about", strict_slashes=False)
def about_us():
    """
    About us page
    """
    return render_template("about_us.html", host_url=host_url)

@app.route("/contact", strict_slashes=False)
def contact_us():
    """
    contact us page
    """
    return render_template("contact_us.html", host_url=host_url)

@app.route("/help", strict_slashes=False)
def help():
    """
    help page
    """
    return render_template("help.html", host_url=host_url)



if __name__ == "__main__":
    app.run(host=main_host_ip, port=main_port_no, debug=main_debug_state)
