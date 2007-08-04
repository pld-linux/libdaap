Summary:	Digital Audio Access Protocol library
Summary(pl.UTF-8):	Biblioteka obsługująca Digital Audio Access Protocol
Name:		libdaap
Version:	0.0.4
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/daap/%{name}-%{version}.tar.bz2
# Source0-md5:	94f830735fc619a09a57dc51e70e67a9
URL:		http://daap.sourceforge.net/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Digital Audio Access Protocol, or DAAP, is used by Apple's iTunes
4.0 digital audio player to share music across a network or the
Internet. It provides capability not only to stream audio from one
computer to another, but also to list the host's playlists so that
they can be accessed remotely.

%description -l pl.UTF-8
Digital Audio Access Protocol (DAAP) jest używany przez odtwarzacz
muzyki iTunes 4.0 firmy Apple do współdzielenia muzyki w sieci lub
Intenecie. Daje możliwość nie tylko przesyłania strumienia dźwięku z
jednego komputera na inny, ale także przekazywania playlist z
komputera w taki sposób, że mogą być wykorzystywane zdalnie.

%package devel
Summary:	Header files for DAAP library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki DAAP
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for DAAP library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki DAAP.

%package static
Summary:	Static DAAP library
Summary(pl.UTF-8):	Statyczna biblioteka DAAP
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static DAAP library.

%description static -l pl.UTF-8
Statyczna biblioteka DAAP.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libdaap.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdaap.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdaap.so
%{_libdir}/libdaap.la
%{_includedir}/libdaap

%files static
%defattr(644,root,root,755)
%{_libdir}/libdaap.a
