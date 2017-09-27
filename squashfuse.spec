Name:     squashfuse
Version:  0.1.100
Release:  1%{?dist}
Summary:  FUSE filesystem to mount squashfs archives

License:  BSD
URL:      https://github.com/vasi/squashfuse
Source0:  https://github.com/vasi/squashfuse/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires: autoconf, automake, fuse-devel, gcc, libattr-devel, lz4-devel, xz-devel, zlib-devel

%description
Squashfuse lets you mount SquashFS archives in user-space. It supports almost
all features of the SquashFS format, yet is still fast and memory-efficient.
SquashFS is an efficiently compressed, read-only storage format. Support for it
has been built into the Linux kernel since 2009. It is very common on Live CDs
and embedded Linux distributions.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license LICENSE
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Sep 25 2017 Kyle Fazzari <kyrofa@ubuntu.com> - 0.1.100-1
- Initial version of the package
