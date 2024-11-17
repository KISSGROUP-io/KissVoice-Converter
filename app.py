from flask import Flask, render_template, request, redirect, send_file, flash, url_for
import os
import ffmpeg
import mimetypes

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024  # 20 Mo

UPLOAD_FOLDER = 'uploads'
CONVERTED_FOLDER = 'converted'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(CONVERTED_FOLDER):
    os.makedirs(CONVERTED_FOLDER)

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def convert_file():
    if 'file' not in request.files:
        flash('Aucun fichier uploadé')
        return redirect(request.url)

    file = request.files['file']
    filename = file.filename.lower()

    # Vérification de l'extension
    if not (filename.endswith('.mp3') or filename.endswith('.wav')):
        flash('Seuls les fichiers MP3 et WAV sont acceptés.')
        return redirect(request.url)

    # Vérification du type MIME
    mime_type, _ = mimetypes.guess_type(filename)
    if mime_type not in ['audio/mpeg', 'audio/wav']:
        flash('Le type de fichier est incorrect.')
        return redirect(request.url)

    if file.filename == '':
        flash('Aucun fichier sélectionné')
        return redirect(request.url)

    if file:
        # Enregistrer le fichier uploadé
        mp3_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(mp3_path)

        # Créer le chemin pour le fichier WAV converti
        wav_filename = os.path.splitext(file.filename)[0] + '.wav'
        wav_path = os.path.join(CONVERTED_FOLDER, wav_filename)

        # Convertir MP3 ou WAV en WAV avec ffmpeg
        ffmpeg.input(mp3_path).output(wav_path, ar=8000, ac=1, sample_fmt='s16').run()

        # Envoyer le fichier WAV à l'utilisateur
        response = send_file(wav_path, as_attachment=True)

        # Supprimer les fichiers MP3/WAV et WAV après le téléchargement
        os.remove(mp3_path)
        os.remove(wav_path)

        return response

@app.errorhandler(413)
def request_entity_too_large(error):
    flash("Le fichier dépasse la limite de 20 Mo.")
    return redirect(url_for('upload_file'))

if __name__ == '__main__':
    app.run(debug=True)
