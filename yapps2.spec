%if 0%{?el5}
%define python python26
%define __python /usr/bin/python2.6
%{!?python_scriptarch: %define python_scriptarch %(%{__python} -c "from distutils.sysconfig import get_python_lib; from os.path import join; print join(get_python_lib(1, 1), 'scripts')")}
%else
%define python python
%define __python /usr/bin/python
%endif
%{!?_python_sitelib: %define _python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define project_name yapps2
%define project_version 2.1.1
%define project_release logilab
%define project_url http://theory.stanford.edu/~amitp/yapps/
%define project_summary Yet Another Python Parser System

Summary: %{project_summary}
Name: %{python}-%{project_name}
Version: %{project_version}
Release: %{project_release}%{?dist}
Source0: http://ftp.logilab.org/pub/yapps/%{project_name}-%{version}.zip
License: LGPLv2+
Group: Development/Languages/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Logilab <contact@logilab.fr>
Packager: Pierre GM <pierre.gerard-marchant@logilab.fr>
Url: %{project_url}
Requires: %{python}
BuildRequires: %{python}


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
%setup -c
%if 0%{?el5}
# change the python version in shebangs
find . -name '*.py' -type f -print0 |  xargs -0 sed -i '1,3s;^#!.*python.*$;#! /usr/bin/python2.6;'
%endif


%install
NO_SETUPTOOLS=1 %{__python} setup.py --quiet install --no-compile --prefix=%{_prefix} --root="$RPM_BUILD_ROOT" %{?python_scriptarch: --install-scripts=%{python_scriptarch}}


%{__python} setup.py --quiet install --no-compile --prefix=%{_prefix} --root="$RPM_BUILD_ROOT" --install-scripts=%{python_scriptarch}
# change the python version in scripts
find %{python_scriptarch}|while read f; do sed -i 's/^\(#!.*python\)/%{python}/' "$f";done

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-, root, root)
%{_python_sitelib}/*
