#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define	pdir	GTop
Summary:	GTop - Perl interface to libgtop
Summary(pl):	GTOP - perlowy interfejs do libgtop
Name:		perl-GTop
Version:	0.10
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
BuildRequires:	libgtop-devel
BuildRequires:	perl-devel >= 5.6
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
  GTOP_LIB=`libgtop-config --libs | perl -we '<>=~/^-L(\S+)/&&print $1'` \
  GTOP_INCLUDE=`libgtop-config --cflags | perl -we '<>=~/^-I(\S+)/&&print $1'` \
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 

%{__make} OPTIMIZE="%{rpmcflags}"

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
