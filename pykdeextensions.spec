# TODO:
# - optflags
# - split to devel static examples packages
# - fix KDE HTML docs packaging
Summary:	Collection of software and Python packages to support the creation and installation of KDE applications
Summary(pl.UTF-8):	Zbiór oprogramowania i pakietów Pythona wspierających tworzenie i instalację aplikacji KDE
Name:		pykdeextensions
Version:	0.4.0
Release:	0.2
License:	GPL
Group:		Development/Languages/Python
Source0:	http://www.simonzone.com/software/pykdeextensions/%{name}-%{version}.tar.gz
# Source0-md5:	5249c7288c1b2bed44a2d91111d3313a
URL:		http://www.simonzone.com/software/pykdeextensions/#introduction
BuildRequires:	python-PyKDE
BuildRequires:	python-devel
BuildRequires:	python-modules >= 2.2.1
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyKDE Extensions is a collection of software and Python packages to
support the creation and installation of KDE applications.

%description -l pl.UTF-8
PyKDE Extensions jest zbiorem oprogramowania i pakietów Pythona
wspierających tworzenie i instalację aplikacji KDE.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_mandir}/man1}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{py_sitescriptdir}/*.py[co]
# app_templates -> examples / docs ?
%{_datadir}/apps/%{name}

#%files devel
#%defattr(644,root,root,755)
#%doc devel-doc/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/pythonize.h
%{_libdir}/lib*.la

#%files static
#%defattr(644,root,root,755)
%{_libdir}/lib*.a
