Summary:	Automatic mail answering program for Linux
Summary(pl):	Autoresponder
Name:		vacation
Version:	1.2.1
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://www.tcob1.uklinux.net/files/%{name}-%{version}.tar.bz2
URL:		http://www.tcob1.uklinux.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vacation is a port of the 386BSD vacation program (an automatic
mail-answering program found on many Unix systems) to Linux.

%description -l pl
Vacation to port programu vacation z 386BSD (programu automatycznie
odpowiadaj±cego na pocztê) na Linuksa.

%prep
%setup -q

%build
rm -f vacation
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README}.gz
%attr(755,root,root) %{_bindir}/vacation 
%{_mandir}/man1/vacation.1.gz
