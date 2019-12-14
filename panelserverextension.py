from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the app.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "Airbnb_Price_Prediction.ipynb", "--allow-websocket-origin=*"])