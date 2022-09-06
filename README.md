# packageScout
Parses /var/lib/dpkg/status (and/or any other needed files) and displays a list of packages explicitly installed by the user

# Environment
### Build
`docker build -t packagescout .`

### Run Container
`docker run packagescout`

### Enter Shell in Interactive Container Environment
`docker run -it packagescout /bin/bash`
