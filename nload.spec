Summary:	A console application which monitors network traffic and bandwidth usage in real time
Summary(pl):	Konsolowa aplikacja monitoruj±ca ruch w sieci w czasie rzeczywistym
Name:		nload
Version:	0.6.0
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	a8859e49176bb50826b52b8345b117d3
Patch0:		%{name}-form_field_h.patch
URL:		http://www.roland-riegel.de/nload/index_en.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nload is a console application which monitors network traffic and
bandwidth usage in real time. It visualizes the in- and outgoing
traffic using two graphs and provides additionally info like total
amount of transfered data and min/max network usage.

%description -l pl
nload jest konsolow± aplikacj± monitoruj±c± w czasie rzeczywistym ruch
pakietów i obci±¿enie sieci. Obrazuje ruch z i do za pomoc± dwóch
wykresów i udostêpnia dodatkowe informacje takie jak ca³kowita ilo¶æ
przes³anych danych oraz minimalne/maksymalne wykorzystanie pasma.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -I%{_includedir}/ncurses"
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
