{
  pkgs ? import <nixpkgs> { },
  pkgsLinux ? import <nixpkgs> { system = "x86_64-linux"; },
}:

pkgs.dockerTools.buildImage {
  name = "anysearch";
  tag = "latest";
  created = "now";
  copyToRoot = pkgs.buildEnv {
    name = "UV";
    paths = [ pkgs.uv ];
    pathsToLink = [
      "/bin"
      "/lib"
      "/lib64"
      "/share"
    ];
  };
  extraCommands = "ls -a";
  config = {
    Cmd = [
      "${pkgs.uv}/bin/uv"
      "run"
      "python"
      "app.py"
    ];
    WorkingDir = "/app";
  };
}
