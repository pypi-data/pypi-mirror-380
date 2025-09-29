from .server import mcp

def main():
    mcp.run(transport="stdio")  # 显式 stdio，防止默认传输差异

if __name__ == "__main__":
    main()
