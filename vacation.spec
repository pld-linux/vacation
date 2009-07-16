Summary:	Automatic mail answering program for Linux
Summary(pl.UTF-8):	Autoresponder pocztowy dla Linuksa
Name:		vacation
Version:	1.2.7.0
Release:	1
License:	GPL
Group:		Applications/Mail
Source0:	http://dl.sourceforge.net/vacation/%{name}-%{version}.tar.gz
# Source0-md5:	cae9253eee4c2e68af01bc6b1f469cd2
URL:		http://vacation.sourceforge.net/
BuildRequires:	gdbm-devel
Conflicts:	zmailer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vacation is a port of the 386BSD vacation program (an automatic
mail-answering program found on many Unix systems) to Linux.

%description -l pl.UTF-8
Vacation to port programu vacation z 386BSD (programu automatycznie
odpowiadającego na pocztę) na Linuksa.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,5}}

install vacation vaclook $RPM_BUILD_ROOT%{_bindir}
install vacation.man $RPM_BUILD_ROOT%{_mandir}/man1/vacation.1
install vaclook.man $RPM_BUILD_ROOT%{_mandir}/man1/vaclook.1

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
%doc AUTHORS ChangeLog KNOWN_BUGS README README.smrsh TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
