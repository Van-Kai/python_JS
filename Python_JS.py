def handler():
    try:
        # 运行 Node.js 脚本并捕获输出
        result = subprocess.run(["node", "-e", 'console.log("kaikai")'], capture_output=True, text=True)

        # 检查 Node.js 脚本是否成功执行
        if result.returncode != 0:
            raise Exception(f"Node.js script failed with exit code {result.returncode}")

            # 打印到 Python 日志（如果您在日志查看器中查看）
        print(f"Node.js output: {result.stdout}")

        # 返回 HTTP 响应
        return {
            'statusCode': 200,
            'body': result.stdout
        }
    except Exception as e:
        # 如果有错误，返回 500 状态码和错误信息
        return {
            'statusCode': 500,
            'body': str(e)
        }
handler()
