%define upstream_name    RTF-Writer
Name:       perl-%{upstream_name}
Version:    1.11
Release:    6

Summary:    for generating documents in Rich Text Format
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/RTF-Writer
Source0:    https://cpan.metacpan.org/authors/id/S/SB/SBURKE/RTF-Writer-%{version}.tar.gz

BuildRequires:	make
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Path)
BuildRequires: perl(Image::Size)
BuildRequires: perl(UNIVERSAL)
BuildRequires: perl(strict)
BuildRequires: perl-devel
BuildArch: noarch

%description
This module is for generating documents in Rich Text Format. 

This module is a class; an object belonging to this class acts like an
output filehandle, and calling methods on it causes RTF text to be written.

Incidentally, this module also exports a few useful functions, upon
request.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog README META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.110.0-2mdv2011.0
+ Revision: 658877
- rebuild for updated spec-helper

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.110.0-1mdv2010.0
+ Revision: 404359
- rebuild using %1.11 Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.11-4mdv2009.0
+ Revision: 258331
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.11-3mdv2009.0
+ Revision: 246409
- rebuild

* Mon Mar 03 2008 Olivier Thauvin <nanardon@mandriva.org> 1.11-1mdv2008.1
+ Revision: 178007
- import perl-RTF-Writer


