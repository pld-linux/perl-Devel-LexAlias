%define		pdir	Devel
%define		pnam	LexAlias
%include	/usr/lib/rpm/macros.perl
Summary:	Devel::LexAlias - alias lexical variables
#Summary(pl.UTF-8):	
Name:		perl-Devel-LexAlias
Version:	0.05
Release:	2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1a4f70dff1a47b3eb96bdeac50db2ec5
URL:		http://search.cpan.org/dist/Devel-LexAlias/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::LexAlias provides the ability to alias a lexical variable in a
subroutines scope to one of your choosing.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorarch}/Devel/*.pm
%dir %{perl_vendorarch}/auto/Devel/LexAlias
%attr(755,root,root) %{perl_vendorarch}/auto/Devel/LexAlias/*.so
%{_mandir}/man3/*
