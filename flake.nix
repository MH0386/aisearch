{
  description = "A very basic flake";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux";
    in
    {
      packages.${system}.default = {
         nixpkgs.dockerTools.buildImage {
          name = "anysearch";
          tag = "latest";
          created = "now";
          copyToRoot = nixpkgs.buildEnv {
            name = "UV";
            paths = [ nixpkgs.uv ];
            pathsToLink = [ "/bin" ];
          };
          runAsRoot = "${nixpkgs.uv}/bin/uv sync";
          config = {
            Cmd = [
              "${nixpkgs.uv}/bin/uv"
              "run"
              "python"
              "app.py"
            ];
          };
        };
    };
}
