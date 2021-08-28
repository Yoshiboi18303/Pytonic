from flask import Flask
app = Flask('app')

def website(client_name, tagline, host, port):
  client_name = str(client_name)
  tagline = str(tagline)
  host_address = str(host)
  port = int(port)
  @app.route('/')
  def main_page():
    return f'{client_name} | {tagline}'
  @app.route('/info')
  def info_page():
    return f'Coming soon!'
  app.run(host=host_address, port=port)