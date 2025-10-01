export def main [
  --pyenv-root: string
  --install-dir: string = "/opt/funstall"
  --reinstall
] {
  if (which ls | is-not-empty) and not $reinstall {
    error make { msg: "funstall is already installed and --reinstall was not passed" }
  }
}
