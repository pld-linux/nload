Summary:	A console application which monitors network traffic and bandwidth usage in real time
Summary(pl):	Konsolowa aplikacja monitoruj±ca ruch w sieci w czasie rzeczywistym
Name:		nload
Version:	0.3.2
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Url:		http://www.roland-riegel.de/nload/index_en.html
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

%build
CFLAGS="%{rpmcflags}"\
	CXXFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"\
	./configure\
		--prefix=%{_prefix}\
		--mandir=%{_mandir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog AUTHORS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
