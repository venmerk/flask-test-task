
from app import create_app
# from admin import admin

if __name__ == "__main__":

    app = create_app()
    app.run(debug=True)

    # snippets in need:
    #port = app.config.get("PORT", 5000)
    #app.run(host="0.0.0.0", port=port)


