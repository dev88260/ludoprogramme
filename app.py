from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def ludo(score1):
    import random
    dice = random.randint(1, 6)
    if dice == 6:
        l = random.randint(1, 6)
        score1 += l
        if l == 6:
            ll = random.randint(1, 6)
            score1 += ll
    return score1

def ludo2(score2):
    import random
    dice = random.randint(1, 6)
    if dice == 6:
        l = random.randint(1, 6)
        score2 += l
        if l == 6:
            ll = random.randint(1, 6)
            score2 += ll
    return score2

def ludo3(score3):
    import random
    dice = random.randint(1, 6)
    if dice == 6:
        l = random.randint(1, 6)
        score3 += l
        if l == 6:
            ll = random.randint(1, 6)
            score3 += ll
    return score3

def ludo4(score4):
    import random
    dice = random.randint(1, 6)
    if dice == 6:
        l = random.randint(1, 6)
        score4 += l
        if l == 6:
            ll = random.randint(1, 6)
            score4 += ll
    return score4
@app.route('/play', methods=['GET', 'POST'])
def nihall():
    if request.method == 'POST':
        players = request.form.get('players')

        # Check if players is valid
        if not players or not players.isdigit() or not (1 <= int(players) <= 4):
            return render_template('play.html', error="Please enter a valid number of players (1 to 4)")

        players = int(players)
        scores = [0] * players
        rounds = 5  # Number of rounds

        for i in range(rounds):
            if players >= 1:
                scores[0] = ludo(scores[0])
            if players >= 2:
                scores[1] = ludo2(scores[1])
            if players >= 3:
                scores[2] = ludo3(scores[2])
            if players >= 4:
                scores[3] = ludo4(scores[3])

        winner = scores.index(max(scores)) + 1
        return render_template('result.html', scores=scores, winner=winner)

    return render_template('play.html')
