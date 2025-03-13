from flask import Blueprint, render_template, request, redirect, url_for

crypto = Blueprint('crypto', __name__)

# Caesar cipher encryption logic
def caesar_encrypt(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

@crypto.route('/caesar', methods=['GET', 'POST'])
def caesar_learning():
    result = None
    if request.method == 'POST':
        plaintext = request.form.get('plaintext')
        shift = int(request.form.get('shift'))
        result = caesar_encrypt(plaintext, shift)
    return render_template('crypto/caesar_learning.html', result=result)

@crypto.route('/caesar/quiz', methods=['POST'])
def caesar_quiz():
    score = 0
    q1 = request.form.get('q1')
    q2 = request.form.get('q2')

    if q1 == 'Substitution':
        score += 1
    if q2 == 'BCD':
        score += 1

    return render_template('crypto/caesar_learning.html', quiz_score=score)
