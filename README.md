# packageScout
Parses /var/lib/dpkg/status (and/or any other needed files) and displays a list of packages explicitly installed by the user

# Environment
### Build
`docker build -t packagescout .`

### Run Container
`docker run packagescout`

### Enter Shell in Interactive Container Environment
`docker run -it packagescout /bin/bash`


### Build Python Package
`python3 -m build` (run in base directory where `pyproject.toml` is located)

# Rules Observed
- No `source` field
- `Priority: Optional`


# Samples from /var/lib/dpkg/status
```
Package: git
Status: install ok installed
Priority: optional
Section: vcs
Installed-Size: 31552
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: amd64
Multi-Arch: foreign
Version: 1:2.17.1-1ubuntu0.12
Replaces: git-core (<< 1:1.7.0.4-1.), gitweb (<< 1:1.7.4~rc1)
Provides: git-completion, git-core
Depends: libc6 (>= 2.16), libcurl3-gnutls (>= 7.16.2), libexpat1 (>= 2.0.1), libpcre3, zlib1g (>= 1:1.2.0), perl, liberror-perl, git-man (>> 1:2.17.1), git-man (<< 1:2.17.1-.)
Recommends: patch, less, ssh-client
Suggests: gettext-base, git-daemon-run | git-daemon-sysvinit, git-doc, git-el, git-email, git-gui, gitk, gitweb, git-cvs, git-mediawiki, git-svn
Breaks: bash-completion (<< 1:1.90-1), cogito (<= 0.18.2+), git-buildpackage (<< 0.6.5), git-core (<< 1:1.7.0.4-1.), gitosis (<< 0.2+20090917-7), gitpkg (<< 0.15), gitweb (<< 1:1.7.4~rc1), guilt (<< 0.33), openssh-client (<< 1:6.8), stgit (<< 0.15), stgit-contrib (<< 0.15)
Conffiles:
 /etc/bash_completion.d/git-prompt 7baac5c3ced94ebf2c0e1dde65c3b1a6
Description: fast, scalable, distributed revision control system
 Git is popular version control system designed to handle very large
 projects with speed and efficiency; it is used for many high profile
 open source projects, most notably the Linux kernel.
 .
 Git falls in the category of distributed source code management tools.
 Every Git working directory is a full-fledged repository with full
 revision tracking capabilities, not dependent on network access or a
 central server.
 .
 This package provides the git main components with minimal dependencies.
 Additional functionality, e.g. a graphical user interface and revision
 tree visualizer, tools for interoperating with other VCS's, or a web
 interface, is provided as separate git* packages.
Homepage: https://git-scm.com/
Original-Maintainer: Gerrit Pape <pape@smarden.org>
```

```
Package: vim
Status: install ok installed
Priority: optional
Section: editors
Installed-Size: 2790
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: amd64
Version: 2:8.0.1453-1ubuntu1.8
Provides: editor
Depends: vim-common (= 2:8.0.1453-1ubuntu1.8), vim-runtime (= 2:8.0.1453-1ubuntu1.8), libacl1 (>= 2.2.51-8), libc6 (>= 2.15), libgpm2 (>= 1.20.7), libpython3.6 (>= 3.6.5), libselinux1 (>= 1.32), libtinfo5 (>= 6)
Suggests: ctags, vim-doc, vim-scripts
Description: Vi IMproved - enhanced vi editor
 Vim is an almost compatible version of the UNIX editor Vi.
 .
 Many new features have been added: multi level undo, syntax
 highlighting, command line history, on-line help, filename
 completion, block operations, folding, Unicode support, etc.
 .
 This package contains a version of vim compiled with a rather
 standard set of features.  This package does not provide a GUI
 version of Vim.  See the other vim-* packages if you need more
 (or less).
Homepage: https://vim.sourceforge.io/
Original-Maintainer: Debian Vim Maintainers <pkg-vim-maintainers@lists.alioth.debian.org>
```

```
Package: liberror-perl
Status: install ok installed
Priority: optional
Section: perl
Installed-Size: 62
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: all
Version: 0.17025-1
Depends: perl
Description: Perl module for error/exception handling in an OO-ish way
 The Error module provides two interfaces.  Firstly "Error" provides a
 procedural interface to exception handling. Secondly "Error" is a base class
 for errors/exceptions that can either be thrown, for subsequent catch, or can
 simply be recorded.
 .
 Errors in the class "Error" should not be thrown directly, but the user
 should throw errors from a sub-class of "Error".
 .
 Warning: Using the "Error" module is no longer recommended due to the
 black-magical nature of its syntactic sugar, which often tends to break. Its
 maintainers have stopped actively writing code that uses it, and discourage
 people from doing so.
 .
 Recommended alternatives are Exception::Class (libexception-class-perl),
 Error::Exception (not packaged), TryCatch (libtrycatch-perl), and Try::Tiny
 (libtry-tiny-perl).
Original-Maintainer: Debian Perl Group <pkg-perl-maintainers@lists.alioth.debian.org>
Homepage: https://metacpan.org/release/Error
```

```
Package: vim-common
Status: install ok installed
Priority: important
Section: editors
Installed-Size: 330
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: all
Source: vim
Version: 2:8.0.1453-1ubuntu1.8
Depends: xxd
Recommends: vim | vim-gtk | vim-gtk3 | vim-athena | vim-nox | vim-tiny
Conffiles:
 /etc/vim/vimrc 8a8f58567e1a68b71d61164a4e039fdc
Description: Vi IMproved - Common files
 Vim is an almost compatible version of the UNIX editor Vi.
 .
 This package contains files shared by all non GUI-enabled vim variants
 available in Debian.  Examples of such shared files are: manpages and
 configuration files.
Homepage: https://vim.sourceforge.io/
Original-Maintainer: Debian Vim Maintainers <pkg-vim-maintainers@lists.alioth.debian.org>
```

```
Package: libsqlite3-0
Status: install ok installed
Priority: standard
Section: libs
Installed-Size: 1182
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Architecture: amd64
Multi-Arch: same
Source: sqlite3
Version: 3.22.0-1ubuntu0.5
Depends: libc6 (>= 2.14)
Description: SQLite 3 shared library
 SQLite is a C library that implements an SQL database engine.
 Programs that link with the SQLite library can have SQL database
 access without running a separate RDBMS process.
Homepage: http://www.sqlite.org/
Original-Maintainer: Laszlo Boszormenyi (GCS) <gcs@debian.org>
```

## Failing exceptions related to Git
- liberror-perl
- xauth
- publicsuffix
- openssl
- ca-certificates
