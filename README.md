# Python script maker for linux

## How to run locally?

Clone and install the application with one script
```
git clone git@github.com:MihaiBlebea/football_updates.git ./football_updates && \
cd ./football_updates && \
chmod +x ./execute.sh && \
./execute.sh install
```

### How to uninstall from local?

Run the installer with the flag `-u`
```
./football_updates/execute.sh install -u && \
rm -rf ./football_updates
```