from typing import Any
# from chain import chain
import litserve as ls


class SimpleLitAPI(ls.LitAPI):
    def setup(self, device) -> None:
        self.model1 = lambda x: x**2
        self.model2 = lambda x: x**3

    def decode_request(self, request):
        return request["input"]

    def predict(self, x) -> dict[str, Any]:
        squared = self.model1(x)
        cubed = self.model2(x)
        output = squared + cubed
        return {"output": output}

    def encode_response(self, output) -> dict[str, Any]:
        return {"output": output}


if __name__ == "__main__":
    api = SimpleLitAPI()
    server = ls.LitServer(api, accelerator="gpu")
    server.run(port=8000)
