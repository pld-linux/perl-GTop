#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	GTop
Summary:	GTop - Perl interface to libgtop
Summary(pl):	GTop - perlowy interfejs do libgtop
Name:		perl-GTop
Version:	0.10
Release:	5
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	1920b8105003c46031000ae16e859a41
BuildRequires:	libgtop-devel >= 2.0
BuildRequires:	perl-devel >= 5.6
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is a Perl interface to libgtop:
http://home-of-linux.org/gnome/libgtop/

See also: Stas Bekman's Apache::VMonitor
http://www.cpan.org/modules/by-module/Apache/

%description -l pl
Ten pakiet jest perlowym interfejsem do libgtop:
http://home-of-linux.org/gnome/libgtop/

Warto zobaczyæ tak¿e Apache::VMonitor Stasa Bekmana:
http://www.cpan.org/modules/by-module/Apache/

%prep
%setup -q -n %{pdir}-%{version}

%build
GTOP_LIB="`pkg-config --libs libgtop-2.0`" \
GTOP_INCLUDE="`pkg-config --cflags libgtop-2.0`" \
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}" \
	INC="`pkg-config --cflags libgtop-2.0`" \
	EXTRALIBS="`pkg-config --libs libgtop-2.0`"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/GTop
%dir %{perl_vendorarch}/auto/GTop
%attr(755,root,root) %{perl_vendorarch}/auto/GTop/*.so
%{perl_vendorarch}/auto/GTop/*.bs
%dir %{perl_vendorarch}/auto/GTop/Server
%attr(755,root,root) %{perl_vendorarch}/auto/GTop/Server/*.so
%{perl_vendorarch}/auto/GTop/Server/*.bs
%{_mandir}/man3/*
