%define module gaphas
Summary:	Cairo based canvas library
Summary(pl.UTF-8):	Biblioteka płótna oparta na Cairo
Name:		python-%{module}
Version:	0.3.6
Release:	6
License:	LGPL
Group:		Python/Libraries
Source0:	http://pypi.python.org/packages/source/g/gaphas/%{module}-%{version}.tar.gz
# Source0-md5:	bd103d6ee8afbf8ec7c92e3a363a15a3
URL:		http://gaphor.devjavu.com/projects/gaphor/wiki/Subprojects/Gaphas
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	python-decorator >= 2.2.0
Requires:	python-pycairo >= 1.4.0
Requires:	python-pygtk-gtk >= 2:2.8.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cairo based canvas library.

%description -l pl.UTF-8
Biblioteka płótna oparta na Cairo.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build
%{__python} setup.py build_doc

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog PKG-INFO README.txt state.txt undo.txt
%{py_sitescriptdir}/gaphas
%{py_sitescriptdir}/gaphas*egg*
