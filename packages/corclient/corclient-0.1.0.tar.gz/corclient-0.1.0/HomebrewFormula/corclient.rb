class Corclient < Formula
  include Language::Python::Virtualenv

  desc "Internal CLI tool for microservices management and infrastructure administration"
  homepage "https://github.com/ProjectCORTeam/corcli"
  url "https://files.pythonhosted.org/packages/source/c/corclient/corclient-VERSION.tar.gz"
  sha256 "SHA256_HASH"
  license "MIT"

  depends_on "python@3.11"

  resource "typer" do
    url "https://files.pythonhosted.org/packages/source/t/typer/typer-0.12.0.tar.gz"
    sha256 "TODO: Add actual hash"
  end

  resource "rich" do
    url "https://files.pythonhosted.org/packages/source/r/rich/rich-13.7.0.tar.gz"
    sha256 "TODO: Add actual hash"
  end

  resource "flask" do
    url "https://files.pythonhosted.org/packages/source/f/flask/flask-3.0.0.tar.gz"
    sha256 "TODO: Add actual hash"
  end

  resource "requests" do
    url "https://files.pythonhosted.org/packages/source/r/requests/requests-2.31.0.tar.gz"
    sha256 "TODO: Add actual hash"
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "CoreCLI", shell_output("#{bin}/cor --help")
  end
end
