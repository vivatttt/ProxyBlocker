from mitmproxy import http


REDIRECT_URL = "http://localhost:8000/"
sites_to_block = set()

def request(flow: http.HTTPFlow) -> None:
    
    global sites_to_block
    
    if flow.request.method == "POST" and flow.request.host == "localhost":
        sites_to_block = set(flow.request.get_text().split())
        
    host = flow.request.host
    print(sites_to_block)
    if host in sites_to_block:
        flow.response = http.Response.make(
            301,  
            b"",  
            {"Location": REDIRECT_URL}  
        )


if __name__ == "__main__":
    from mitmproxy.tools.main import mitmdump
    mitmdump(['-s', __file__])
