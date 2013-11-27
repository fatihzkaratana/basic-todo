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

@package controller
@date 26/11/13
@author fatih
@version 1.0.0
"""
import json
import uuid
from model.Task import Task
from helper.Resources import Resources, utilities
import random

__author__ = 'fatih'
__date__ = '26/11/13'
__version__ = '1.0.0'


class Controller(object):
    """
    Controller
    """

    def __init__(self):
        """
        Regular constructor for Controller
        """

    def get_task_list(self):
        """
        Get all task and return it into template renderer
        @return task list read from file
        """
        tasks = dict()
        try:
            with open(Resources.FILE_DB["tasks"]) as tasks_file:
                tasks = json.load(tasks_file)
            return tasks["tasks"]
        except IOError as exception:
            utilities.log(
                utilities.logging.ERROR, "Error occurred while getting tasks from database with exception: " +
                exception.message
            )

    def get_users_list(self):
        """
        Get all users and return it into template renderer
        @return task list read from file
        """
        users = dict()
        try:
            with open(Resources.FILE_DB["users"]) as users_file:
                users = json.load(users_file)
            return users["users"]
        except IOError as exception:
            utilities.log(
                utilities.logging.ERROR, "Error occurred while getting users from database with exception: " +
                                         exception.message
            )

    def add_task(self, **kwargs):
        """
        Add provided task into database
        @param kwargs
        @return status code
        """
        status = {"code": 200, "message": ""}
        try:
            # Create a new Task object
            task = Task()

            # Set attributes of new Task
            for key in kwargs:
                task[key] = kwargs[key]

            # Get recent file content as a json
            tasks = self.get_task_list()
            new_tasks = dict()

            with open(Resources.FILE_DB["tasks"], "w+") as tasks_file:
                tasks.append(task)
                new_tasks["tasks"] = tasks
                json.dump(new_tasks, tasks_file)
            status["message"] = "Task successfully added!"
        except IOError as exception:
            utilities.log(
                utilities.logging.CRITICAL, 'Error occurred while adding task with exception: ' + str(exception.message)
            )
            status["code"] = 500
            status["message"] = "Error occurred while adding task. Please contact system administrator"
        finally:
            return status

    def edit_task(self, task_id, **kwargs):
        """
        Edit provided task by given values
        """
        tasks = self.get_task_list()
        new_tasks = dict()
        task_id = unicode(task_id)
        status = {"code": 200, "message": ""}
        try:
            for todo in tasks:
                if task_id == todo["__id"]:
                    todo.update(kwargs)
            new_tasks["tasks"] = tasks
            with open(Resources.FILE_DB["tasks"], "w+") as tasks_file:
                json.dump(new_tasks, tasks_file)
            status["message"] = "Task successfully edited!"
        except BaseException as exception:
            utilities.log(
                utilities.logging.ERROR, "Task with given id could not be updated in database with exception: "
                + exception.message
            )
            status["code"] = 500
            status["message"] = "Task with given id could not be updated in database."
        finally:
            return status

    def remove_task(self, task_id):
        """
        Remove the task which has given id
        """
        tasks = self.get_task_list()
        task_id = unicode(task_id)
        new_tasks = dict()
        status = {"code": 200, "message": ""}
        try:
            new_tasks["tasks"] = [todo for todo in tasks if todo["__id"] != task_id]

            # Write new list into Json file to store data
            with open(Resources.FILE_DB["tasks"], "w+") as tasks_file:
                json.dump(new_tasks, tasks_file)
            status["message"] = "Task successfully deleted!"
        except BaseException as exception:
            utilities.log(
                utilities.logging.ERROR, "Task with given id could not be deleted from database with exception: "
                + exception.message
            )
            status["code"] = 500
            status["message"] = "Task with given id could not be deleted from database."
        finally:
            return status

    def get_task(self, task_id):
        """
        Find and retrieve task from database where id is submitted
        """
        tasks = self.get_task_list()

        # Convert regular string to unicode
        task_id = unicode(task_id)
        try:
            for todo in tasks:
                if task_id == todo["__id"]:
                    return todo
        except BaseException as exception:
            utilities.log(
                utilities.logging.ERROR, "Task with given id could not find in database with exception: "
                + exception.message
            )
            return None


if __name__ == "__main__":
    controller = Controller()
    tasks = controller.get_task_list()
    users = controller.get_users_list()
    task = controller.get_task("e3410a65-8a37-4d34-a26e-f7915e19846b")

    controller.add_task(value="This is my first task to be inserted.",
                        due_date="2013-11-26 12:00",
                        assignee=users[int(random.randint(0,3))]["name"],
                        status="Open")

