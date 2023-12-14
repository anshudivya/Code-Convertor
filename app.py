from flask import Flask, render_template, request,jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = "YOUR-API-KEY"


@app.route("/convert", methods=["POST"])
def translate():
    print("in the translate phase")
    if request.method == "POST":
        source_language = request.form.get("source")
        target_language = request.form.get("target")
        code = request.form.get("code")

        prompt = f"Translate this function from {source_language} into {target_language} ### {source_language} \n\n {code} \n\n ### {target_language}"

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt= prompt,
            temperature=0,
            max_tokens=1050,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["###"]
        )

        output = response.choices[0].text
        return jsonify({"output": output})

if __name__ == '__main__':
    app.run()