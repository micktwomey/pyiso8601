{ pkgs, ... }:

let
    python-pkg = pkgs.python312;
in {
  packages = [
    pkgs.gh
    pkgs.git
    pkgs.just
    python-pkg
  ];

  languages.python = {
    enable = true;
    package = python-pkg;
    venv.enable = true;
    poetry.enable = true;
    poetry.activate.enable = true;
    poetry.install.enable = true;
    poetry.install.installRootPackage = true;
  };

  # Note: I'm not using devenv's pre-commit support as isn't portable
}
