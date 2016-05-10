%if 0%{?el5}
%define python python26
%define __python /usr/bin/python2.6
%{!?python_scriptarch: %define python_scriptarch %(%{__python} -c "from distutils.sysconfig import get_python_lib; from os.path import join; print join(get_python_lib(1, 1), 'scripts')")}
%else
%define python python
%define __python /usr/bin/python
%endif

Summary:        Yet Another Python Parser System
Name:           %{python}-yapps2
Version:        2.2.0
Release:        logilab.1%{?dist}
Source0:        http://download.logilab.org/pub/yapps/yapps2-%{version}.zip
License:        LGPLv2+
Group:          Development/Languages/Python
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:      noarch
Vendor:         Logilab <contact@logilab.fr>
Url:            https://github.com/smurfix/yapps
Requires:       %{python}
Requires:       %{python}-setuptools
BuildRequires:  %{python}
BuildRequires:  %{python}-setuptools

%description
YAPPS is an easy to use parser generator that is written in Python and
generates Python code.  There are several parser generator systems
already available for Python, but this parser has different goals:
Yapps is simple, very easy to use, and produces human-readable parsers.

It is not the fastest or most powerful parser.  Yapps is designed to be
used when regular expressions are not enough and other parser systems
are too much: situations where you might otherwise write your own
recursive descent parser.

This package contains several upward-compatible enhancements to the
original YAPPS source:
- Handle stacked input ("include files")
- augmented ignore-able patterns (can parse multi-line C comments correctly)
- better error reporting
- read input incrementally

%prep
%setup -q -n yapps2-%{version}

%build
%{__python} setup.py build
%if 0%{?el5}
# change the python version in shebangs
find . -name '*.py' -type f -print0 |  xargs -0 sed -i '1,3s;^#!.*python.*$;#! /usr/bin/python2.6;'
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT %{?python_scriptarch: --install-scripts=%{python_scriptarch}}

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, root)
/*

