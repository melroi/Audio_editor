from flask import Flask, render_template, request, send_file
from flask_uploads import UploadSet, configure_uploads, AUDIO

app = Flask(__name__)
app.config['UPLOADED_FILES_DEST'] = 'uploads'  # Dossier où les fichiers uploadés seront stockés
files = UploadSet('files', AUDIO)
configure_uploads(app, files)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script', methods=['POST'])
def run_script():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        if audio_file and files.is_allowed(audio_file.filename):
            # Enregistrez le fichier audio
            filename = files.save(audio_file)
            
            # Exécutez votre script Python sur le fichier (votre_script.py)
            # Cela pourrait impliquer le traitement du fichier audio
            
            return render_template('index.html', modification_done=True, filename=filename)

    return render_template('index.html', modification_done=False)

@app.route('/download_modified_file/<filename>')
def download_modified_file(filename):
    # Chemin vers le fichier modifié
    modified_file_path = f"uploads/{filename}"
    return send_file(modified_file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
