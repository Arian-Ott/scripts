import typer

app = typer.Typer()
import os


def main():
    os.system("apt update && apt upgrade -y >> /dev/null 2>&1")
    lul = {}
    lul["default"] = typer.confirm("Install default? (Curl, net-tools, wget)")
    lul["portainer"] = typer.confirm("Install portainer?")
    lul["docker"] = typer.confirm("Install docker? (compose, engine...)")
    lul["ufw"] = typer.confirm("Install ufw?")
    lul["python"] = typer.confirm("Install python?")
    lul["git"] = typer.confirm("Install git?")
    lul["ssh"] = typer.confirm("Configure SSH keys")
    typer.secho("Config \n"+f"Default: {lul['default']}"
                f"\nPortainer: {lul['portainer']}"
                f"\nDocker: {lul['docker']}"
                f"\nUFW: {lul['ufw']}"
                f"\nPython: {lul['python']}"
                f"\nGit: {lul['git']}"
                f"\nSSH: {lul['ssh']}", color=typer.colors.CYAN)

    typer.confirm("Start installation", abort=True)
    os.system("clear")
    fsad = 0
    for i in lul.values():
        if i:
            fsad += 1
    x = typer.progressbar(length=fsad )

    os.system(f"apt update >> /dev/null 2>&1")
    x.update(1)
    os.system(f"apt upgrade -y >> /dev/null 2>&1")
    x.update(1)
    if lul["default"]:
        os.system(f"apt install curl -y && apt install net-tools -y  && apt install wget -y > /dev/null 2>&1")
        x.update(1)
    if lul["portainer"]:
        lul["docker"] = True

    if lul["docker"]:
        os.system(f"""sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc""")
        x.update(1)
        os.system(f"""echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$UBUNTU_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null""")
        os.system(f""" sudo apt-get update""")
        x.update(1)
        os.system(
            f"""sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y""")
        x.update(1)
    if lul["portainer"]:
        os.system(f"docker volume create portainer_data")
        x.update(1)
        os.system("""docker run -d -p 8000:8000 -p 9443:9443 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest""")
        x.update(1)
    if lul["ufw"]:
        os.system("apt install ufw")
        x.update(1)
        os.system("ufw allow 22")
        x.update(1)
        os.system("ufw allow 80")
        x.update(1)
        os.system("ufw allow 443")
        x.update(1)
        os.system("ufw enable")
        x.update(1)





if __name__ == "__main__":
    main()