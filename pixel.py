from flask import Flask, request, send_file
import logging

app = Flask(__name__)

@app.route('/tracking_pixel')
def tracking_pixel():
    # Log the request details
    app.logger.info(f"Tracked request: {request.remote_addr}, User-Agent: {request.headers.get('User-Agent')}")
    
    # Send a 1x1 pixel GIF
    return send_file('pixel.gif', mimetype='image/gif')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)

# How tracking_pixel is called when a client loads website content
# <img src="http://pixelserver.com/tracking_pixel" width="1" height="1" alt="" />
