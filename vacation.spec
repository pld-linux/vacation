Summary:	Automatic mail answering program for Linux
Name:		vacation
Version:	1.2.1
Release:	1
License:	GPL
Group:		Applications/Mail
URL:		http://www.tcob1.uklinux.net/
Source:		http://www.tcob1.uklinux.net/files/%{name}-%{version}.tar.bz2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vacation is a port of the 386BSD vacation program (an automatic
mail-answering program found on many Unix systems) to Linux.

%prep
%setup -q

%build
rm -f vacation
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}

make install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/vacation

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	ChangeLog README vacation-1.2.1.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,vacation-1.2.1.lsm}.gz
%attr(755,root,root) %{_bindir}/vacation 
%{_mandir}/man1/vacation.1.gz
