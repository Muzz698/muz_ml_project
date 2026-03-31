from flask import Flask, render_template, request

application = Flask(__name__, template_folder="src/templates")

@application.route("/", methods=["GET", "POST"])
def index():
    results = None
    if request.method == "POST":
        try:
            # Get form values
            gender = request.form.get("gender")
            ethnicity = request.form.get("ethnicity")
            parent_edu = request.form.get("parent_edu")
            lunch = request.form.get("lunch")
            test_course = request.form.get("test_course")
            writing_score = float(request.form.get("writing_score", 0))
            reading_score = float(request.form.get("reading_score", 0))

            # Example prediction logic: average of scores
            results = (writing_score + reading_score) / 2

            # Later you can replace above logic with your ML model prediction

        except Exception as e:
            results = f"Error: {e}"

    return render_template("home.html", results=results)

if __name__ == "__main__":
    application.run(debug=True, host="0.0.0.0", port=9000)