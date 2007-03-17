Summary:	Aria2 is a download utility with resuming and segmented downloading
Name:		aria2
Version:	0.10.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/aria2/%{name}-%{version}.tar.bz2
# Source0-md5:	ee56d934d11c70e8d3b778658e5d7d9d
URL:		http://aria2.sourceforge.net/
BuildRequires:	gnutls-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aria2 has segmented downloading engine in its core. It can download
one file from multiple URLs or multiple connections from one URL. This
results in very high speed downloading, very much faster than ordinary
browsers. It can also download BitTorrent files. We implemented this
engine in single-thread model. The architecture is very clean and easy
to extend. It also supports Metalink version 3.0.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang aria2c

%clean
rm -rf $RPM_BUILD_ROOT

%files -f aria2c.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/aria2c
%{_mandir}/man1/*
