from flask import Flask, request, jsonify
from career_suggestions import career_suggestions

app = Flask(__name__)

@app.route('/predict_career/', methods=['GET'])
def predict_career():
    try:
        openness = int(request.args.get('openness'))
        conscientiousness = int(request.args.get('conscientiousness'))
        extraversion = int(request.args.get('extraversion'))
        agreeableness = int(request.args.get('agreeableness'))
        neuroticism = int(request.args.get('neuroticism'))

        personality_scores = {
            "O": openness,
            "C": conscientiousness,
            "E": extraversion,
            "A": agreeableness,
            "N": neuroticism
        }

        dominant_traits = [trait for trait, score in personality_scores.items() if score == 2]

        if not dominant_traits:
            return jsonify({"error": "No dominant traits were selected. At least one trait should be scored as 1."}), 400

        result = {trait: career_suggestions[trait] for trait in dominant_traits}
        
        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
