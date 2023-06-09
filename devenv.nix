{ pkgs, ... }:

{
  packages = [
    pkgs.git
    pkgs.python38
    pkgs.python39
    pkgs.python310
    pkgs.python311
    pkgs.python312
  ];

  enterShell = ''
    git --version
    # type -a python
    python --version
    poetry install
  '';

  languages.python = {
    enable = true;
    package = pkgs.python311;
    poetry.enable = true;
    poetry.package = pkgs.poetry;
    venv.enable = true;
  };

  # Note: I'm not using devenv's pre-commit support as isn't portable
}
