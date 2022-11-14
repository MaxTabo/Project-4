from flask import Flask, request, jsonify
import numpy as np
import markdown.extensions.fenced_code
import tools.sql_queries as tools
from nltk.sentiment.vader import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()


app = Flask(__name__)


@app.route("/")
def readme ():
    readme_file = open("README.md", "r")
    return markdown.markdown(readme_file.read(), extensions = ["fenced_code"])


@app.route("/sql/")
def sql ():
    return jsonify(tools.get_everything())

@app.route("/compound/<name>")
def get_compound (name):
    return jsonify(tools.get_compound(name))






@app.route("/text/<name>/" )
def get_text (name):
   
    
    return jsonify(tools.get_just_text(name))





    ####### POST



@app.route("/insertrow", methods=["POST"])
def try_post ():
    
    my_params = request.args
    compound = my_params["compound"]
    name = my_params["name"]
    text = my_params["text"]

    
    tools.insert_one_row(name,text,compound)
    return f"YOU ARE A POST MASTER!"


    ####### DELETE


@app.route("/delete_row", methods=["DELETE"])
def delete_row ():
    
    my_params = request.args
    name = my_params["name"]    
    tools.delete_row(name)
    return f"YOU ARE A POST MASTER!"




if __name__ == "__main__":
    app.run(port=9000, debug=True)