from flask import Flask, render_template, abort

app = Flask(__name__)

# Hardcoded news by category
news_data = {
    "technology": [
        "AI is transforming the tech industry.",
        "New smartphone released with innovative features.",
        "Cybersecurity threats on the rise globally."
    ],
    "sports": [
        "Local team wins championship after 10 years.",
        "Olympics 2024 preparations in full swing.",
        "Star player suffers injury during match."
    ],
    "entertainment": [
        "Blockbuster movie breaks box office records.",
        "Famous singer releases new album.",
        "Awards ceremony highlights best performances."
    ]
}

@app.route('/news/<category>')
def news(category):
    category = category.lower()
    articles = news_data.get(category)
    if not articles:
        abort(404)
    return render_template('news.html', category=category.title(), articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
