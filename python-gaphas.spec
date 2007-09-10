%define module gaphas
Summary:	Cairo based canvas library
Name:		python-%{module}
Version:	0.3.3
Release:	1
License:	LGPL
Group:		Python/Libraries
Source0:	http://pypi.python.org/packages/source/g/gaphas/%{module}-%{version}.tar.gz
# Source0-md5:	50ab5f156d7de7fb3c66b32fd07078c6
URL:		http://gaphor.devjavu.com/projects/gaphor/wiki/Subprojects/Gaphas
BuildRequires:	python-devel
%pyrequires_eq	python-libs
Requires:	python-pygtk-gtk >= 2.8.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cairo based canvas library.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build
%{__python} setup.py build_doc

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
		--optimize=2 \
		--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO
%doc html/*
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}*egg*
