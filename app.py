# coding: utf-8
"""
The MIT License (MIT)

Copyright (c) 2013 Fatih Karatana

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

@package
@date 26/11/13
@author fatih
@version 1.0.0
"""

try:
    import flask
    from flask import Flask
    from flask import render_template
    from flask import request
    from flask import session
    from helper.Resources import Resources, utilities
    from controller import Controller
except ImportError as exception:
    print "Error occurred while importing packages in Utilities file with Exception: ", exception.message

app = Flask(__name__)


@app.route('/add', methods=["POST", "GET"])
def add():
    """
    Insert To-Do into the database
    """
    try:
        controller = Controller()
        status = request.form["status"] if "status" in request.form else None
        due_date = request.form["duedate"] if "duedate" in request.form else None
        value = request.form["value"] if "value" in request.form else None
        assignee = request.form["assignee"] if "assignee" in request.form else None
        response = controller.add_task(status=status,
                                       due_date=due_date,
                                       value=value,
                                       assignee=assignee)
    except BaseException as exception:
        utilities.log(
            utilities.logging.CRITICAL, "Error occurred while removing data on remove route. Exception: " +
            exception.message
        )
    finally:
        return flask.jsonify(response)


@app.route('/edit', methods=["POST", "GET"])
def edit():
    """
    Insert To-Do into the database
    """
    try:
        controller = Controller()
        id = request.form["id"] if "id" in request.form else None
        status = request.form["status"] if "status" in request.form else None
        due_date = request.form["duedate"] if "duedate" in request.form else None
        value = request.form["value"] if "value" in request.form else None
        assignee = request.form["assignee"] if "assignee" in request.form else None
        response = controller.edit_task(task_id=id,
                                        status=status,
                                        due_date=due_date,
                                        value=value,
                                        assignee=assignee)
    except BaseException as exception:
        utilities.log(
            utilities.logging.CRITICAL, "Error occurred while removing data on remove route. Exception: " +
            exception.message
        )
    finally:
        return flask.jsonify(response)


@app.route('/remove', methods=["POST", "GET"])
def remove():
    """
    Insert To-Do into the database
    """
    try:
        controller = Controller()
        id = request.form["id"]
        response = controller.remove_task(id)
    except BaseException as exception:
        utilities.log(
            utilities.logging.CRITICAL, "Error occurred while removing data on remove route. Exception: " +
            exception.message
        )
    finally:
        return flask.jsonify(response)


@app.route('/')
def index():
    """
    Index route for application
    """
    try:
        controller = Controller()
        title = Resources.APP["title"]
        tasks = controller.get_task_list()
        users = controller.get_users_list()
        return render_template("index.html",
                               title=title,
                               tasks=tasks,
                               users=users)
    except BaseException as exception:
        print exception.message


if __name__ == '__main__':
    app.run(host=Resources.APP["host"],
            port=Resources.APP["port"],
            debug=Resources.APP["debug"])
