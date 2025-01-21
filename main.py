import server
import uvicorn

if __name__ == '__main__':
    server = server.Server()
    
    # 启动 FastAPI 应用
    uvicorn.run(server.app, host="0.0.0.0", port=8000)