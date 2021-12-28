

import dash_uploader as du

from app import app, server

from routes import render_page_content
from pages.home.home_callbacks import *
from pages.page0.page0_callbacks import *

from environment.settings import APP_HOST, APP_PORT, APP_DEBUG, DEV_TOOLS_PROPS_CHECK, UPLOAD_FOLDER_ROOT


if __name__ == "__main__":
    # app.run_server()
    # app.run_server(debug=True, port=8082)
    # app.run_server(
    #     debug=False, host=os.getenv("HOST", "0.0.0.0"), port=os.getenv("PORT", "5000")
    # )

    du.configure_upload(app, UPLOAD_FOLDER_ROOT)

    app.run_server(
        host=APP_HOST,
        port=APP_PORT,
        debug=APP_DEBUG,
        dev_tools_props_check=DEV_TOOLS_PROPS_CHECK
    )