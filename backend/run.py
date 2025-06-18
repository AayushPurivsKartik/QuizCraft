import warnings
warnings.filterwarnings("ignore", category=FutureWarning, module="huggingface_hub.file_download")

from app import create_app, db
from flask_migrate import Migrate
import nltk
import spacy.cli
spacy.cli.download("en_core_web_sm")
nltk.download('wordnet')
nltk.download('omw-1.4')
app = create_app()
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)