from flask import Flask, jsonify, json, render_template
import json

app = Flask(__name__)

app.config.update(DEBUG=True)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/json')
def get_json():
	d = {'a':'b','alessio':'civitillo'}
	return jsonify(a='d')

if __name__=='__main__':
	app.run()
