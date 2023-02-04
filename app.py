import ast
import logging
from stable import run
from flask import Flask, render_template, request, redirect, flash

logger = logging.getLogger(__name__)
app = Flask(__name__)
app.secret_key = "X2JD3JD36BD4SH43BS3H5BX77663"

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        try:
            prompts = list(ast.literal_eval(request.form["prompts"]))
            animation_prompt = dict(ast.literal_eval(request.form["animation_prompt"]))
            max_frames = int(request.form["max_frames"])
            animation_mode = request.form["animation_mode"]
            flash("script run successfully!!!", "success")
            run(prompts, animation_prompt, max_frames, animation_mode)
        except Exception as e:
            logger.error(e)
            flash(str(e) + "(Invalid inputs Passed Try Again!!!)", "danger")
            return redirect('/')
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)