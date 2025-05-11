from flask import Flask, render_template, request
import ollama

app = Flask(__name__)
client = ollama.Client()
MODEL = "llama3.2"

@app.route('/', methods=["GET", "POST"])
def home():
    ai_response = None
    
    if request.method == "POST":
        a_city = request.form.get("a_city")
        da_city = request.form.get("da_city")       
        people = request.form.get("people")
        means_of_transport = request.form.get("means_of_transport")
        days = request.form.get("days")
        budget = request.form.get("budget")
        activities = request.form.getlist("activities")
        prompt = (
            f"Voglio visitare {a_city} partendo da {da_city} con {people} persone in {means_of_transport}, in {days} giorni. Crea per me un itinerario."
            f"Il mio budget e {budget} e sono interessato alla seguenti atività: "
            f"{', '.join(activities) if activities else 'varie'}"
        )
        ai_response = client.generate(model=MODEL, prompt=prompt).response

    return render_template("home.html", ai_response=ai_response)

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000)