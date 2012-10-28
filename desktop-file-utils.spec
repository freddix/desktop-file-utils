Summary:	A couple of command line utilities for working with desktop entries
Name:		desktop-file-utils
Version:	0.21
Release:	1
License:	GPL
Group:		Applications
Source0:	http://freedesktop.org/software/desktop-file-utils/releases/%{name}-%{version}.tar.xz
# Source0-md5:	fda5c312c9fb3b8d818fb54f2c34db82
URL:		http://www.freedesktop.org/wiki/Software_2fdesktop_2dfile_2dutils
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
desktop-file-utils contains a couple of command line utilities for
working with desktop entries.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/desktop-file-install.1*
%{_mandir}/man1/desktop-file-validate.1*
%{_mandir}/man1/update-desktop-database.1*

