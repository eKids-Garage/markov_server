# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_render_template]
import datetime
import json
from flask import Flask, render_template, request, jsonify 
from data import store_solution
from interpreter import interpret, parse_line


app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')

@app.route('/help')
def help():
    return render_template('help.html')

@app.route('/start-program', methods = ['POST'])
def start_program():
    if request.method == 'POST':
        initial_word = json.loads(request.form['message'])['initial_word']
        program_lines = json.loads(request.form['message'])['program']
        team = json.loads(request.form['message'])['team']
        task = json.loads(request.form['message'])['task']
                
        program = []
        for l in program_lines:
            program.append((l['in'], l['out'], l['stop']))
            
        # jsonify(interpret(initial_word, program, True))
        # store_solution('test-team', 'test-task', program_lines)
        return render_template('index.html', response = interpret(initial_word, program, True))
    else: 
        return "Oops"


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=5000, debug=True)
# [START gae_python37_render_template]
