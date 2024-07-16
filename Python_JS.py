import time
import subprocess
def handler():
    result = subprocess.run(["node", "-e", 'console.log("kaikai")'], capture_output=True, text=True).stdout

    return {
        'statusCode': 200,
        'body': result
    }

    # def main():
    #     while True:
    #         result = subprocess.run(["node", "-e", 'console.log("kaikai")'], capture_output=True, text=True)
    #         print(result.stdout)
    #         time.sleep(1)

