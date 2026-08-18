%define major 0
%define libname %mklibname fyaml
%define devname %mklibname fyaml -d

Name:		libfyaml
Version:	0.9.6
Release:	2
Source0:	https://github.com/pantoniou/libfyaml/releases/download/v%{version}/libfyaml-%{version}.tar.gz
Patch0:		libfyaml-sphinx-man-destdir.patch
Summary:	YAML parser and emitter
URL:		https://github.com/pantoniou/libfyaml
License:	MIT
Group:		System/Libraries
BuildRequires:	cmake
BuildRequires:	python%{pyver}dist(linuxdoc)
BuildRequires:	python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(sphinx-rtd-theme)
BuildRequires:	python%{pyver}dist(sphinx-markdown-builder)
BuildRequires:	pkgconfig(check)
BuildSystem:	cmake

%description
YAML parser and emitter

%package -n %{libname}
Summary:	YAML parser and emitter
Group:		System/Libraries

%description -n %{libname}
YAML parser and emitter

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name},
a YAML parser and emitter

%files
%{_bindir}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/*
%{_mandir}/man3/*
