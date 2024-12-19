from decouple import config
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Lee las variables usando decouple
    debug_mode = config("FLASK_DEBUG", default=False, cast=bool)
    port = config("PORT", default=5000, cast=int)

    # Ejecuta la aplicación
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
