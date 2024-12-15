from typing import Any
import litserve as ls


class SimpleLitAPI(ls.LitAPI):
    def setup(self, device) -> None:
        print(f"setup at {device}")
    def decode_request(self, request) -> Any:
        return request["input"]

    def predict(self, x) -> dict[str, Any]:
        squared = self.model1(x=x)
        cubed = self.model2(x=x)
        output = squared + cubed
        return {"output": output}

    def encode_response(self, output) -> dict[str, Any]:
        return {"output": output}


if __name__ == "__main__":
    api = SimpleLitAPI()
    server = ls.LitServer(lit_api=api, accelerator="auto")
    server.run(port=8000)
