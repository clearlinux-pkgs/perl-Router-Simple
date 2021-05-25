#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Router-Simple
Version  : 0.17
Release  : 19
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Router-Simple-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Router-Simple-0.17.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libr/librouter-simple-perl/librouter-simple-perl_0.17-1.debian.tar.xz
Summary  : 'simple HTTP router'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Router-Simple-license = %{version}-%{release}
Requires: perl-Router-Simple-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
# NAME
Router::Simple - simple HTTP router
# SYNOPSIS
use Router::Simple;
my $router = Router::Simple->new();
$router->connect('/', {controller => 'Root', action => 'show'});
$router->connect('/blog/{year}/{month}', {controller => 'Blog', action => 'monthly'});

%package dev
Summary: dev components for the perl-Router-Simple package.
Group: Development
Provides: perl-Router-Simple-devel = %{version}-%{release}
Requires: perl-Router-Simple = %{version}-%{release}

%description dev
dev components for the perl-Router-Simple package.


%package license
Summary: license components for the perl-Router-Simple package.
Group: Default

%description license
license components for the perl-Router-Simple package.


%package perl
Summary: perl components for the perl-Router-Simple package.
Group: Default
Requires: perl-Router-Simple = %{version}-%{release}

%description perl
perl components for the perl-Router-Simple package.


%prep
%setup -q -n Router-Simple-0.17
cd %{_builddir}
tar xf %{_sourcedir}/librouter-simple-perl_0.17-1.debian.tar.xz
cd %{_builddir}/Router-Simple-0.17
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Router-Simple-0.17/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Router-Simple
cp %{_builddir}/Router-Simple-0.17/LICENSE %{buildroot}/usr/share/package-licenses/perl-Router-Simple/39916610619ca187786c4836f46462487e0eea7d
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Router-Simple/2f50f843052c546a8a41a027c49ae2a712873a03
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Router::Simple.3
/usr/share/man/man3/Router::Simple::Cookbook.3
/usr/share/man/man3/Router::Simple::Declare.3
/usr/share/man/man3/Router::Simple::Route.3
/usr/share/man/man3/Router::Simple::SubMapper.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Router-Simple/2f50f843052c546a8a41a027c49ae2a712873a03
/usr/share/package-licenses/perl-Router-Simple/39916610619ca187786c4836f46462487e0eea7d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Router/Simple.pm
/usr/lib/perl5/vendor_perl/5.34.0/Router/Simple/Cookbook.pod
/usr/lib/perl5/vendor_perl/5.34.0/Router/Simple/Declare.pm
/usr/lib/perl5/vendor_perl/5.34.0/Router/Simple/Route.pm
/usr/lib/perl5/vendor_perl/5.34.0/Router/Simple/SubMapper.pm
