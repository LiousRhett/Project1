import os

from app import create_app

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# 运行 Flask 应用
if __name__ == "__main__":
    print("Successfully Run")    
    app.run(debug=True)