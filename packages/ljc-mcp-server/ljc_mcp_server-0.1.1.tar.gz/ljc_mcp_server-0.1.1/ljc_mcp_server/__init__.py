from ljc_mcp_server.server import mcp


def main():
    mcp.run(transport='stdio')
    # mcp.run(transport='streamable-http', host="0.0.0.0", port=8001)


if __name__ == "__main__":
    main()
