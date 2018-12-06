#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Router-Simple
Version  : 0.17
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Router-Simple-0.17.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TO/TOKUHIROM/Router-Simple-0.17.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libr/librouter-simple-perl/librouter-simple-perl_0.17-1.debian.tar.xz
Summary  : 'simple HTTP router'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Router-Simple-license = %{version}-%{release}
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

%description dev
dev components for the perl-Router-Simple package.


%package license
Summary: license components for the perl-Router-Simple package.
Group: Default

%description license
license components for the perl-Router-Simple package.


%prep
%setup -q -n Router-Simple-0.17
cd ..
%setup -q -T -D -n Router-Simple-0.17 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Router-Simple-0.17/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
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
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Router-Simple/LICENSE
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
/usr/lib/perl5/vendor_perl/5.28.1Router/Simple.pm
/usr/lib/perl5/vendor_perl/5.28.1Router/Simple/Cookbook.pod
/usr/lib/perl5/vendor_perl/5.28.1Router/Simple/Declare.pm
/usr/lib/perl5/vendor_perl/5.28.1Router/Simple/Route.pm
/usr/lib/perl5/vendor_perl/5.28.1Router/Simple/SubMapper.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Router::Simple.3
/usr/share/man/man3/Router::Simple::Cookbook.3
/usr/share/man/man3/Router::Simple::Declare.3
/usr/share/man/man3/Router::Simple::Route.3
/usr/share/man/man3/Router::Simple::SubMapper.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Router-Simple/LICENSE
