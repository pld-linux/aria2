#
# Conditional build:
%bcond_with	openssl	# OpenSSL instead of GnuTLS
%bcond_with	libuv	# libuv usage

Summary:	Aria2 is a download utility with resuming and segmented downloading
Summary(pl.UTF-8):	Narzędzie do pobierania plików z obsługą wznawiania i pobierania segmentowego
Name:		aria2
Version:	1.35.0
Release:	2
License:	GPL v2+ with OpenSSL exception
Group:		Applications/Networking
#Source0Download: https://github.com/aria2/aria2/releases
Source0:	https://github.com/aria2/aria2/releases/download/release-1.35.0/%{name}-%{version}.tar.gz
# Source0-md5:	6057c91559a3e82e44a89689944b5d0c
URL:		https://aria2.github.io/
BuildRequires:	c-ares-devel >= 1.7.0
BuildRequires:	cppunit-devel >= 1.10.2
%{!?with_openssl:BuildRequires:	gmp-devel}
%{!?with_openssl:BuildRequires:	gnutls-devel >= 2.2.0}
BuildRequires:	libssh2-devel
BuildRequires:	libstdc++-devel >= 6:4.8.3
%{?with_libuv:BuildRequires:	libuv-devel >= 1.13}
BuildRequires:	libxml2-devel >= 1:2.6.24
%{?with_openssl:BuildRequires:	openssl-devel >= 0.9.8}
%{!?with_openssl:BuildRequires:	nettle-devel}
BuildRequires:	pkgconfig >= 1:0.20
BuildRequires:	rpmbuild(macros) >= 1.673
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	zlib-devel >= 1.2.3
Requires:	c-ares >= 1.7.0
%{!?with_openssl:Requires:	gnutls >= 2.2.0}
%{?with_libuv:Requires:	libuv >= 1.13}
Requires:	libxml2 >= 1:2.6.24
%{?with_openssl:Requires:	openssl >= 0.9.8}
Requires:	zlib >= 1.2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aria2 has segmented downloading engine in its core. It can download
one file from multiple URLs or multiple connections from one URL. This
results in very high speed downloading, very much faster than ordinary
browsers. It can also download BitTorrent files. We implemented this
engine in single-thread model. The architecture is very clean and easy
to extend. It also supports Metalink version 3.0.

%description -l pl.UTF-8
Aria2 wykorzystuje silnik pobierania segmentowego. Może pobierać jeden
plik z kilku adresów lub użyć wielu połączeń do jednego serwera. W
rezultacie pobieranie jest bardzo szybkie, znacznie szybsze niż w
przypadku standardowej przeglądarki WWW. Silnik ten zaimplementowany
jest w modelu jednowątkowym. Aria2 charakteryzuje się bardzo prostą i
rozszerzalną architekturą, która obsługuje także pliki BitTorrent oraz
MetaLink w wersji 3.0.

%package -n bash-completion-aria2
Summary:	Bash completion for aria2c command
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów programu aria2c
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0
BuildArch:	noarch

%description -n bash-completion-aria2
Bash completion for aria2 commands.

%description -n bash-completion-aria2 -l pl.UTF-8
Bashowe dopełnianie parametrów poleceń aria2.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{?with_openssl:--without-gnutls} \
	%{?with_libuv:--with-libuv}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{bash_compdir}
cp -p doc/bash_completion/aria2c $RPM_BUILD_ROOT%{bash_compdir}

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/aria2

%find_lang aria2

%clean
rm -rf $RPM_BUILD_ROOT

%files -f aria2.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE.OpenSSL NEWS README.rst doc/xmlrpc
%attr(755,root,root) %{_bindir}/aria2c
%{_mandir}/man1/aria2c.1*
%lang(pt) %{_mandir}/pt/man1/aria2c.1*
%lang(ru) %{_mandir}/ru/man1/aria2c.1*

%files -n bash-completion-aria2
%defattr(644,root,root,755)
%{bash_compdir}/aria2c
