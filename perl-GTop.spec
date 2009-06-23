#
# Conditional build:
%bcond_with	tests	# perform "make test" (requires /proc access)
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	GTop
Summary:	GTop - Perl interface to libgtop
Summary(pl.UTF-8):	GTop - interfejs perlowy do libgtop
Name:		perl-GTop
Version:	0.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/GTop/%{pdir}-%{version}.tar.gz
# Source0-md5:	c3b1f36c3c9e1031f783027fe1c098d0
Patch0:		%{name}-error_h.patch
URL:		http://search.cpan.org/dist/GTop/
BuildRequires:	libgtop-devel >= 2.0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is a Perl interface to libgtop:
<http://home-of-linux.org/gnome/libgtop/>.

See also: Stas Bekman's Apache::VMonitor
<http://www.cpan.org/modules/by-module/Apache/>.

%description -l pl.UTF-8
Ten pakiet jest perlowym interfejsem do libgtop:
<http://home-of-linux.org/gnome/libgtop/>.

Warto zobaczyć także Apache::VMonitor Stasa Bekmana:
<http://www.cpan.org/modules/by-module/Apache/>.

%prep
%setup -q -n %{pdir}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/auto/GTop
%{perl_vendorarch}/auto/GTop/GTop.bs
%attr(755,root,root) %{perl_vendorarch}/auto/GTop/GTop.so
%{perl_vendorarch}/config.pl
%{_mandir}/man3/*
