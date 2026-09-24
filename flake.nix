{
  description = "A flake for a python environment.";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { self, nixpkgs }:
    let
      system = "x86_64-linux"; # Adjust if needed
      pkgs = import nixpkgs {
        system = system;
        config.allowUnfree = true;
      };
    in
    {
      devShells.${system}.default = pkgs.mkShell rec {
        buildInputs = with pkgs; [
          python3
          (python3.withPackages (
            ps: with ps; [
              pyyaml
              streamlit
            ]
          ))
        ];

        shellHook = ''
          unset SOURCE_DATE_EPOCH
        '';
      };
    };
}
