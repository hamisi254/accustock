from flask import Blueprint, redirect, url_for, flash, request, render_template
route=Blueprint('route', __name__)

@route.route('/', methods=['GET'])
def index():
    return render_template('index.html')
