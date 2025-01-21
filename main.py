import server
import uvicorn

if __name__ == '__main__':
    server = server.Server()
    
    # 启动 FastAPI 应用
    uvicorn.run(server.app, host="127.0.0.1", port=8000)