Summary:	Automatic mail answering program for Linux
Summary(pl):	Autoresponder pocztowy dla linuxa
Name:		vacation
Version:	1.2.6.1
Release:	1
License:	GPL
Group:		Applications/Mail
BuildRequires:	gdbm-devel
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vacation is a port of the 386BSD vacation program (an automatic
mail-answering program found on many Unix systems) to Linux.

%description -l pl
Vacation to port programu vacation z 386BSD (programu automatycznie
odpowiadaj±cego na pocztê) na Linuksa.

%prep
%setup -q -n %{name}

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}

install vacation ${RPM_BUILD_ROOT}%{_bindir}/vacation
install vaclook ${RPM_BUILD_ROOT}%{_bindir}/vaclook
install vacation.man ${RPM_BUILD_ROOT}%{_mandir}/man1/vacation.1
install vaclook.man ${RPM_BUILD_ROOT}%{_mandir}/man1/vaclook.1

gzip -9nf ChangeLog README README.smrsh

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -d /etc/smrsh ]; then
  ln -sf %{_bindir}/vacation /etc/smrsh
fi

%postun
if [ -e /etc/smrsh/vacation ]; then
  rm -f /etc/smrsh/vacation
fi

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,README.smrsh}.gz
%attr(755,root,root) %{_bindir}/vacation
%attr(755,root,root) %{_bindir}/vaclook
%{_mandir}/man1/vacation.1.gz
%{_mandir}/man1/vaclook.1.gz
