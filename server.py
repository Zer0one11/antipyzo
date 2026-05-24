import os
from flask import Flask, jsonify, render_template
import config

# Явно указываем Flask, где искать папку static относительно этого файла
current_dir = os.path.dirname(os.path.abspath(__file__))

server = Flask(
    __name__,
    static_folder=os.path.join(current_dir, 'static'),
    static_url_path='/static'
)

# --- РОУТЫ ДЛЯ СТАТИКИ (чтобы не менять index.html) ---

@server.route('/')
def index():
    # Отдаем index.html напрямую из папки static
    return server.send_static_file('index.html')

@server.route('/style.css')
def style_css():
    return server.send_static_file('style.css')

@server.route('/app.js')
def app_js():
    return server.send_static_file('app.js')

# Если у тебя есть папка assets внутри static, этот роут отдаст файлы оттуда
@server.route('/assets/<path:filename>')
def serve_assets(filename):
    return server.send_static_file(f'assets/{filename}')


# --- ТВОИ ОСТАЛЬНЫЕ API РОУТЫ (пример) ---

@server.route('/api/config')
def get_config():
    # Пример использования твоего модуля config
    return jsonify({"status": "ok", "project": "Antilose"})


# Точка входа для локального запуска (Vercel игнорирует этот блок)
if __name__ == '__main__':
    server.run(debug=True)
    
