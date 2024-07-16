import time
import subprocess
from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def hello():
    result = subprocess.run(["node", "-e", 'console.log("kaikai")'], capture_output=True, text=True)
    return result.stdout
 
if __name__ == '__main__':
    app.run()
    # def main():
    #     while True:
    #         result = subprocess.run(["node", "-e", 'console.log("kaikai")'], capture_output=True, text=True)
    #         print(result.stdout)
    #         time.sleep(1)

