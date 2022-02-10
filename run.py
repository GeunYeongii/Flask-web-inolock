#run.py
import sys
from flask import Flask, redirect, request, jsonify, url_for, render_template
from app import app

app.config['TEMPLATES_AUTO_RELOAD'] = True

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
