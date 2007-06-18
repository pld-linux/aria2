Summary:	Aria2 is a download utility with resuming and segmented downloading
Summary(pl.UTF-8):	Narzędzie do pobierania plików z obsługą wznawiania i pobierania segmentowego
Name:		aria2
Version:	0.11.0
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/aria2/%{name}-%{version}.tar.bz2
# Source0-md5:	4d0274d53401360689598815de72e7fe
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

%description -l pl.UTF-8
Aria2 wykorzystuje silnik pobierania segmentowego. Może pobierać
jeden plik z kilku adresów lub użyć wielu połączeń do jednego
serwera. W rezultacie pobieranie jest bardzo szybkie, znacznie
szybsze niż w przypadku standardowej przeglądarki WWW. Silnik ten
zaimplementowany jest w modelu jednowątkowym. Aria2 charakteryzuje
się bardzo prostą i rozszerzalną architekturą, która obsługuje także
pliki BitTorrent oraz MetaLink w wersji 3.0.

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
