# Python script maker for linux

## How to run locally?

- Clone this repo with 
```bash
curl https://raw.githubusercontent.com/MihaiBlebea/python-script-maker/master/installer.sh --output installer.sh --silent && chmod +x ./installer.sh && ./installer.sh
```
- To create a new script project, just run this script with 
```bash
scriptmaker <script-name>
```

### How to uninstall from local?

- Option 1 - with the installer file: 
```bash
./installer.sh -u
```

- Option 2 - download the installer and uninstall in one command:
```bash
curl https://raw.githubusercontent.com/MihaiBlebea/python-script-maker/master/installer.sh --output installer.sh --silent && chmod +x ./installer.sh && ./installer.sh -u && rm -rf ./installer.sh
```

- Option 3 - just run this command:
```bash
unlink ${HOME}/.local/bin/scriptmaker && rm -rf ${HOME}/.local/bin/_scriptmaker
```