from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP()
count = 0

@mcp.tool
def get_current_time():
    t = datetime.now()
    print('heihei, it is' + str(t))
    global count
    s = ("你好啊我的第%d位朋友，现在时刻" + str(t) )% count
    count += 1
    return s

def main():
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8886, path="/mcp")

if __name__ == "__main__":
    main()