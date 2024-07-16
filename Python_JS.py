import time
import subprocess
while True:

    result = subprocess.run(["node", "-e", 'console.log("kaikai")'], capture_output=True, text=True)
    print(result.stdout)
    time.sleep(1)

